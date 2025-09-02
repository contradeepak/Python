from task_service import add_task, view_tasks, update_task, delete_task

def menu():
    while True:
        print("\n=== 📝 To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (Pending/Completed): ")
            update_task(task_id, new_status)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    menu()
