
from task_manager.validation import validate_task_title,validate_task_description,validate_due_date
# Import validation functions
None

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False
    
    task={'title':title, 'description':description, 'due_date':due_date, 'completed':False}
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0<=index<len(tasks):
        tasks[index]['completed']=True
        print("Task marked as complete!")
    else:
        print('Invalid index')
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending=False
    for i,task in enumerate(tasks):
        if not task['completed']:
            print(f"[{i}] {task['title']} - Due: {task['due_date']}")
            print(f'Description: {task['description']}')
            pending=True
    if not pending:
        print('No pending tasks ')

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count=sum(1 for task in tasks if task['completed'])
    progress=(completed_count/len(tasks))*100
    return progress
    