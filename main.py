# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task,mark_task_as_complete,view_pending_tasks,calculate_progress
None
SHOW_MENU = False
# Define the main function
def main():
    while True:
        if SHOW_MENU:
           print("Task Management System")
           print("1. Add Task")
           print("2. Mark Task as Complete")
           print("3. View Pending Tasks")
           print("4. View Progress")
           print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            while True:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                
                if add_task(title,description,due_date):
                    break
                print('Lets try that again\n')

        elif choice == "2":
            # show tasks to user
            # view_pending_tasks()
            try:
                index = int(input("Enter the index of the task to complete: "))
                mark_task_as_complete(index)
            except ValueError:
                print("Error: Please enter a valid number index.")

        elif choice =='3':
            view_pending_tasks()

        elif choice =='4':
            progress=calculate_progress()
            print(f'\n Your current completeon progress is {progress:.2f}%')
        
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
