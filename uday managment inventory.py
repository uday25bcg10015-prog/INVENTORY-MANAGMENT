#  ANSI COLORS
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

inventory = {}

def add_item():
    item_id = input("Enter ITEM ID: ")
    name = input("Enter ITEM NAME: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    inventory[item_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    print(GREEN + "Item added successfully!\n" + RESET)


def update_item():
    item_id = input("Enter item ID to update: ")

    if item_id in inventory:
        print("1. Update name")
        print("2. Update quantity")
        print("3. Update price")
        choice = input("Choose option: ")

        if choice == "1":
            inventory[item_id]["name"] = input("Enter new name: ")
        elif choice == "2":
            inventory[item_id]["quantity"] = int(input("Enter new quantity: "))
        elif choice == "3":
            inventory[item_id]["price"] = float(input("Enter new price: "))
        else:
            print(RED + "Invalid choice" + RESET)

        print(GREEN + "Item updated successfully!\n" + RESET)
    else:
        print(RED + "Item not found!\n" + RESET)


def remove_item():
    item_id = input("Enter item ID to remove: ")
    if item_id in inventory:
        del inventory[item_id]
        print(GREEN + "Item removed!\n" + RESET)
    else:
        print(RED + "Item not found!\n" + RESET)


def search_item():
    item_id = input("Enter item ID to search: ")
    if item_id in inventory:
        print(YELLOW + "Item Found:" + RESET)
        print(f"Name: {inventory[item_id]['name']}")
        print(f"Quantity: {inventory[item_id]['quantity']}")
        print(f"Price: ₹{inventory[item_id]['price']}\n")
    else:
        print(RED + "Item not found!\n" + RESET)


# ⭐ COLORFUL TABLE DISPLAY ⭐
def display_inventory():
    if not inventory:
        print(RED + "Inventory is empty.\n" + RESET)
        return

    print(CYAN + "-" * 72 + RESET)
    print(
        CYAN + "|" + RESET +
        YELLOW + f" {'ID':<8}" + RESET + CYAN + "|" + RESET +
        YELLOW + f" {'Name':<18}" + RESET + CYAN + "|" + RESET +
        YELLOW + f" {'Quantity':<10}" + RESET + CYAN + "|" + RESET +
        YELLOW + f" {'Price (₹)':<12}" + RESET + CYAN + "|" + RESET
    )
    print(CYAN + "-" * 72 + RESET)

    for item_id, details in inventory.items():
        print(
            CYAN + "|" + RESET +
            GREEN + f" {item_id:<8}" + RESET + CYAN + "|" + RESET +
            MAGENTA + f" {details['name']:<18}" + RESET + CYAN + "|" + RESET +
            BLUE + f" {details['quantity']:<10}" + RESET + CYAN + "|" + RESET +
            RED + f" {details['price']:<12}" + RESET + CYAN + "|" + RESET
        )

    print(CYAN + "-" * 72 + RESET + "\n")


def main():
    while True:
        print(YELLOW + "---- INVENTORY MENU ----" + RESET)
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Search Item")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            search_item()
        elif choice == '5':
            display_inventory()
        elif choice == '6':
            print(GREEN + "Exiting... Thank you!" + RESET)
            break
        else:
            print(RED + "Invalid choice! Try again.\n" + RESET)


main()
