from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.base_class import Base


class AccountLoan(Base):
    __tablename__ = "account_loan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)

    account_id = Column(Integer, ForeignKey("account.id"), primary_key=True)
    loan_id = Column(Integer, ForeignKey("loan.id"), primary_key=True)

