# Simple To-Do List Application
# This program allows users to manage tasks through a command-line interface

def main():
    # Initialize an empty list to store tasks
    tasks = []
    
    # Display welcome message
    print("Welcome to the To-Do List App!")
    
    # Main program loop - runs until user chooses to quit
    while True:
        # Display menu options
        print("\nOptions: 1=Add, 2=View, 3=Delete, 4=Quit")
        
        # Get user input for menu selection
        choice = input("Choose an option: ")
        
        # Option 1: Add a new task
        if choice == "1":
            # Get task description from user
            task = input("Enter task: ").strip()
            
            # Check if task is not empty
            if task:
                # Add task to the list
                tasks.append(task)
                # Confirm addition
                print("Task added!")
            else:
                # Inform user if they tried to add an empty task
                print("Task can't be empty.")
                
        # Option 2: View all tasks
        elif choice == "2":
            # Check if there are any tasks to display
            if not tasks:
                # Inform user if no tasks are present
                print("No tasks yet!")
            else:
                # Display all tasks with numbering
                print("\nYour Tasks:")
                # Display tasks with numbering
                for i, task in enumerate(tasks, 1):
                    #
                    print(f"{i}. {task}")
                    
        # Option 3: Delete a task
        elif choice == "3":
            # Check if there are any tasks to delete
            if not tasks:
                print("No tasks to delete!")
                continue  # Skip the rest of this loop iteration
                
            # Display all tasks so user can see what to delete
            print("\nYour Tasks:")
            # Display tasks with numbering
            for i, task in enumerate(tasks, 1):
                # Display each task with its number
                print(f"{i}. {task}")
                
            # Try to get and process the task number to delete
            try:
                # Get task number from user
                num = int(input("Enter task number to delete: "))
                
                # Check if the number is valid
                if 1 <= num <= len(tasks):
                    # Remove the task from the list
                    removed = tasks.pop(num-1)
                    # Confirm deletion
                    print(f"Deleted: {removed}")
                else:
                    # Inform user if number is out of range
                    print("Invalid task number!")
            except ValueError:
                # Handle non-numeric input
                print("Please enter a number!")
                
        # Option 4: Quit the application
        elif choice == "4":
            # Confirm exit
            print("Goodbye!")
            # break the loop
            break  # Exit the loop and end the program
            
        # Handle invalid menu options
        else:
            # Inform user of invalid choice
            print("Invalid option! Choose 1-4.")

# This ensures the program only runs when executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()

    # Confirm program completion
    print("To-Do List App has ended.")

#note: I kept it 100; This code was crafted by Justin Wold with ❤️.