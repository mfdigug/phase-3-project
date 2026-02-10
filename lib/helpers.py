from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem


# 1
def get_menu_items(session):
    items = session.query(MenuItem).all()
    return items


# get mods
def get_mods(session):
    mods = session.query(Mod).all()
    return mods

# 2. Find customer


def get_customer_by_email(session, email):
    customer = session.query(Customer).filter(Customer.email == email).first()
    return customer


# 2.1 if not customer - add customer
def add_to_customers(session, new_first_name, new_last_name, new_email):
    new_customer = Customer(
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email
    )

    session.add(new_customer)
    session.commit()

    # check customer's orders
    # customer.orders
    # for orders in customer.orders:
    # print(order.id)

    # print(order.customer.name)

    # 2. New order

    # 2.1 Add order_items (use flush?)


# 3 create order
def create_order(session, customer_id):
    new_order = Order(
        customer_id=customer_id,
    )
    session.add(new_order)
    session.commit()
    print(new_order.id)


def add_item(session, order_id, menu_item_id, quantity):
    new_item = OrderItem(
        order_id=order_id,
        menu_item_id=menu_item_id,
        quantity=quantity
    )
    session.add(new_item)
    session.commit()
    print(f"{new_item.id}")


def add_mod(session, item_id, mod_id):
    order_item = session.query(OrderItem).filter(
        OrderItem.id == item_id).first()
    mod = session.query(Mod).filter(Mod.id == mod_id).first()

    if not order_item or not mod:
        print("item or mod not found")
        return

    order_item.mods.append(mod)
    print(order_item.mods)
    session.commit()
    print("Mod added!")


# def delete_order_item(session, item_id):
#     item = session.query(OrderItem).get(item_id)
#     if not item:
#         return False
#     session.delete(item)
#     session.commit()

    # 2.1.1 Add item mods
    # 2.2 Add item to order
    # 3. Review order and price
    # 3.1 Update existing items
    # 3.2 View total_price
    # 4. Submit order
    # 5. Cafe level => view total amount made on a particular date?
