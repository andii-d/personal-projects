#   import tkinter as tk
#   from tkinter import messagebox
#   
#   def add_task():
#       task = entry.get()
#       user = user_entry.get()
#       if task and user:
#           task_list.insert(tk.END, f"{user}: {task}")
#           entry.delete(0, tk.END)
#           user_entry.delete(0, tk.END)
#       else:
#           messagebox.showwarning("Warning", "Please enter both a user and a task.")
#   
#   def remove_task():
#       try:
#           selected_task_index = task_list.curselection()[0]
#           task_list.delete(selected_task_index)
#       except IndexError:
#           messagebox.showwarning("Warning", "Please select a task to remove.")
#   
#   def toggle_complete():
#       try:
#           selected_task_index = task_list.curselection()[0]
#           task = task_list.get(selected_task_index)
#           if task.startswith("[ ] "):
#               task = "[X] " + task[4:]
#           elif task.startswith("[X] "):
#               task = "[ ] " + task[4:]
#           task_list.delete(selected_task_index)
#           task_list.insert(selected_task_index, task)
#       except IndexError:
#           messagebox.showwarning("Warning", "Please select a task to toggle.")
#   
#   def save_tasks():
#       tasks = task_list.get(0, tk.END)
#       with open("tasks.txt", "w") as file:
#           for task in tasks:
#               file.write(f"{task}\n")
#       messagebox.showinfo("Info", "Tasks have been saved to tasks.txt")
#   
#   root = tk.Tk()
#   root.title("To-Do List")
#   
#   entry = tk.Entry(root, width=30)
#   entry.pack(pady=10)
#   
#   user_entry = tk.Entry(root, width=30)
#   user_entry.pack()
#   
#   add_button = tk.Button(root, text="Add Task", command=add_task)
#   add_button.pack()
#   
#   task_list = tk.Listbox(root, height=10, width=50)
#   task_list.pack()
#   
#   remove_button = tk.Button(root, text="Remove Task", command=remove_task)
#   remove_button.pack()
#   
#   toggle_button = tk.Button(root, text="Toggle Complete", command=toggle_complete)
#   toggle_button.pack()
#   
#   save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
#   save_button.pack()
#   
#   root.mainloop()
#   

# ABOVE CODE IS CHATGPT'S CODE, FOR REFERENCE OF USING TKINTER MODULE 

class Account:
    def __init__(self, username):
        self.username = username
    
with open('usernames.txt', 'a') as f:
    pass

username_input = input("Enter the name of the person's tasks you want to view: ")

while True:
    try:
        if username_input not in 

task_ccount = Account(username)

        
tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append({"task": task, "complete": False})
    print("Task added.")

def removeTask():
    if tasks:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. [{task['complete']}]", task['task'])
        
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")

def toggleComplete():
    if tasks:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. [{task['complete']}]", task['task'])
        
        task_index = int(input("Enter the task number to toggle completion: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['complete'] = not tasks[task_index]['complete']
            print(f"Toggled completion of task: {tasks[task_index]['task']}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to toggle.")

def viewTasks():
    if tasks:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. [{task['complete']}]", task['task'])
    else:
        print("No tasks to display.")

while True:
    print("\nText-Based To-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Toggle Complete")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addTask()
    elif choice == "2":
        removeTask()
    elif choice == "3":
        toggleComplete()
    elif choice == "4":
        viewTasks()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


# add to it so 