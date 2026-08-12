"""
To-Do List Manager
-------------------
"""

import json
import os
from datetime import datetime

DATA_FILE = "todo_data.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if not desc:
        print("Task cannot be empty.")
        return
    tasks.append({
        "description": desc,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['description']}  (added {t['created']})")


def mark_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Removed: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    menu = """
=== TO-DO LIST MANAGER ===
1. Add task
2. List tasks
3. Mark task as done
4. Remove task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()