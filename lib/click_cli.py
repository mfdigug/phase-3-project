from db.db_setup import session
from helpers import get_customer_by_email, add_to_customers, get_menu_items, get_mods, create_order, add_item, add_mod, view_order, delete_order, delete_order_item


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
    email = input("Enter customer email (or 'q' to exit): ").strip()
    if email.lower() == "q":
        return
    else:
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
    create_order(session, int(customer_id))
    # flush?


# 5
def new_item():
    order_id = input("Enter order id: ")
    menu_item_id = input("Enter menu item number: ")
    quantity = input("Enter quantity: ")
    print(f"Order Number: {order_id}, Item: {menu_item_id}")
    add_item(session, int(order_id), int(menu_item_id), int(quantity))


# 6
def add_mod_to_item():
    item_id = input("Enter item_id: ")
    while True:
        mod = input("Add modification (or type 'q' to quit): ")
        if mod.lower() == 'q':
            break
        else:
            add_mod(session, int(item_id), int(mod))


# 7 Finalise/update order
def update_order(session):
    while True:
        print("a. Add item")
        print("b. Delete item")
        choice = input("Select an action (or 'q' to exit): ")
        if choice.lower() == "q":
            break
        elif choice.lower() == "a":
            new_item()
        elif choice.lower() == "b":
            item_id = input("Which item would you like to delete? ")
            delete_order_item(session, int(item_id))


def finalise_order():
    order_id = input("Enter order number: ")
    view_order(session, int(order_id))
    while True:
        print("1. Confirm order")
        print("2. Modify order")
        print("3. Delete order")

        option = input(
            "Please select a number (or 'q' to exit): ")

        if option.lower() == "q":
            return
        elif option == "1":
            print(f"Order {order_id} confirmed")
            return
        elif option == "2":
            update_order(session)
        elif option == "3":
            delete_order(session, int(order_id))


# CLI Menu
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
        print("7. Finalise order")
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
            finalise_order()
        elif choice == "8":
            print("Ciao!")
            break
        else:
            print("Invalid choice. Please view the menu and select an option")
