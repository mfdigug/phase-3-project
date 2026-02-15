from db.db_setup import session
from helpers import get_customer_by_email, add_to_customers, get_menu_items, get_mods, create_order, add_item, add_mod, view_order, delete_order, delete_order_item, print_customer_details


# 1. CUSTOMER MANAGEMENT
# 1.1 find customer
def find_customer():
    email = input("Enter customer email (or 'q' to exit): ").strip()
    if email.lower() == "q":
        return
    else:
        customer = get_customer_by_email(session, email)
        if customer:
            print_customer_details(customer)
        else:
            print("Customer not found")
            add_customer = input("Would you like to add a customer? Y/N: ")
            if add_customer.lower() == "y":
                new_customer = create_new_customer(email)
                print_customer_details(new_customer)


# 1.2 new customer
def create_new_customer(email):
    new_first_name = input("Enter customer's first name: ")
    new_last_name = input("Enter customer's last name: ")
    new_email = email
    new_customer = add_to_customers(
        session, new_first_name, new_last_name, new_email)
    return (new_customer)


# 2. NEW ORDER
def new_order():
    customer_id = input("Enter customer id: ")
    order = create_order(session, int(customer_id))
    return order


# 3. ADD ITEM
# 3.1 view items
def view_menu_items():
    menu_items = get_menu_items(session)
    for item in menu_items:
        print(f"{item.id}. {item.item} ${item.price}")


# 3.2 add item
def new_item():

    order_id = input("To add an item, enter the order number: ")
    if not order_id:
        order = new_order(session)
        order_id = order.id
    else:
        order_id = int(order_id)

    menu_item_id = input(
        "Enter the menu item number to add it to your order: ")
    if not menu_item_id:
        print("There is no item with that id")
        return
    else:
        menu_item_id = int(menu_item_id)

    quantity = input(f"How many would you like?")
    if not quantity.isdigit():
        print("quantity must be a number")
        return

    print(
        f"Item added to order Number: {order_id}, Item ID: {menu_item_id}, Quantity added: {quantity}")
    add_item(session, int(order_id), int(menu_item_id), int(quantity))


# 4. ADD MOD TO ITEM
# 4.1 view mods
def view_mods():
    mods = get_mods(session)
    for mod in mods:
        print(f"{mod.id}. {mod.mod_item}, + ${mod.mod_price}")


# 4.2 add mod
def add_mod_to_item():
    item_id = input(
        "Enter the item ID for the item you would like to modify: ")
    while True:
        mod = input("Add modification (or type 'q' to quit): ")
        if mod.lower() == 'q':
            break
        else:
            add_mod(session, int(item_id), int(mod))


# 5. FINALISE ORDER
# 5.1 view order and make choice:
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


# 5.2 update order
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


# CLI Menu
if __name__ == "__main__":
    print("☕ Welcome to the CLI Café")

    while True:
        print("Please select an option:")
        print("1. Find customer")
        print("2. Create new order")
        print("3. Add item")
        print("4. Add mod to item")
        print("5. Finalise order")
        print("6. Exit")

        choice = input("What would you like to do? Select a number: ")

        if choice == "1":
            find_customer()
        elif choice == "2":
            new_order()
        elif choice == "3":
            view_menu_items()
            new_item()
        elif choice == "4":
            view_mods()
            add_mod_to_item()
        elif choice == "5":
            finalise_order()
        elif choice == "6":
            print("Ciao!")
            break
        else:
            print("Invalid choice. Please view the menu and select an option")
