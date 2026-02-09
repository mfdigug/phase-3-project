from lib.db.models import Customer, MenuItem, Mod, OrderItem, Order
from lib.db.db_setup import session, engine


def create_menu_items():
    espresso = MenuItem(item="espresso", price=3.50)
    latte = MenuItem(item="latte", price=4.50)
    session.add_all([espresso, latte])
    session.commit()


def create_mods():
    extra_shot = Mod(mod_item="extra shot", mod_price=.50)
    small = Mod(mod_item="small", mod_price=0)
    regular = Mod(mod_item="regular", mod_price=.50)
    large = Mod(mod_item="large", mod_price=1)
    session.add_all([extra_shot, small, regular, large])
    session.commit()


# def create_customers():
#     session.add_all()
#     session.commit()


# def create_orders():
#     session.add_all()
#     session.commit()


# def create_order_items():
#     session.add_all()
#     session.commit()


def delete_records():
    # session.query(Order).delete()
    # session.query(OrderItem).delete()
    session.query(MenuItem).delete()
    session.query(Mod).delete()
    # session.query(Customer).delete()

    session.commit()


if __name__ == '__main__':
    delete_records()
    create_menu_items()
    create_mods()
    # create_customers()
    # create_orders()
    # create_order_items()
