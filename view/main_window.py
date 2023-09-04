import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from controller import task_controller

def initialize_view():
    window = tk.Tk()
    window.title("Task Manager")
    
    notebook = ttk.Notebook(window)
    
    # Create frames
    add_task_frame = ttk.Frame(notebook)
    list_task_frame = ttk.Frame(notebook)
    
    # Add frames to notebook
    notebook.add(add_task_frame, text='Add Task')
    notebook.add(list_task_frame, text='List & Modify Tasks')
    
    # Add Task tab content
    tk.Label(add_task_frame, text="Title").pack()
    title_entry = tk.Entry(add_task_frame)
    title_entry.pack()
    
    tk.Label(add_task_frame, text="Description").pack()
    desc_entry = tk.Entry(add_task_frame)
    desc_entry.pack()
    
    tk.Label(add_task_frame, text="Due Date").pack()
    due_date_entry = DateEntry(add_task_frame)
    due_date_entry.pack()

    # Helper function to update list of tasks after adding a new task
    def add_and_fetch():
        task_controller.add_task(title_entry.get(), desc_entry.get(), due_date_entry.get())
        task_controller.fetch_tasks()

    tk.Button(add_task_frame, text="Add Task", command=add_and_fetch).pack()
    
    # List & Modify Tasks tab content

    # Fetch tasks from database
    tasks = task_controller.fetch_tasks()

    # Create Text Widget
    text_widget = tk.Text(list_task_frame, wrap='word', height=20, width=50)
    text_widget.pack(expand=1, fill='both')

    # Insert tasks into Text Widget
    for i, (title, due_date) in enumerate(tasks):
        task_str = f"{i+1}. {title} ({due_date})\n"
        text_widget.insert('end', task_str)

    # Make Text Widget Read-Only
    text_widget.config(state='disabled')
    
    notebook.pack(expand=1, fill='both')
    
    window.mainloop()
