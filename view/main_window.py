import tkinter as tk
from tkinter import ttk
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
    due_date_entry = tk.Entry(add_task_frame)
    due_date_entry.pack()

    tk.Button(add_task_frame, text="Add Task", command=lambda: task_controller.add_task(title_entry.get(), desc_entry.get(), due_date_entry.get())).pack()
    
    # List & Modify Tasks tab content
    # ... Populate as needed
    
    notebook.pack(expand=1, fill='both')
    
    window.mainloop()
