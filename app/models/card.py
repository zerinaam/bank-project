from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, DECIMAL
from app.db.base_class import Base
from app.utils.enums import CardTypeEnum


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    type = Column(Enum(CardTypeEnum))
    card_number = Column(DECIMAL(16, 0))
    expires = Column(String)
    amount = Column(Integer)
    active = Column(Boolean)



