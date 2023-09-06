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
    cursor.execute("SELECT id, title, description, due_date, completed FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def delete_task(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()

def tick_task(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (id,))
    conn.commit()
    conn.close()

def untick_task(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=0 WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_task(id, title, description, due_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title=?, description=?, due_date=? WHERE id=?", (title, description, due_date, id))
    conn.commit()
    conn.close()