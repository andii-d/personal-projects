import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    user = user_entry.get()
    if task and user:
        task_list.insert(tk.END, f"{user}: {task}")
        entry.delete(0, tk.END)
        user_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both a user and a task.")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def toggle_complete():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        if task.startswith("[ ] "):
            task = "[X] " + task[4:]
        elif task.startswith("[X] "):
            task = "[ ] " + task[4:]
        task_list.delete(selected_task_index)
        task_list.insert(selected_task_index, task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to toggle.")

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    messagebox.showinfo("Info", "Tasks have been saved to tasks.txt")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

user_entry = tk.Entry(root, width=30)
user_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, height=10, width=50)
task_list.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

toggle_button = tk.Button(root, text="Toggle Complete", command=toggle_complete)
toggle_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

root.mainloop()
