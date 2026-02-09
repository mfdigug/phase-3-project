from db.db_setup import session
from helpers import get_customer_by_email, get_menu_items, add_to_customers, create_order, add_item, add_mod, get_mods


# 1
def view_menu_items():
    menu_items = get_menu_items(session)
    for item in menu_items:
        print(f"{item.id}. {item.item} ${item.price}")


# 2
def view_mods():
    mods = get_mods(session)
    for mod in mods:
        print(f"{mod.id}. {mod.mod_item}, + ${mod.mod_price}")

# 3
def find_customer():
    email = input("Enter customer email (or 'quit' to exit): ").strip()
    customer = get_customer_by_email(session, email)
    if customer:
        print(f"Customer found: {customer.id} {customer.first_name}")
    else:
        print("Customer not found")
        add_customer = input("Would you like to add a customer? Y/N: ")
        if add_customer.lower() == "y":
            create_new_customer(email)


# 3.1
def create_new_customer(email):
    new_first_name = input("Enter customer's first name: ")
    new_last_name = input("Enter customer's last name: ")
    new_email = email
    add_to_customers(session, new_first_name, new_last_name, new_email)


# 4
def new_order():
    customer_id = input("Enter customer id: ")
    create_order(session, customer_id)
    # flush?


# 5
def new_item():
    order_id = input("Enter order id: ")
    menu_item_id = input("Enter menu item number: ")
    quantity = input("Enter quantity: ")
    print(f"Order Number: {order_id}, Item: {menu_item_id}")
    add_item(session, order_id, menu_item_id, quantity)

# 6
def add_mod_to_item():
    item_id = input("Enter item_id: ")
    while True:
        mod = input("Add modification (or type 'q' to quit): ")
        if mod.lower() == 'q':
            break
        else:
            add_mod(session, item_id, mod)


if __name__ == "__main__":
    print("☕ CLI Cafe started")

    while True:
        print("Options:")
        print("1. View menu")
        print("2. View mods")
        print("3. Find customer")
        print("4. New Order")
        print("5. Add Item")
        print("6. Add mod to item")
        print("8. Exit")

        choice = input("What would you like to do? Select a number: ")

        if choice == "1":
            view_menu_items()
        elif choice == "2":
            view_mods()
        elif choice == "3":
            find_customer()
        elif choice == "4":
            new_order()
        elif choice == "5":
            new_item()
        elif choice == "6":
            add_mod_to_item()
        elif choice == "7":
            print("Ciao!")
            break
        else:
            print("Invalid choice. Please view the menu and select an option")


# options
# intro - Welcome, what would you like to do:
# 1. Add new customer
# 2. New order
# find_customer_by_id
# create_order (with customer id)
# 2.1 Add order_items (use flush?)
# 2.1.1 Add item mods
# 2.2 Add items to order
# 3. Review order and price
# 3.1 Update existing items
# 3.2 View total_price
# 4. Submit order
# 5. Cafe level => view total amount made on a particular date?
