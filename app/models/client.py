from sqlalchemy import Column, Integer, String, DateTime
from app.db.base_class import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    first_name = Column(String)
    last_name = Column(String)
    street_address = Column(String)
    phone_number = Column(String)
    post_number = Column(String)
    town = Column(String)

