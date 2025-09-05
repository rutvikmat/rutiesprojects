# A simple To-Do List application in Python

# The list to store all the tasks
tasks = []


def show_menu():
    """Displays the main menu to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a New Task")
    print("3. Mark a Task as Complete")
    print("4. Delete a Task")
    print("5. Exit")
    print("-----------------------")


def view_tasks():
    """Displays all the tasks in the list."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty. Great job! 👍")
    else:
        for i, task in enumerate(tasks, 1):
            # Check the status and display a checkmark if complete
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. [{status}] {task['name']}")
    print("-----------------------")


def add_task():
    """Adds a new task to the list."""
    task_name = input("Enter the name of the new task: ")
    task_info = {"name": task_name, "completed": False}
    tasks.append(task_info)
    print(f"Task '{task_name}' has been added successfully! 🎉")


def mark_task_complete():
    """Marks a specific task as completed."""
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} has been marked as complete. Well done! ✨")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():
    """Deletes a specific task from the list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' has been deleted. 🗑️")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Main loop to run the application
def main():
    """The main function to run the application loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using the To-Do List App. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()