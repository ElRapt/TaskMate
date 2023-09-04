import tkinter as tk
from controller import task_controller

def initialize_view():
    window = tk.Tk()
    window.title("Task Manager")
    
    tk.Label(window, text="Title").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()
    
    tk.Label(window, text="Description").pack()
    desc_entry = tk.Entry(window)
    desc_entry.pack()
    
    tk.Label(window, text="Due Date").pack()
    due_date_entry = tk.Entry(window)
    due_date_entry.pack()

    tk.Button(window, text="Add Task", command=lambda: task_controller.add_task(title_entry.get(), desc_entry.get(), due_date_entry.get())).pack()

    window.mainloop()
