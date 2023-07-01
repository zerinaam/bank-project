from fastapi import APIRouter
from app.db.session import session
from app.models.bank import Bank
from app.schemas.bank import BankModel

router = APIRouter()


@router.get("/bank")
async def get_bank():
    return session.query(Bank).all()


@router.post("/bank")
async def add_bank(bank_model: BankModel):
    bank = Bank(
        id=bank_model.id,
        name=bank_model.name,
        country=bank_model.country,
        town=bank_model.town,
        street_address=bank_model.street_address,
        phone_number=bank_model.phone_number,
        post_number=bank_model.post_number
    )

    session.add(bank)
    session.commit()
    return "The bank has been added."


@router.get("/bank/{bank_name}")
async def get_bank_by_bank_name(bank_name: str):
    return session.query(Bank).filter(Bank.name == bank_name).first()


@router.put("/bank/{bank_name}")
async def update_bank(bank_name: str, bank_update: BankModel):
    bank = session.query(Bank).filter(Bank.name == bank_name).first()
    if bank is None:
        return "Bank with provided name does not exist."

    bank.country = bank_update.country if bank_update.country else bank.country
    bank.town = bank_update.town if bank_update.town else bank.town
    bank.street_address = bank_update.street_address if bank_update.street_address else bank.street_address
    bank.phone_number = bank_update.phone_number if bank_update.phone_number else bank.phone_number
    bank.post_number = bank_update.post_number if bank_update.post_number else bank.post_number

    session.commit()
    return "Bank has been updated."


@router.delete("/bank/{bank_name}")
async def delete_bank(bank_name: str):
    bank = session.query(Bank).filter(Bank.name == bank_name).first()
    if bank is None:
        return f"Bank with name {bank_name} does not exist."

    session.delete(bank)
    session.commit()
    return "Bank has been deleted."




