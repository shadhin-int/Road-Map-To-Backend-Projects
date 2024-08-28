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


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Add Task
    parser_add = subparsers.add_parser('add', help="Add a new task")
    parser_add.add_argument('description', type=str, help='Task Description')


    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    



if __name__ == '__main__':
    main()
