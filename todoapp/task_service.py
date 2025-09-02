from db import get_connection

def add_task(task):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Task added successfully!")

def view_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    if rows:
        for (id, task, status) in rows:
            print(f"{id}. {task} [{status}]")
    else:
        print("📭 No tasks found.")
    cursor.close()
    conn.close()

def update_task(task_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=%s WHERE id=%s", (new_status, task_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("🔄 Task updated successfully!")

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("🗑 Task deleted successfully!")
