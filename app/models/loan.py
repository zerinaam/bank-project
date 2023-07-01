from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.utils.enums import LoanTypeEnum


class Loan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    type = Column(Enum(LoanTypeEnum))
    interest_rate = Column(DECIMAL)
    duration = Column(Integer)
    expected_end_date = Column(DateTime)
    rate = Column(Integer)
    amount = Column(Integer)
    active = Column(Boolean)

