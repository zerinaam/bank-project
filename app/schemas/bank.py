from pydantic import BaseModel


class BankModel(BaseModel):
    id: int | None
    name: str | None
    country: str | None
    town: str | None
    street_address: str | None
    phone_number: str | None
    post_number: str | None
