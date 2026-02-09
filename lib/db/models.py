from sqlalchemy import Table, ForeignKey, MetaData, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer(), primary_key=True)
    item = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    # relationships
    order_items = relationship('OrderItem', backref="menu_item")

    def __repr__(self):
        return f"Menu item {self.id}: " \
            + f"{self.item}, " \
            + f"{self.price}"


class Mod(Base):
    __tablename__ = "mods"

    id = Column(Integer, primary_key=True)
    mod_item = Column(String(), nullable=False)
    mod_price = Column(Float(), nullable=False)

    # relationships
    order_items = relationship(
        "OrderItem", secondary="order_item_mods", back_populates="mods")

    def __repr__(self):
        return f"Modification: {self.id}: " \
            + f"{self.mod_item}, " \
            + f"{self.mod_price}"


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(), unique=True)

    # relationships
    orders = relationship("Order", backref="customer")

    def __repr__(self):
        return f"Customer: {self.id}: " \
            + f"{self.first_name}"


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    # relationships
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    # deleting an order deletes all its orderitems
    order_items = relationship(
        "OrderItem", backref="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Order Number: {self.id}"


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer(), primary_key=True)
    # relationships
    menu_item_id = Column(Integer(), ForeignKey("menu_items.id"))
    # if an order is deleted, delete associated order items
    order_id = Column(Integer(), ForeignKey("orders.id", ondelete="CASCADE"))
    # link to join table - allow passive deletes to handle delete associated items
    mods = relationship("Mod", secondary="order_item_mods",
                        back_populates="order_items", passive_deletes=True)


order_item_mod = Table(
    "order_item_mods",
    Base.metadata,
    # if an order_item is deleted delete all associated mods -> ondelete="CASCADE"
    Column("order_item_id", ForeignKey(
        "order_items.id", ondelete="CASCADE"), primary_key=True),
    # no cascade - only want to remove() mods from order items
    Column("mod_id", ForeignKey("mods.id"), primary_key=True),
    extend_existing=True
)
