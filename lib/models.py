from sqlalchemy import ForeignKey, MetaData, create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///cafe.db')
Base = declarative_base(metadata=metadata)


class MenuItems(Base):
    __tablename__ = "menu_items"

    id = Column(Integer(), primary_key=True)
    item = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

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

    def __repr__(self):
        return f"Customer: {self.id}: " \
            + f"{self.first_name}"
