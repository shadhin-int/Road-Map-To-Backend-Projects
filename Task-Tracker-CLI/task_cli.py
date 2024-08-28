import argparse
import json
import os
from datetime import datetime

FILE_PATH = 'tasks.json'


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    
    if os.path.getsize(FILE_PATH) == 0:
        return []

    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1

    new_task ={
        'id': task_id,
        'description': description,
        'status': 'todo',
        'created_at': get_current_time(),
        'updated_at': get_current_time()
    }

    tasks.append(new_task)
    print(tasks)
    save_tasks(tasks)
    print(f"New task {task_id} created successfully")

def list_tasks(filter_by=None):
    tasks = load_tasks()
    if filter_by:
        tasks = [task for task in tasks if task['status'] == filter_by]
    
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['created_at']}, Updated: {task['updated_at']})")



def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Add Task
    parser_add = subparsers.add_parser('add', help="Add a new task")
    parser_add.add_argument('description', type=str, help='Task Description')

    # List Tasks
    parser_list = subparsers.add_parser('list', help='List of Tasks')
    parser_list.add_argument('filter', type=str, nargs='?', default=None, choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')


    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks(args.filter)
    


if __name__ == '__main__':
    main()
