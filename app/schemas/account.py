from pydantic import BaseModel
from pydantic.schema import datetime


class AccountModel(BaseModel):
    id: int | None
    created_at: datetime | None
    active: bool | None
    bank_id: int | None
    client_id: int | None

