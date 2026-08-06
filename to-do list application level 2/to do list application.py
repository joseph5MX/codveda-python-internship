import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['description']}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            raise IndexError
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}")
    except (ValueError, IndexError):
        print("Error: That task doesn't exist.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if index < 0 or index >= len(tasks):
            raise IndexError
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked done: {tasks[index]['description']}")
    except (ValueError, IndexError):
        print("Error: That task doesn't exist.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()