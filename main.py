import json
import os
from datetime import datetime

class TaskTracker:
    def __init__(self):
        self.tasks = []
        self.data_file = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nTask List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']} - Due: {task['due_date']} - Status: {task['status']}")
        print()

    def add_task(self, title, description, due_date):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "To-Do"
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def update_task_status(self, task_index, new_status):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["status"] = new_status
            self.save_tasks()
            print(f"Task status updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{deleted_task['title']}' deleted successfully.")
        else:
            print("Invalid task index.")

# Example Usage:
task_tracker = TaskTracker()

while True:
    print("\nTask Tracker Menu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task_tracker.display_tasks()
    elif choice == '2':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        task_tracker.add_task(title, description, due_date)
    elif choice == '3':
        task_tracker.display_tasks()
        task_index = int(input("Enter task index to update status: "))
        new_status = input("Enter new status: ")
        task_tracker.update_task_status(task_index, new_status)
    elif choice == '4':
        task_tracker.display_tasks()
        task_index = int(input("Enter task index to delete: "))
        task_tracker.delete_task(task_index)
    elif choice == '5':
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
