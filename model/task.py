from .database import connect_db

def create_task(title, description, due_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
    conn.commit()
    conn.close()

def fetch_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT title, due_date FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks