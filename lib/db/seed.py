from models import Customer, MenuItem, Mod, OrderItem, Order
from db_setup import session, engine
from faker import Faker
fake = Faker()


def create_menu_items():
    espresso = MenuItem(item="espresso", price=3.50)
    macchiato = MenuItem(item="macchiato", price=4)
    cappuccino = MenuItem(item="cappuccino", price=5.50)
    flat_white = MenuItem(item="flat white", price=5.50)
    latte = MenuItem(item="latte", price=5.50)
    chai_latte = MenuItem(item="chai latte", price=5)
    iced_coffee = MenuItem(item="iced coffee", price=6.50)
    iced_chocolate = MenuItem(item="iced chocolate", price=6.50)

    session.add_all([espresso, macchiato, cappuccino, flat_white,
                    latte, chai_latte, iced_coffee, iced_chocolate])
    session.commit()


def create_mods():
    extra_shot = Mod(mod_item="extra shot", mod_price=.50)
    weak = Mod(mod_item="weak", mod_price=0)
    extra_hot = Mod(mod_item="extra hot", mod_price=0)
    sugar = Mod(mod_item="sugar", mod_price=0)
    small = Mod(mod_item="small", mod_price=0)
    regular = Mod(mod_item="regular", mod_price=.50)
    large = Mod(mod_item="large", mod_price=1)
    full_cream = Mod(mod_item="full cream milk", mod_price=0)
    skim = Mod(mod_item="skim milk", mod_price=0.50)
    oat = Mod(mod_item="oat milk", mod_price=0.70)
    almond = Mod(mod_item="almond milk", mod_price=0.70)
    soy = Mod(mod_item="soy milk", mod_price=0.50)

    session.add_all([extra_shot, weak, extra_hot, sugar, small,
                    regular, large, full_cream, skim, oat, almond, soy])
    session.commit()


def create_customers():
    customers = [
        Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        for i in range(50)]

    session.add_all(customers)
    session.commit()


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
    session.query(Customer).delete()

    session.commit()


if __name__ == '__main__':
    delete_records()
    create_menu_items()
    create_mods()
    create_customers()
    # create_orders()
    # create_order_items()
