from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem


# 1 View Menu
def get_menu_items(session):
    items = session.query(MenuItem).all()
    return items


# 2 View Mods
def get_mods(session):
    mods = session.query(Mod).all()
    return mods


# 3. Find/Add customer
def get_customer_by_email(session, email):
    customer = session.query(Customer).filter(Customer.email == email).first()
    return customer


# 3.1 if not customer - add customer
def add_to_customers(session, new_first_name, new_last_name, new_email):
    new_customer = Customer(
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email
    )

    session.add(new_customer)
    session.commit()
    print("Customer has been added!")

    # check customer's orders
    # customer.orders
    # for orders in customer.orders:
    # print(order.id)
    # print(order.customer.name)


# 4 New Order
def create_order(session, customer_id):
    new_order = Order(
        customer_id=customer_id,
    )
    session.add(new_order)
    session.commit()
    print(f"Order Number: {new_order.id} has been created")


# 5 Add Order Item to Order
def add_item(session, order_id, menu_item_id, quantity):
    new_item = OrderItem(
        order_id=order_id,
        menu_item_id=menu_item_id,
        quantity=quantity
    )
    session.add(new_item)
    session.commit()
    print(f"{new_item.id}")


# 6 Add mod to item
def add_mod(session, item_id, mod_id):
    order_item = session.query(OrderItem).filter(
        OrderItem.id == item_id).first()
    mod = session.query(Mod).filter(Mod.id == mod_id).first()

    if not order_item or not mod:
        print("item or mod not found")
        return

    order_item.mods.append(mod)
    session.commit()
    print(f"{order_item.mods} added to {order_item.menu_item.item}!")


# 7 Finalise order = view/update/confirm
def view_order(session, order_id):
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        print("Order not found")
        return

    print("\n")
    print("*" * 10)
    print(f"Order: {order.id}")
    print(f"Customer: {order.customer.first_name}")
    print("*" * 10)

    for item in order.order_items:
        print(f"{item.menu_item.item} ${item.menu_item.price:.2f}")
        for mod in item.mods:
            print(f" + {mod.mod_item} (${mod.mod_price:.2f})")
        print(f"${item.subtotal()}\n")

    print("*" * 10)
    print(f"${order.order_total()}")
    print("*" * 10)


# 7.1 modify order
def delete_order_item(session, item_id):
    item = session.query(OrderItem).get(item_id)
    if not item:
        print("Order item not found")
        return

    session.delete(item)
    session.commit()
    print("Order item has been deleted.")


# 7.2 Delete order
def delete_order(session, order_id):
    order = session.query(order_id).filter(
        Order.id == order_id).first()

    if not order:
        print("Order not found")
        return

    session.delete(order)
    session.commit()
    print(f"Order number {order_id} deleted")
