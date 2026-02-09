from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem


# 1
def get_menu_items(session):
    items = session.query(MenuItem).all()
    return items


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


def create_order():
    pass

    # find_customer_by_id
    # create_order (with customer id)

    # view menu


def delete_order_item(session, item_id):
    item = session.query(OrderItem).get(item_id)
    if not item:
        return False
    session.delete(item)
    session.commit()

    # 2.1.1 Add item mods
    # 2.2 Add item to order
    # 3. Review order and price
    # 3.1 Update existing items
    # 3.2 View total_price
    # 4. Submit order
    # 5. Cafe level => view total amount made on a particular date?
