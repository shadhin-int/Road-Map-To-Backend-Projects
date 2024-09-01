# Expense Tracker CLI


## Introduction
Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

## Requirements

Application should run from the command line and should have the following features:

-   Users can add an expense with a description and amount.
-   Users can update an expense.
-   Users can delete an expense.
-   Users can view all expenses.
-   Users can view a summary of all expenses.
-   Users can view a summary of expenses for a specific month (of current year).



### The list of commands and their expected output is shown below:

```bash
$ python expense_tracker.py  add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ python expense_tracker.py  add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ python expense_tracker.py  list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ python expense_tracker.py  summary
# Total expenses: $30

$ python expense_tracker.py  delete --id 1
# Expense deleted successfully

$ python expense_tracker.py  summary
# Total expenses: $20

$ python expense_tracker.py  summary --month 8
# Total expenses for August: $20
```