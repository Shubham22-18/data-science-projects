import json
import os

FILE_NAME = "expenses.json"

# Load existing expenses
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses()

        print("Expense added successfully!")

    elif choice == "2":
        if expenses:
            print("\n--- Expense Records ---")

            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. Category: {expense['category']} | Amount: ₹{expense['amount']}")

        else:
            print("No expenses found.")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"\nTotal Expenses: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Please try again.")
