from pydantic import BaseModel
from pydantic.schema import datetime


class AccountLoanModel(BaseModel):
    id: int | None
    created_at: datetime | None
    account_id: int | None
    loan_id: int
