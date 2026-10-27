
from todo import TodoApp


def main():
    app = TodoApp()

    while True:
        print("\n====== CLI TO-DO APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            app.add_task(title)

        elif choice == "2":
            app.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                app.complete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                app.delete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "5":
            print("Goodbye! Your tasks have been saved.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
