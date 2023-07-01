from pydantic import BaseModel
from pydantic.schema import datetime

from app.utils.enums import CardTypeEnum


class CardModel(BaseModel):
    id: int | None
    created_at: datetime | None
    type: CardTypeEnum | None
    card_number: int | None
    expires: str | None
    amount: int | None
    active: bool | None
