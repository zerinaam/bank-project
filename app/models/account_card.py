from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.base_class import Base


class AccountCard(Base):
    __tablename__ = "account_card"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)

    account_id = Column(Integer, ForeignKey("account.id"), primary_key=True)
    card_id = Column(Integer, ForeignKey("card.id"), primary_key=True)
