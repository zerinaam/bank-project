from pydantic import BaseModel
from pydantic.schema import datetime


class AccountCardModel(BaseModel):
    id: int | None
    created_at: datetime | None
    account_id: int | None
    card_id: int | None

