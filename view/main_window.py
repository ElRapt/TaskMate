import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from controller import task_controller

window = None

def initialize_view():
    global window
    if window:
        window.destroy()

    window = tk.Tk()
    window.title("Task Manager")
    
    notebook = ttk.Notebook(window)
    
    add_task_frame = ttk.Frame(notebook)
    list_task_frame = ttk.Frame(notebook)
    
    notebook.add(add_task_frame, text='Add Task')
    notebook.add(list_task_frame, text='List & Modify Tasks')
    
    tk.Label(add_task_frame, text="Title").pack()
    title_entry = tk.Entry(add_task_frame)
    title_entry.pack()
    
    tk.Label(add_task_frame, text="Description").pack()
    desc_entry = tk.Entry(add_task_frame)
    desc_entry.pack()
    
    tk.Label(add_task_frame, text="Due Date").pack()
    due_date_entry = DateEntry(add_task_frame)
    due_date_entry.pack()

    def add_and_fetch():
        task_controller.add_task(title_entry.get(), desc_entry.get(), due_date_entry.get())
        initialize_view()  # Reinitialize the view

    tk.Button(add_task_frame, text="Add Task", command=add_and_fetch).pack()
    
    task_list_frame = tk.Frame(list_task_frame)
    task_list_frame.pack(expand=1, fill='both')
    
    tasks = task_controller.fetch_tasks()

    for i, (title, due_date) in enumerate(tasks):
        task_str = f"{i+1}. {title} ({due_date})"
        
        task_label = tk.Label(task_list_frame, text=task_str)
        task_label.grid(row=i, column=0, sticky="w")
        
        def task_delete(title=title):
            task_controller.delete_task(title)
            initialize_view()

        delete_button = tk.Button(task_list_frame, text="❌", command=lambda title=title: task_delete(title), fg='red')
        delete_button.grid(row=i, column=1)

    notebook.pack(expand=1, fill='both')
    
    window.mainloop()

# Call the function to initialize the view
initialize_view()
