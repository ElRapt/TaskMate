import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from controller import task_controller 

def populate_tasks(task_list_frame, selected_index=None, edit_index=None):
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    tasks = task_controller.fetch_tasks()

    if edit_index is not None:
        id, title, description, due_date, completed = tasks[edit_index]
        
        tk.Label(task_list_frame, text="Title").grid(row=0, column=0)
        edit_title_entry = tk.Entry(task_list_frame)
        edit_title_entry.grid(row=0, column=1)
        edit_title_entry.insert(0, title)

        tk.Label(task_list_frame, text="Description").grid(row=1, column=0)
        edit_desc_entry = tk.Entry(task_list_frame)
        edit_desc_entry.grid(row=1, column=1)
        edit_desc_entry.insert(0, description)

        tk.Label(task_list_frame, text="Due Date").grid(row=2, column=0)
        edit_due_date_entry = DateEntry(task_list_frame)
        edit_due_date_entry.grid(row=2, column=1)
        edit_due_date_entry.set_date(due_date)


        def update_task():
            new_title = edit_title_entry.get()
            new_desc = edit_desc_entry.get()
            new_due_date = edit_due_date_entry.get_date()
            formatted_due_date = f"{new_due_date.month}/{new_due_date.day}/{str(new_due_date.year)[2:]}"  # Convert to M/D/YY format
            task_controller.update_task(id, new_title, new_desc, formatted_due_date)
            populate_tasks(task_list_frame)

        update_button = tk.Button(task_list_frame, text="Update Task", command=update_task)
        update_button.grid(row=3, column=1)

        return

    for i, (id, title, description, due_date, completed) in enumerate(tasks):
        tick_symbol = "✅" if completed else "☐"

        tick_label = tk.Label(task_list_frame, text=tick_symbol, fg="green" if completed else "black", cursor="hand2")
        tick_label.grid(row=i * 2, column=0, sticky="w")

        def toggle_tick(id=id):
            task_controller.toggle_task(id)
            populate_tasks(task_list_frame, selected_index)

        tick_label.bind("<Button-1>", lambda event, id=id: toggle_tick(id))

        task_str = f"{i + 1}. {title} ({due_date})"
        task_label = tk.Label(task_list_frame, text=task_str, fg="blue", cursor="hand2")
        task_label.grid(row=i * 2, column=1, sticky="w")

        def toggle_desc(i=i):
            populate_tasks(task_list_frame, selected_index=i if i != selected_index else None)

        task_label.bind("<Button-1>", lambda event, i=i: toggle_desc(i))

        def task_delete(id=id):
            task_controller.delete_task(id)
            populate_tasks(task_list_frame)

        delete_button = tk.Button(task_list_frame, text="❌", fg='red', command=lambda id=id: task_delete(id) and populate_tasks(task_list_frame))
        delete_button.grid(row=i * 2, column=2)

        edit_button = tk.Button(task_list_frame, text="✏️", command=lambda i=i: populate_tasks(task_list_frame, edit_index=i))
        edit_button.grid(row=i * 2, column=3)

        if i == selected_index:
            desc_label = tk.Label(task_list_frame, text=f"Description: {description}")
            desc_label.grid(row=i * 2 + 1, column=0, columnspan=4, sticky="w")




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
