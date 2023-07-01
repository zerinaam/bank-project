from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    country = Column(String)
    town = Column(String)
    street_address = Column(String)
    phone_number = Column(String)
    post_number = Column(String)


