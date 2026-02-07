from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cafe.db')
Base = declarative_base()


class MenuItems(Base):
    __tablename__ = "menu_items"

    id = Column(Integer(), primary_key=True)
    item = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)

    def __repr__(self):
        return f"Menu item {self.id}: " \
            + f"{self.item}, " \
            + f"{self.price}"
