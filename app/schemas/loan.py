from pydantic import BaseModel
from pydantic.schema import datetime

from app.utils.enums import LoanTypeEnum


class LoanModel(BaseModel):
    id: int | None
    created_at: datetime | None
    type: LoanTypeEnum | None
    interest_rate: int | None
    duration: int | None
    expected_end_date: datetime
    rate: int | None
    amount: int | None
    active: bool | None
