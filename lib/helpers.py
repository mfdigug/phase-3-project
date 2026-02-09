from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem, session

# intro - Welcome, what would you like to do:

# 1. Add new customer


def get_customer_by_email(email):
    customer = Customer.query.filter(Customer.email == email)
    print(customer.name)


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
    # find_customer_by_id
    # create_order (with customer id)

    # view menu
    # 2.1 Add order_items (use flush?)
    # 2.1.1 Add item mods
    # 2.2 Add item to order
    # 3. Review order and price
    # 3.1 Update existing items
    # 3.2 View total_price
    # 4. Submit order
    # 5. Cafe level => view total amount made on a particular date?
