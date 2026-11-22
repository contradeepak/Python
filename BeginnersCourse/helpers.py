from colorama import init, Fore

init(autoreset=True)

def display(message, is_warning=False):
    if is_warning:
        print(Fore.YELLOW + "This is a warning")
        print(message)
    else:
        print(Fore.RED + "This is red text")
        print(Fore.GREEN + "This is green text")
        print(Fore.YELLOW + "This is yellow text")
