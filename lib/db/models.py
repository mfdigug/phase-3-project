from sqlalchemy import Table, ForeignKey, MetaData, Column, Integer, Float, String, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

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
    order_items = relationship('OrderItem', back_populates="menu_item")

    def __repr__(self):
        return f"Menu item {self.id}: " \
            + f"{self.item}, " \
            + f"{self.price}"


class Mod(Base):
    __tablename__ = "mods"

    id = Column(Integer, primary_key=True)
    mod_item = Column(String(), nullable=False)
    mod_price = Column(Float(), nullable=False)

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
    created_at = Column(DateTime(), server_default=func.now())

    # relationships
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    order_items = relationship(
        "OrderItem", backref="order", cascade="all, delete-orphan")
    # deleting an order deletes all its orderitems

    # methods
    def order_total(self):
        return sum(order_item.subtotal() for order_item in self.order_items)

    def __repr__(self):
        return f"Order Number: {self.id}"


class OrderItemMod(Base):
    __tablename__ = "order_item_mods"

    order_item_id = Column(Integer, ForeignKey(
        "order_items.id"), primary_key=True)
    mod_id = Column(Integer, ForeignKey("mods.id"), primary_key=True)

    order_item = relationship("OrderItem", back_populates="order_item_mods")
    mod = relationship("Mod")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer(), primary_key=True)
    quantity = Column(Integer(), default=1)

    # relationships
    menu_item_id = Column(Integer(), ForeignKey("menu_items.id"))
    menu_item = relationship("MenuItem", back_populates="order_items")
    order_id = Column(Integer(), ForeignKey("orders.id", ondelete="CASCADE"))
    # if an order is deleted, delete associated order items
    order_item_mods = relationship(
        "OrderItemMod",
        cascade="all, delete-orphan"
    )

    mods = association_proxy(
        "order_item_mods",
        "mod",
        creator=lambda mod: OrderItemMod(mod=mod)
    )

    def subtotal(self):
        return self.quantity*(self.menu_item.price + sum(mod.mod_price for mod in self.mods))

    def __repr__(self):
        return f"Item No {self.id}. {self.menu_item.item}, add ons:{[mod.mod_item for mod in self.mods]}"
