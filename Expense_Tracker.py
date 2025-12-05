import matplotlib.pyplot as nkp
import numpy as np

def expenditure():
    print('Welcome to the Expenses of NIHAR')
    salary = int(input('Enter Your Salary: '))
    print('--------------------Now enter your EXPENSES---------------------')

    expenses = {
        'Food': int(input('Enter your Food Expenses: ')),
        'Travel': int(input('Enter your Travel Expenses: ')),
        'Rent': int(input('Enter your Rent Expenses: ')),
        'Internet': int(input('Enter your Internet Expenses: ')),
        'Netflix': int(input('Enter your Netflix Expenses: '))
    }

    total_expense = sum(expenses.values())
    print(f'\nYour Total Expense is {total_expense}')

    if total_expense == salary / 2:
        print('Your Expenses are Normal.')
    elif salary - total_expense == 0:
        print('Your Expenses are equal to your Salary.')
    elif salary - total_expense > 0:
        print(f'You are saving {salary - total_expense}.')
    else:
        print(f'You are overspending by {total_expense - salary}!')
    return expenses
expenses = expenditure()
labels = list(expenses.keys())
values = list(expenses.values())
nkp.pie(values, labels=labels)
nkp.title("Nihar's Monthly Expenses")
nkp.show()
