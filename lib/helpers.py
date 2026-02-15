from db.models import Base, MenuItem, Mod, Customer, OrderItemMod, Order, OrderItem


# 1. CUSTOMER MANAGEMENT
# 1.1 get customer
def get_customer_by_email(session, email):
    customer = session.query(Customer).filter(Customer.email == email).first()
    return customer

# 1.2 new customer


def add_to_customers(session, new_first_name, new_last_name, email):
    new_customer = Customer(
        first_name=new_first_name,
        last_name=new_last_name,
        email=email
    )

    session.add(new_customer)
    session.commit()
    return new_customer

# 1.3 view details


def print_customer_details(customer):
    print(f"""
    ******
    Customer ID {customer.id}
    Name: {customer.first_name} {customer.last_name}
    email {customer.email}
    ******
    """)


# 2 CREATE NEW ORDER
def create_order(session, customer_id):
    new_order = Order(
        customer_id=customer_id,
    )
    session.add(new_order)
    session.commit()
    print(f"""
    ****** 
    Order Number: {new_order.id} has been created.
    ******
    """)


# 3 ADD ITEM TO ORDER
# 3.1 View Menu
def get_menu_items(session):
    items = session.query(MenuItem).all()
    return items
# 3.2 Add item


def add_item(session, order_id, menu_item_id, quantity):
    new_item = OrderItem(
        order_id=order_id,
        menu_item_id=menu_item_id,
        quantity=quantity
    )
    session.add(new_item)
    session.commit()
    print(f"""
    ******
    Item ID: {new_item.id} added to {order_id}.
    ******
    """)


# 4 ADD MOD TO ITEM
# 4.1 view mods
def get_mods(session):
    mods = session.query(Mod).all()
    return mods


# 4.2 add mod
def add_mod(session, item_id, mod_id):
    order_item = session.query(OrderItem).filter(
        OrderItem.id == item_id).first()
    mod = session.query(Mod).filter(Mod.id == mod_id).first()

    if not order_item or not mod:
        print("******\n Item or mod not found. \n******")
        return

    order_item.mods.append(mod)

    session.commit()
    print(f"""
    ******
    {order_item.mods} added to {order_item.menu_item.item}!
    ******
    """)


# 5 FINALISE ORDER
# 5.1 view order
def view_order(session, order_id):
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        print("******\n Order not found. \n******")
        return

    print("*" * 10)
    print(f"""
    Order: {order.id}"
    Customer: {order.customer.first_name}
    """)
    print("*" * 10)

    for item in order.order_items:
        print(f"{item.menu_item.item} ${item.menu_item.price:.2f}")
        for mod in item.mods:
            print(f"""
                + {mod.mod_item} (${mod.mod_price:.2f})"
                ${item.subtotal():.2f}
            """)
    print("*" * 10)
    print(f"Order Total = ${order.order_total():.2f}")
    print("*" * 10)


# 5.2 modify order - delete item
def delete_order_item(session, item_id):
    item = session.query(OrderItem).get(item_id)
    if not item:
        print("******\n Order item not found \n******")
        return

    session.delete(item)
    session.commit()
    print("******\n Item has been deleted. \n******")


# 5.3 Delete order
def delete_order(session, order_id):
    order = session.query(Order).filter(
        Order.id == order_id).first()

    if not order:
        print("******\n Order not found. \n******")
        return

    session.delete(order)
    session.commit()
    print(f"******\n Order number {order_id} deleted. \n******")
