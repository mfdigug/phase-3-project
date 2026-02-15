import click
from db.db_setup import session
from helpers import get_customer_by_email, add_to_customers, get_menu_items, get_mods, create_order, add_item, add_mod, view_order, delete_order, delete_order_item, print_customer_details


# 1. CUSTOMER MANAGEMENT
# 1.1 find customer
@click.command()
@click.option('--email', prompt="Enter customer email (or 'q' to exit)", help="Customer email")
def find_customer(email):
    if email.lower() == "q":
        return
    customer = get_customer_by_email(session, email)
    if customer:
        click.echo("\nCustomer found:\n")
        print_customer_details(customer)
    else:
        print("Customer not found")
        if click.confirm("Would you like to add a customer?"):
            new_customer = create_new_customer(email)
            


# 1.2 new customer
def create_new_customer(email):
    new_first_name = click.prompt("Enter customer's first name")
    new_last_name = click.prompt("Enter customer's last name")

    new_customer = add_to_customers(
        session, new_first_name, new_last_name, email)
    click.echo("\nCustomer successfully created:\n")
    print_customer_details(new_customer)
    
    return new_customer


# 2. NEW ORDER
def new_order():
    customer_id = input("Enter customer id: ")
    order = create_order(session, int(customer_id))
    return order


# 3. ADD ITEM

# 3.1 add item
@click.command()
@click.option("--order-id", prompt="To add an item, enter the order number (leave blank to create new)", default="", show_default=False)
def new_item(order_id):
    if not order_id:
        order = new_order()
        order_id = order.id
    else:
        if not order_id.isdigit():
            click.echo("Order number must be numeric")
            return
        order_id = int(order_id)
    
    add_more_items = True
    while add_more_items:

        menu_items = get_menu_items(session)
        valid_ids = [item.id for item in menu_items]
        while True:
            menu_item_id = click.prompt("Enter the menu item number to add", type=int)
            if menu_item_id in valid_ids:
                break
            click.echo("There is no menu item with that id")

        quantity = click.prompt(f"How many would you like?", type=int)

        new_order_item = add_item(session, order_id, menu_item_id, quantity)

        item_id = new_order_item.id

        while click.confirm("Would you like to modify this item?"):
            view_mods()
            mod_id = click.prompt("Enter mod ID to add", type=int)
            add_mod(session, item_id, mod_id)

        choice = click.prompt("Do you want to: (a) add another item, or (b) finalise order?", type=click.Choice(['a', 'b'], case_sensitive=False))
        if choice == 'b':
            finalise_order(session, order_id)
            add_more_items = False


# 3.2 view items
def view_menu_items():
    menu_items = get_menu_items(session)
    for item in menu_items:
        click.echo(f"{item.id}. {item.item} ${item.price}")

# 3.3 view mods
def view_mods():
    mods = get_mods(session)
    for mod in mods:
        print(f"{mod.id}. {mod.mod_item}, + ${mod.mod_price}")

            

# 5. FINALISE ORDER
# 5.1 view order and make choice:
def finalise_order(session, order_id):
    order_id = input("Enter order number: ")
    view_order(session, order_id)
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
