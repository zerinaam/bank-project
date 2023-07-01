from pydantic import BaseModel
from pydantic.schema import datetime


class ClientModel(BaseModel):
    id: int | None
    created_at: datetime | None
    first_name: str | None
    last_name: str | None
    street_address: str | None
    phone_number: str | None
    post_number: str | None
    town: str | None
