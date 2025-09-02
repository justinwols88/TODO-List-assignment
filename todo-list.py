# Simple To-Do List Application
# This program allows users to manage tasks through a command-line interface

# Function to display the menu
def display_menu():
    # Display the menu
    """Display the main menu options."""
    # Display the menu
    print("\nOptions: 1=Add, 2=View, 3=Delete, 4=Quit")

def add_task(tasks):
    # Display the menu
    """Add a new task to the list."""
    # Get user input
    task = input("Enter task: ").strip()
    # Check if task is not empty
    if task:
        # Add the task
        tasks.append(task)
        # Display the menu
        print("Task added!")
        # Display the menu
    else:
        # Handle empty task
        print("Task can't be empty.")

def view_tasks(tasks):
    # Display the tasks
    """View all tasks in the list."""
    # Check if tasks list is empty
    if not tasks:
        # No tasks to display
        print("No tasks yet!")
        # Display the menu
    else:
        # Display the tasks
        print("\nYour Tasks:")
        # Display each task with its number
        for i, task in enumerate(tasks, 1):
            # Display each task with its number
            print(f"{i}. {task}")

def delete_task(tasks):
    # Display the menu
    """Delete a task from the list."""
    # Check if tasks list is empty
    if not tasks:
        # No tasks to delete
        print("No tasks to delete!")
        # Display the menu
        return
    # Display current tasks
    view_tasks(tasks)
    # Get user input
    try:
        # Get user input
        num = int(input("Enter task number to delete: "))
        # Validate task number
        if 1 <= num <= len(tasks):
            # Remove the task
            removed = tasks.pop(num-1)
            # Display the menu
            print(f"Deleted: {removed}")
            # Display the menu
        else:
            # Handle invalid input
            print("Invalid task number!")
            # Handle invalid input
    except ValueError:
        # Handle invalid input
        print("Please enter a number!")
#
def main():
    """Main function to run the To-Do List CLI app."""
    # Initialize task list
    tasks = []
    # Welcome message
    print("Welcome to the To-Do List App!")
    # Main loop of the TODO app
    try:
        # Start the main loop
        while True:
            # Display the menu
            display_menu()
            # Get user choice
            choice = input("Choose an option: ")
            # Process user choice
            if choice == "1":
                # Add a task
                add_task(tasks)
            # View tasks
            elif choice == "2":
                # View all tasks
                view_tasks(tasks)
            # Delete tasks
            elif choice == "3":
                # Delete a task
                delete_task(tasks)
            # Quit
            elif choice == "4":
                # Quit the application
                print("Goodbye!")
                # Clean up resources if needed
                break
            # Handle invalid input
            else:
                # Inform the user about the invalid option
                print("Invalid option! Choose 1-4.")
    # Clean up resources if needed
    finally:
        # Display end message
        print("To-Do List App has ended.")

if __name__ == "__main__":
    # Start the main program
    main()
    # Display end message
    print("To-Do List App has ended.")

# This code was crafted by Justin Wold with ❤️.
# to run this program open a terminal, browser to parent folder and type: python todo-list.py