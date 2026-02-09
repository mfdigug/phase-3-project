from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem


# intro - Welcome, what would you like to do:

# 1. Add new customer


def get_customer_by_email(session, email):
    customer = session.query(Customer).filter(Customer.email == email).first()
    return customer


def add_customer():
    pass

    # name = input(“Enter user name: ”)
    # if get_customer_by_name(name):
    # print (f“customer already exists”)
    # return
    # else:
    # session.add(customer(name=name)
    # session.commit()
    # print (f“customer {name} added”)

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

    def view_menu_items(session):
        items = session.query(MenuItem).all()
        return items

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
