import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully ID: {task_id}')

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description']  = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully.')
            return
    print(f'Task {task_id} not found.')

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully.')

def mark_task(task_id, status):
    valid_statuses = ['in-progress', 'done']
    if status not in valid_statuses:
        print(f"Invalid status. Use 'in-progress' or 'done'.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatdAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}.')
            return
    print(f'Task {task_id} not found.')


def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]

        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
        for task in filtered_tasks:
            print(f"[{task['status']}] ID: {task['id']} - {task['description']} (Created: {task['createdAt']})")

    else:

        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(f"[{task['status']}] ID: {task['id']} - {task['description']} (Created: {task['createdAt']})")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [command] [args]")
        return

    command = sys.argv[1]

    if command == 'add':
        description = ' '.join(sys.argv[2:])
        add_task(description)

    elif command == 'update':
        try:
            task_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
            update_task(task_id, new_description)
        except ValueError:
            print("Invalid ID.")

    elif command == 'delete':
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Invalid ID.")

    elif command == 'mark-in-progress':
        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, 'in-progress')
        except ValueError:
            print("Invalid ID.")

    elif command == 'mark-done':
        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, 'done')
        except ValueError:
            print("Invalid ID.")

    elif command == 'list':
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print("Unknown command.")

if __name__ == '__main__':
    main()

