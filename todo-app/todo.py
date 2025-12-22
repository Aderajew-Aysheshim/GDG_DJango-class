import json
import os
from typing import List
JSON_FILE = "todos.json"
class Task:
  
    
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed
    
    def to_dict(self) -> dict:
        """Convert Task object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Create a Task object from dictionary (deserialization)."""
        return cls(data["id"], data["title"], data["completed"])
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.id}: {self.title}"


class TodoManager:
    """Manages the collection of tasks and persistence."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file on startup."""
        if not os.path.exists(JSON_FILE):
            self.tasks = []
            self.next_id = 1
            return
        
        try:
            with open(JSON_FILE, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                if self.tasks:
                    self.next_id = max(task.id for task in self.tasks) + 1
                else:
                    self.next_id = 1
        except (json.JSONDecodeError, FileNotFoundError):
            print("Warning: Could not load tasks. Starting with empty list.")
            self.tasks = []
            self.next_id = 1
    
    def save_tasks(self):
        """Save all tasks to JSON file."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks]
        }
        try:
            with open(JSON_FILE, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, title: str):
        """Add a new task."""
        if not title.strip():
            print("Task title cannot be empty!")
            return
        task = Task(self.next_id, title.strip())
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Added: {task}")
    
    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks yet! Add one using 'add'.")
            return
        
        print("\nYour Todo List:")
        print("-" * 40)
        for task in self.tasks:
            print(task)
        print("-" * 40)
    
    def find_task_by_id(self, task_id: int) -> Task:
        """Find task by ID or return None."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, new_title: str = None, completed: bool = None):
        """Update task title or completion status."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found!")
            return
        
        if new_title is not None:
            if not new_title.strip():
                print("Title cannot be empty!")
                return
            task.title = new_title.strip()
        
        if completed is not None:
            task.completed = completed
        
        self.save_tasks()
        print(f"Updated: {task}")
    
    def delete_task(self, task_id: int):
        """Delete a task by ID."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found!")
            return
        
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
        print(f"Deleted task {task_id}: {task.title}")

def main():
    manager = TodoManager()
    print("Welcome to OOP Todo App!")
    
    while True:
        print("\nCommands: add, view, update, toggle, delete, quit")
        command = input("> ").strip().lower()
        
        if command == "add":
            title = input("Enter task title: ").strip()
            manager.add_task(title)
        
        elif command == "view":
            manager.view_tasks()
        
        elif command == "update":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title (or press Enter to skip): ").strip()
                manager.update_task(task_id, new_title if new_title else None)
            except ValueError:
                print("Invalid ID!")
        
        elif command == "toggle":
            try:
                task_id = int(input("Enter task ID to toggle completion: "))
                task = manager.find_task_by_id(task_id)
                if task:
                    manager.update_task(task_id, completed=not task.completed)
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid ID!")
        
        elif command == "delete":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid ID!")
        
        elif command in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        
        else:
            print("Unknown command. Try: add, view, update, toggle, delete, quit")


if __name__ == "__main__":
    main()