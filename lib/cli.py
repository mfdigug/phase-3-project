import click
from db.db_setup import session
from helpers import get_customer_by_email, add_to_customers, get_menu_items, get_mods, create_order, add_item, add_mod, view_order, delete_order, delete_order_item, print_customer_details, check_for_order


# 1. CUSTOMER MANAGEMENT
# 1.1 find customer
def find_customer(session, email):
    customer = get_customer_by_email(session, email)
    if customer:
        click.echo("\nCustomer found:\n")
        print_customer_details(customer)
    else:
        click.echo("Customer not found")
        if click.confirm("Would you like to add a customer?"):
            new_customer = create_new_customer(session, email)
            return new_customer
    return customer


# 1.2 new customer
def create_new_customer(session, email):
    new_first_name = click.prompt("Enter customer's first name")
    new_last_name = click.prompt("Enter customer's last name")

    new_customer = add_to_customers(
        session, new_first_name, new_last_name, email)
    click.echo("\nCustomer successfully created:\n")
    print_customer_details(new_customer)

    return new_customer


# 2. NEW ORDER
def new_order(session):
    customer_id = click.prompt("Enter customer id", type=int)
    order = create_order(session, customer_id)
    return order


# 3. ADD ITEM
def new_item(session, order_id):
    # 3.1 check if order number exists
    if order_id:
        order = check_for_order(session, order_id)
        if not order:
            return
    elif not order_id:
        order = new_order(session)
        order_id = order.id
    else:
        if not order_id.isdigit():
            click.echo("Order number must be numeric")
            return
        order_id = int(order_id)

    # 3.2 view menu
    view_menu_items()

    # loop add items
    add_more_items = True
    while add_more_items:
        menu_items = get_menu_items(session)
        valid_ids = [item.id for item in menu_items]
        while True:
            menu_item_id = click.prompt(
                "Enter the menu item number to add", type=int)
            if menu_item_id in valid_ids:
                break
            click.echo("There is no menu item with that id")
        quantity = click.prompt(f"How many would you like?", type=int)
        # commit item and assign id
        new_order_item = add_item(session, order_id, menu_item_id, quantity)
        item_id = new_order_item.id
        # add mods
        while click.confirm("Would you like to modify this item?"):
            # 3.3 view mods
            view_mods()
            # 3.4 add mods
            mod_id = click.prompt("Enter mod ID to add", type=int)
            add_mod(session, item_id, mod_id)
        # loop
        choice = click.prompt(
            "Do you want to: (a) add another item, or (b) finalise order?",
            type=click.Choice(['a', 'b'], case_sensitive=False))
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
        click.echo(f"{mod.id}. {mod.mod_item}, + ${mod.mod_price}")


# 5. FINALISE ORDER
# 5.1 view order and make choice - can be called by add_items(), from menu or top level cli
def finalise_order(session, order_id=None):
    if order_id is None:
        order_id = click.prompt("Enter order number", type=int)

    view_order(session, order_id)
    while True:
        print("1. Confirm order")
        print("2. Modify order")
        print("3. Delete order")

        choice = click.prompt(
            "Please select a number (or 'q' to exit)", type=click.Choice(['q', '1', '2', '3'], case_sensitive=False)
        )

        if choice == "q":
            return
        elif choice == "1":
            print(f"Order {order_id} confirmed")
            return
        elif choice == "2":
            update_order(session)
        elif choice == "3":
            delete_order(session, order_id)
        else:
            print("Invalid choice. Please try again")


# 5.2 update order
def update_order(session):
    while True:
        print("1. Add item")
        print("2. Delete item")
        choice = click.prompt(
            "Please select an option (or 'q' to exit)", type=click.Choice(['q', '1', '2']), case_sensitive=False
        )
        if choice == "q":
            break
        elif choice == "1":
            new_item()
        elif choice == "2":
            item_id = click.prompt(
                "Which item would you like to delete?", type=int)
            delete_order_item(session, item_id)


# main menu entry point
def main_menu(session):
    print("☕ Welcome to the CLI Café")

    while True:
        print("Please select an option:")
        print("1. Find customer")
        print("2. Create new order")
        print("3. Add item")
        print("4. Finalise order")
        print("5. Exit")

        choice = click.prompt("What would you like to do? Select a number",
                              type=click.Choice(['1', '2', '3', '4', '5']))

        if choice == "1":
            email = click.prompt("Enter customer email(or 'q' to quit)")
            if email.lower() == 'q':
                continue
            find_customer(session, email)
        elif choice == "2":
            new_order(session)
        elif choice == "3":
            order_id = click.prompt(
                "Enter the order id or leave blank to create new order")
            new_item(session, order_id)
        elif choice == "4":
            finalise_order(session, None)
        elif choice == "5":
            print("Ciao!")
            break
        else:
            print("Invalid choice. Please view the menu and select an option")


# click commands run through terminal
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["session"] = session

    if ctx.invoked_subcommand is None:
        main_menu(ctx.obj["session"])


# main menu
@click.command(name="main-menu")
@click.pass_context
def main_menu_cli(ctx):
    """
    Launch menu
    """
    main_menu(ctx.obj["session"])


# find customer
@click.command(name="find-customer")
@click.option('--email', prompt="Enter customer email (or 'q' to exit)", help="Customer email")
@click.pass_context
def find_customer_cli(ctx, email):
    """
    Find a customer by searching their email
    """
    session = ctx.obj["session"]
    if email.lower() == "q":
        return
    find_customer(session, email)


# create new order:
@click.command(name="new-order")
@click.option("--customer-id", prompt="Create a new order with a customer id", default="", show_default=False)
@click.pass_context
def new_order_cli(ctx, customer_id):
    """
    Create a new order with a customer id.
    """
    session = ctx.obj["session"]
    new_order(session, customer_id)


# add item to order:
@click.command(name="add-item")
@click.option("--order-id", prompt="To add an item, enter the order number (leave blank to create new)", default="", show_default=False)
@click.pass_context
def new_item_cli(ctx, order_id):
    """
    Add an item by passing --order-id followed by the order id number, or via prompt.
    """
    session = ctx.obj["session"]
    new_item(session, order_id)


# finalise order
@click.command(name="finalise-order")
@click.option("--order-id", type=int, default=None, help="Order number to finalise. Leave empty to be prompted")
@click.pass_context
def finalise_order_cli(ctx, order_id):
    """
    Finalise an order by passing --order-id followed by the order id number, or via prompt.
    """
    session = ctx.obj["session"]
    finalise_order(session, order_id)


# add wrapper functions
cli.add_command(main_menu_cli)
cli.add_command(find_customer_cli)
cli.add_command(new_order_cli)
cli.add_command(new_item_cli)
cli.add_command(finalise_order_cli)

# CLI Menu through $python cli.py
if __name__ == "__main__":
    cli()
