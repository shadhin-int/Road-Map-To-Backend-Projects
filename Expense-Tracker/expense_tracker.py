import argparse
import json
import os
from datetime import datetime

FILE_PATH = 'expenses.json'

def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    
    if os.path.getsize(FILE_PATH) == 0:
        return []
    
    with open(FILE_PATH, 'r') as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_PATH, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    new_expense = {
        'id' : expense_id,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': float(amount)
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")


def list_expenses():
    expenses = load_expenses()
    print("ID  Date       Description  Amount")
    for expense in expenses:
        print(f"{expense['id']}   {expense['date']} {expense['description']}        ${expense['amount']:.2f}")


def update_expense(id, description, amount):
    expenses = load_expenses()

    for expense in expenses:
        if expenses['id'] == id:
            expense['description'] = description
            expense['amount'] = float(amount)
            save_expenses(expense)
            print(f"Expense {id} updated successfully")
            return
            
    print(f"Expense with ID {id} not found")



def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest='command')


    # Add expense
    parser_add = subparsers.add_parser('add', help="Add a new Expense")
    parser_add.add_argument('--description', type=str, required=True, help='Expense Description')
    parser_add.add_argument('--amount', type=int, required=True, help='Expense Amount')


    # List of Expense
    parser_list = subparsers.add_parser('list', help='List all expenses')


    # Update Expense
    parser_update = subparsers.add_parser('update', help='Update an expense')
    parser_update.add_argument('--id', type=int, required=True, help='Expense ID')
    parser_update.add_argument('--description', type=str, required=True, help='New expense description')
    parser_update.add_argument('--amount', type=float, required=True, help='New expense amount')


    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.description, args.amount)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'update':
        update_expense()


if __name__ == "__main__":
    main()
