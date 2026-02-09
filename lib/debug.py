from db.models import Base, MenuItem, Mod, Customer, Order, OrderItem
from helpers import get_customer_by_email
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # creates tables in memory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fake menu items
    espresso = MenuItem(item="espresso", price=3.50)
    macchiato = MenuItem(item="macchiato", price=4)
    cappuccino = MenuItem(item="cappuccino", price=5.50)
    flat_white = MenuItem(item="flat white", price=5.50)
    # Fake mods
    extra_shot = Mod(mod_item="extra shot", mod_price=.50)
    extra_hot = Mod(mod_item="extra hot", mod_price=0)
    sugar = Mod(mod_item="sugar", mod_price=0)
    small = Mod(mod_item="small", mod_price=0)
    regular = Mod(mod_item="regular", mod_price=.50)
    large = Mod(mod_item="large", mod_price=1)

    # fake customers
    Maria = Customer(first_name="Maria", last_name="Smith",
                     email="maria@example.com")
    Jo = Customer(first_name="Jo", last_name="Smith", email="jo@example.com")
    Phil = Customer(first_name="Phil", last_name="Smith",
                    email="alice@example.com")

    order1 = Order(customer=Maria)

    session.add_all([espresso, macchiato, cappuccino, flat_white,
                    extra_shot, sugar, small, regular, large, Maria, Jo, Phil])
    session.commit()

    import ipdb
    ipdb.set_trace()
