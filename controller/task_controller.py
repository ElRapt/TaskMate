from model import task

def add_task(title, description, due_date):
    task.create_task(title, description, due_date)

def fetch_tasks():
    return task.fetch_tasks()

def delete_task(title):
    task.delete_task(title)

def tick_task(title):
    task.tick_task(title)

def untick_task(title):
    task.untick_task(title)
