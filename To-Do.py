# Simple To-Do List

# Initialize an empty list to store tasks
to_do_list = []

# Function to display the list of tasks
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for index, (task, completed) in enumerate(to_do_list, start=1):
            status = "✓" if completed else "✗"
            print(f"{index}. [{status}] {task}")

# Function to add a new task
def add_task(task):
    to_do_list.append((task, False))
    print(f"Added task: '{task}'")

# Function to mark a task as completed
def mark_task_completed(index):
    if 0 <= index < len(to_do_list):
        task, _ = to_do_list[index]
        to_do_list[index] = (task, True)
        print(f"Marked task {index + 1} as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(to_do_list):
        task, _ = to_do_list.pop(index)
        print(f"Deleted task: '{task}'")
    else:
        print("Invalid task number.")

# Main loop to interact with the to-do list
def to_do_list_app():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            view_tasks()

        elif choice == '2':
            task = input("Enter the new task: ")
            add_task(task)

        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: ")) - 1
                mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: ")) - 1
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == '5':
            print("Exiting the to-do list app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the to-do list app
to_do_list_app()
