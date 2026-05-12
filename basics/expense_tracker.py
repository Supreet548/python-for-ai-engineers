expenses = []

#add expense

def add_expense():
    amount = float(input("Enter amount: "))
    category=input('Enter category: ')


    expense = {
        "amount":amount,
        "category":category
    }

    expenses.append(expense)

    print("Expense added successfully!\n")

#show all expenses
def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    print("\nAll expenses:")

    for expense in expenses:
        print(expense)

    


# Show total expense
def show_total():

    total = 0 

    for expense in expenses:
        total += expense["amount"] 

    print("Total Expense:", total)

    


# Main menu
while True:
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice\n")