from datetime import datetime

def validate_task_title(title):
    if not title or not title.strip() :
        print('Error: Title cannot be empty')
        return False
    return True
    
def validate_task_description(description):
    if not description or not description.strip():
        print('Error: Description cannot be empty')
        return False
    return True
       
    
def validate_due_date(due_date):
    if not due_date or not due_date.strip():
        raise ValueError('Error :Due_date cannot be empty')
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print(f"Invalid format: '{due_date}' must use the YYYY-MM-DD template.")
        return False
        
        
    