from pydantic import BaseModel
from pydantic.schema import datetime

from app.utils.enums import CardTypeEnum


class TransactionModel(BaseModel):
    sender_id: int | None
    receiver_id: int | None
    amount: int | None
