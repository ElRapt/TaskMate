from model import task

def add_task(title, description, due_date):
    task.create_task(title, description, due_date)
