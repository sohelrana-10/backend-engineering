
import json
from pathlib import Path


class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            completed=data.get("completed", False)
        )


class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = Path(filename)
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not self.filename.exists():
            self.tasks = []
            return

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)

            self.tasks = [Task.from_dict(item) for item in data]

        except (json.JSONDecodeError, OSError, TypeError, KeyError, ValueError):
            print("Warning: Could not load tasks. Starting with an empty list.")
            self.tasks = []

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_task(self, title):
        title = title.strip()

        if not title:
            print("Task title cannot be empty.")
            return

        task_id = max(
            (task.task_id for task in self.tasks),
            default=0
        ) + 1

        task = Task(task_id, title)
        self.tasks.append(task)
        self.save_tasks()

        print(f"Task {task_id} added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n--- YOUR TASKS ---")

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.task_id}. [{status}] {task.title}")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        return None

    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print("Task not found.")
            return

        if task.completed:
            print("This task is already completed.")
            return

        task.mark_completed()
        self.save_tasks()
        print(f"Task {task_id} marked as completed!")

    def delete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print("Task not found.")
            return

        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task {task_id} deleted successfully!")
