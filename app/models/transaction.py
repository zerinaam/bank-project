from sqlalchemy import Column, Integer
from app.db.base_class import Base


class Transaction(Base):
    __tablename__ = "transaction"

    sender_id = Column(Integer, primary_key=True)
    receiver_id = Column(Integer)
    amount = Column(Integer)

