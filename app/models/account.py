from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from app.db.base_class import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    active = Column(Boolean)
    bank_id = Column(Integer, ForeignKey("bank.id"))
    client_id = Column(Integer, ForeignKey("client.id"))





