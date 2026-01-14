import os, re, json, tempfile, subprocess, shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from github import Github

ECOSYSTEMS = {
    "npm-eresolve": {
        "image": "node:16",
        "setup": "npm install -g npm@7",
        "cmds": [
            "npm ci --ignore-scripts",
            "npm install --ignore-scripts --legacy-peer-deps"
        ],
        "err": re.compile(r"npm ERR! code ERESOLVE", re.IGNORECASE),
    },
    "npm-peer-dep": {
        "image": "node:16",
        "setup": "npm install -g npm@7",
        "cmds": [
            "npm ci --ignore-scripts",
            "npm install --ignore-scripts --legacy-peer-deps"
        ],
        "err": re.compile(r"npm ERR! peer dep", re.IGNORECASE),
    },
    "pip-conflict": {
        "image": "python:3.9",
        "setup": None,
        "cmds": [
            "pip install --no-build-isolation --no-deps -r requirements.txt",
            "pip install --no-build-isolation -r requirements.txt"
        ],
        "err": re.compile(
            r"ERROR: (?:Could not install|ResolutionImpossible)",
            re.IGNORECASE
        ),
    },
    "poetry-conflict": {
        "image": "python:3.9",
        "setup": None,
        "cmds": [
            "pip install poetry && poetry install --no-root "
            "--no-interaction --no-scripts",
            "poetry install --no-root --no-interaction --no-scripts"
        ],
        "err": re.compile(r"ResolutionImpossible", re.IGNORECASE),
    },
    "bundler-compat": {
        "image": "ruby:2.7",
        "setup": None,
        "cmds": [
            "bundle install --jobs=1 --retry=2 --without development test"
        ],
        "err": re.compile(
            r"Bundler could not find compatible versions",
            re.IGNORECASE
        ),
    },
}

GITHUB_TOKEN = ""
INPUT = Path("mined_conflicts.jsonl")
OUTPUT = Path("validated_results.jsonl")
GITHUB_TOKEN = ""



def load_entries():
    for line in INPUT.open():
        yield json.loads(line)


def get_done():
    seen = set()
    if OUTPUT.exists():
        for l in OUTPUT.open():
            r = json.loads(l)
            seen.add((r["repo"], r["issue_number"], r["comment_id"]))
    return seen


def record(entry, success, out):
    r = {
        **entry,
        "validation_success": success,
        "install_output": out.strip(),
        "validated_at": __import__("datetime").datetime.utcnow().isoformat() + "Z"
    }
    with OUTPUT.open("a") as f:
        f.write(json.dumps(r) + "\n")


def docker_run(workdir, image, cmd):
    full = [
        "docker", "run", "--rm", "-v", f"{workdir}:/app",
        "-w", "/app", image, "sh", "-c", cmd
    ]
    p = subprocess.run(full, capture_output=True, text=True)
    return p.stdout + p.stderr


def process(entry, done):
    key = (entry["repo"], entry["issue_number"], entry["comment_id"])
    if key in done:
        return

    cfg = ECOSYSTEMS[entry["ecosystem"]]
    tmp = Path(tempfile.mkdtemp(prefix="val_"))
    out, success = "", False

    try:
        repo_url = f"https://github.com/{entry['repo']}.git"
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, tmp / "r"],
            check=True
        )
        subprocess.run(
            ["git", "-C", tmp / "r", "fetch", "--depth", "1",
             "origin", entry["base_commit"]],
            check=True
        )
        subprocess.run(
            ["git", "-C", tmp / "r", "checkout", entry["base_commit"]],
            check=True
        )
        wd = str(tmp / "r")

        if cfg["setup"]:
            out += docker_run(wd, cfg["image"], cfg["setup"])

        for cmd in cfg["cmds"]:
            out += docker_run(wd, cfg["image"], cmd)
            if cfg["err"].search(out):
                success = True
                break

    except Exception as e:
        out += f"\n Pipeline error: {e}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    record(entry, success, out)


if __name__ == "__main__":
    WORKERS = os.cpu_count() or 4  # <-- define WORKERS (missing in your code)
    OUTPUT.touch(exist_ok=True)
    done = get_done()
    entries = list(load_entries())

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(process, e, done) for e in entries]
        for _ in tqdm(as_completed(futures),
                      total=len(futures),
                      desc="Validating"):
            pass

    print("Done; results in", OUTPUT)
