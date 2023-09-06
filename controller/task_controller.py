from model import task

def add_task(title, description, due_date):
    task.create_task(title, description, due_date)

def fetch_tasks():
    return task.fetch_tasks()

def delete_task(id):
    task.delete_task(id)

def tick_task(id):
    task.tick_task(id)

def untick_task(id):
    task.untick_task(id)

def update_task(id, title, description, due_date):
    task.update_task(id, title, description, due_date)