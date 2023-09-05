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
    cursor.execute("SELECT title, description, due_date, completed FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def delete_task(title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE title=?", (title,))
    conn.commit()
    conn.close()

def tick_task(title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE title=?", (title,))
    conn.commit()
    conn.close()