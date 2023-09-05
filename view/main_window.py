import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from controller import task_controller  

def populate_tasks(task_list_frame, selected_index=None):
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    tasks = task_controller.fetch_tasks()

    for i, (title, description, due_date, completed) in enumerate(tasks):
        tick_symbol = "✅" if completed else "☐"

        tick_label = tk.Label(task_list_frame, text=tick_symbol, fg="green" if completed else "black", cursor="hand2")
        tick_label.grid(row=i*2, column=0, sticky="w")

        def toggle_tick(title=title):
            if completed:
                task_controller.untick_task(title)
            else:
                task_controller.tick_task(title)
            populate_tasks(task_list_frame, selected_index)

        tick_label.bind("<Button-1>", lambda event, title=title: toggle_tick(title))

        task_str = f"{i+1}. {title} ({due_date})"
        task_label = tk.Label(task_list_frame, text=task_str, fg="blue", cursor="hand2")
        task_label.grid(row=i*2, column=1, sticky="w")

        def toggle_desc(i=i):
            populate_tasks(task_list_frame, selected_index=i if i != selected_index else None)

        task_label.bind("<Button-1>", lambda event, i=i: toggle_desc(i))

        if i == selected_index:
            desc_label = tk.Label(task_list_frame, text=f"Description: {description}")
            desc_label.grid(row=i*2 + 1, column=0, columnspan=2, sticky="w")

def initialize_view():
    window = tk.Tk()
    window.title("Task Manager")
    
    notebook = ttk.Notebook(window)
    
    # Create frames
    add_task_frame = ttk.Frame(notebook)
    task_list_frame = ttk.Frame(notebook)
    
    # Add frames to notebook
    notebook.add(add_task_frame, text='Add Task')
    notebook.add(task_list_frame, text='List & Modify Tasks')
    
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
    
    def add_and_fetch():
        task_controller.add_task(title_entry.get(), desc_entry.get(), due_date_entry.get())
        populate_tasks(task_list_frame)
    
    tk.Button(add_task_frame, text="Add Task", command=add_and_fetch).pack()
    
    # Initial population of tasks
    populate_tasks(task_list_frame)
    
    notebook.pack(expand=1, fill='both')
    
    window.mainloop()

if __name__ == "__main__":
    initialize_view()
