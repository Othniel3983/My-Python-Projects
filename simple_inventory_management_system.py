import json
import os

INVENTORY_FILE = "inventory.json"

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    return{}

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)



def display_menu():
    print("\n INVENTORY MANAGEMENT SYSTEM")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Exit")


def view_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nCurrent Inventory")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

def add_item(inventory):
    item = input("\nEnter item name: ").strip().lower()
    if item in inventory:
        print("Item already exists. use update option to change it's quantity")
    else:
        try:
            quantity = int(input("Enter quantity: "))
            inventory[item] = quantity
            print(f"{item} added with quantity {quantity}")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

def update_quantity(inventory):
    item = input("\nEnter the item name to update: ").strip().lower()
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            inventory[item] = quantity
            print(f"{item} updated to quantity {quantity}.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not found in inventory.")

def delete_item(inventory):
    item = input("\nEnter item name to delete: ")
    if item in inventory:
        del inventory[item]
        print(f"{item} deleted from inventory")
    else:
        print("Item not found in inventory.")

def main():
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip().lower()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
            save_inventory(inventory)
        elif choice == "3":
            update_quantity(inventory)
            save_inventory(inventory)
        elif choice == "4":
            delete_item(inventory)
            save_inventory(inventory)
        elif choice == "5":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()