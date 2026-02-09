from db.db_setup import session
from helpers import get_customer_by_email


def run():
    print("☕ CLI Cafe started")

    while True:
        email = input("Enter customer email (or 'quit' to exit): ").strip()

        if email.lower() == "quit":
            print("Ciao")
            break

        customer = get_customer_by_email(session, email)
        if customer:
            print(f"Customer found: {customer.id} {customer.first_name}")
        else:
            print("Customer not found")


if __name__ == "__main__":
    run()


# options
# intro - Welcome, what would you like to do:
# 1. Add new customer
# 2. New order
# find_customer_by_id
# create_order (with customer id)
# 2.1 Add order_items (use flush?)
# 2.1.1 Add item mods
# 2.2 Add items to order
# 3. Review order and price
# 3.1 Update existing items
# 3.2 View total_price
# 4. Submit order
# 5. Cafe level => view total amount made on a particular date?
