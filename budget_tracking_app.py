import json
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(transactions):
    with open(DATA_FILE, "w")as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transactions, type_):
    description = input("\nEnter description (Salry/Food): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    transaction = {
        "type": type_,
        "description": description,
        "amount": amount,
        "date": date
    }

    transactions.append(transaction)
    print(f"\n{type_.capitalize()} added successfully!\n")
    save_data(transactions)


def view_transactions(transactions):
    if not transactions:
        print("\nNo transactions found.\n")
        return
    
    for i, t in enumerate(transactions):
        print(f"{i}. {t['date']} - {t['type'].capitalize()}: {t['description']} - GHS{t['amount']}")
    print()

def show_summary(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] =="expense")
    balance = income - expense

    print()
    print(f"Total Income: GHS{income}")
    print(f"Total Expenses: GHS{expense}")
    print(f"Balance: GHS{balance}\n")

def delete_transaction(transactions):
    view_transactions(transactions)
    if not transactions:
        return
    
    try:
        index = int(input("Enter the number of the transaction to deleted: "))
        if 0 <= index < len(transactions):
            deleted = transactions.pop(index)
            print(f"Deleted: {deleted['description']} - GHS{deleted['amount']}\n")
        else:
            print("Invalid transaction number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    save_data(transactions)

def main():
    print("___ Welcome to the ULTIMATe Budget Tracking App ___\n")
    transactions = load_data()

    while True:
        print("   -- Menu --")
        print("1. Add Income\n2. Add Expense\n3. View Transactions\n4. Delete Transaction\n5. View Summary\n6. Save & Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            show_summary(transactions)
        elif choice == "6":
            save_data(transactions)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    main()