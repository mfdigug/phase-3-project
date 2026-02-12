from models import Customer, MenuItem, Mod
from db_setup import session
from faker import Faker
fake = Faker()


def create_menu_items():
    items = [
        MenuItem(item="espresso", price=3.50),
        MenuItem(item="macchiato", price=4),
        MenuItem(item="cappuccino", price=5.50),
        MenuItem(item="flat white", price=5.50),
        MenuItem(item="latte", price=5.50),
        MenuItem(item="chai latte", price=5),
        MenuItem(item="iced coffee", price=6.50),
        MenuItem(item="iced chocolate", price=6.50)
    ]
    session.add_all(items)
    session.commit()


def create_mods():
    mods = [
        Mod(mod_item="extra shot", mod_price=0.50),
        Mod(mod_item="weak", mod_price=0),
        Mod(mod_item="extra hot", mod_price=0),
        Mod(mod_item="sugar", mod_price=0),
        Mod(mod_item="small", mod_price=0),
        Mod(mod_item="regular", mod_price=0.50),
        Mod(mod_item="large", mod_price=1),
        Mod(mod_item="full cream milk", mod_price=0),
        Mod(mod_item="skim milk", mod_price=0.50),
        Mod(mod_item="oat milk", mod_price=0.70),
        Mod(mod_item="almond milk", mod_price=0.70),
        Mod(mod_item="soy milk", mod_price=0.50),
    ]

    session.add_all(mods)
    session.commit()


def create_customers():
    customers = [
        Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        for _ in range(50)]

    session.add_all(customers)
    session.commit()


# def delete_records():
#     session.query(OrderItem).delete()
#     session.query(Order).delete()
#     session.query(Mod).delete()
#     session.query(MenuItem).delete()
#     session.query(Customer).delete()

#     session.commit()


if __name__ == '__main__':
    # delete_records()
    create_menu_items()
    create_mods()
    create_customers()
