from time import sleep
import os

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = {}
        self.task_count = 1

    def addTask(self, task):
        task_info = {"task": task, "completed": False}
        self.tasks[self.task_count] = task_info
        self.task_count += 1

    def completedTask(self, username):
        with open(f"{username}_completed_tasks.txt", "a") as f:
            for task_number, task_info in self.tasks.items():
                task = task_info["task"]
                completion = task_info["completed"]
                if completion:
                    completion_state = "True"
                    f.write(f"{task_number}: {task}: {completion_state}\n")

    def removeTask(self, task_number):
        if task_number in self.tasks:
            removed_task = self.tasks.pop(task_number)

            # Update the task numbers for the remaining tasks
            updated_tasks = {}
            # Start from an index of 1 to the end number
            for i in range(1, len(self.tasks) + 1):
                if i < task_number:
                    #
                    updated_tasks[i] = self.tasks[i]
                else:
                    updated_tasks[i] = self.tasks[i + 1]

            self.tasks = updated_tasks
            self.task_count -= 1

            print(f"Removed task {task_number}.")
        else:
            print(f"Task {task_number} not found.")

    def viewAllTasks(self):
        print("")
        for task_number, task_info in self.tasks.items():
                print(f"Task {task_number}: {task_info['task']}")
                sleep(0.3)
        X = input("\nPress enter when finished.")

    def viewIncompleteTasks(self):
        print("")
        for task_number, task_info in self.tasks.items():
            if not task_info["completed"]:
                print(f"Task {task_number}: {task_info['task']}")
                sleep(0.3)
        X = input("\nPress enter when finished.")

    def saveTasks(self):
        with open(f"{self.username}_tasks.txt", "a") as file:
            for task_number, task_info in self.tasks.items():
                task = task_info["task"]
                completion = task_info["completed"]
                completion_state = "True" if completion else "False"
                file.write(f"{task_number}: {task}: {completion_state}\n")

    def loadTasks(self):
        self.tasks = {}
        try:
            with open(f"{self.username}_tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(": ")
                    if len(parts) == 3:
                        task_number, task, completion = parts[0], parts[1].strip(), parts[2]
                        self.tasks[int(task_number)] = {"task": task, "completed": completion == "True"}
        except FileNotFoundError:
            # If the file doesn't exist, create an empty one
            with open(f"{self.username}_tasks.txt", "w"):
                pass

    def editTasks(self, task_number_edit, task_new_edited):
        print("")
        for task_number, task_info in self.tasks.items():
                print(f"Task {task_number}: {task_info['task']}")
        if task_number_edit in self.tasks:
            self.tasks[task_number_edit]["task"] = task_new_edited
            print(f"Task {task_number_edit} updated.")
        else:
            print(f"Task {task_number_edit} not found.")

    def toggleTasks(self, task_number_edit):
        print("")
        if task_number_edit in self.tasks:
            current_completion_state = self.tasks[task_number_edit]["completed"]
            self.tasks[task_number_edit]["completed"] = not current_completion_state

            if task_number_edit in self.tasks:
                removed_task = self.tasks.pop(task_number_edit)

                # Update the task numbers for the remaining tasks
                updated_tasks = {}
                # Start from an index of 1 to the end number
                for i in range(1, len(self.tasks) + 1):
                    if i < task_number_edit:
                        # Adds the current task to the new task dictionary
                        updated_tasks[i] = self.tasks[i]
                    else:
                        updated_tasks[i] = self.tasks[i + 1]

                self.tasks = updated_tasks
                self.task_count -= 1
                pass
            else:
                pass
            print(f"Task {task_number_edit} completed.")
        else:
            print(f"Task {task_number_edit} not found. ")

def main():
    with open('usernames.txt', 'r') as f:
        usernames = [line.strip() for line in f]

    username = input("Enter your name: ")
    if username not in usernames:
        print("\nName does not exist. Creating a new account...\n")
        with open('usernames.txt', 'a') as f:
            f.write(f"{username}\n")

    # Create an object of the user's name
    user = User(username)
    # Load all the user's tasks if they have any
    user.loadTasks()

    while True:
        choice = input("\n1. Add task\n2. Remove task\n3. View tasks\n4. Edit tasks\n5. Toggle completion of tasks\n6. Save and Exit\n")

        if choice == "1":
            task = input("Enter a task: ")
            user.addTask(task)
        elif choice == "2":
            user.viewAllTasks()
            while True:
                try:
                    task_number = int(input("\nEnter the task number to remove: "))
                except ValueError:
                    print("\nEnter a number.\n")
                    continue
                else:
                    user.removeTask(task_number)
                    break
        elif choice == "3":
            if user.tasks:
                user.viewIncompleteTasks()
            else:
                print("No tasks to display.")
        elif choice == "4":
            if user.tasks:
                task_new_edit = input("Enter the new task message: ")
                user.editTasks(task_num_edit, task_new_edit)
            else:
                print("No tasks to display.")
        elif choice == "5":
            if user.tasks:
                task_num_edit = int(input("Enter the number of the task you want to complete: "))
                user.toggleTasks(task_num_edit)
            else:
                print("No tasks to display.")
        elif choice == "6":
            user.saveTasks()
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# In these following loops:
    # for key, value in dictionary.items()
    # The computer iterates through each key and then executes code if the value is also needed.
