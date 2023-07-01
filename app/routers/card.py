from fastapi import APIRouter
from app.db.session import session
from app.models.account import Account
from app.models.bank import Bank
from app.models.card import Card
from app.schemas.card import CardModel

router = APIRouter()


@router.post("/bank/account/card")
async def add_card(card_model: CardModel):
    card = Card(
        id=card_model.id,
        created_at=card_model.created_at,
        type=card_model.type,
        card_number=card_model.card_number,
        expires=card_model.expires,
        amount=card_model.amount,
        active=card_model.active,
    )

    session.add(card)
    session.commit()

    return "Card has been added."


@router.get("/bank/{bank_name}/account/{account_id}/card/{card_id}")
async def get_card_by_card_id(bank_name: str, account_id: int, card_id: int):
    account = (
        session.query(Account)
        .join(Bank, Account.bank_id == Bank.id)
        .filter(Bank.name == bank_name, Account.id == account_id)
        .first()
    )

    card = session.query(Card).filter(Card.id == card_id).first()

    return account, card


@router.put("/bank/account/card/{card_id}")
async def update_card(card_id: int, card_update: CardModel):
    card = session.query(Card).filter(Card.id == card_id).first()

    if card is None:
        return "Bank with provided name does not exist."

    card.created_at = card_update.created_at if card_update.created_at else card.created_at
    card.type = card_update.type if card_update.type else card.type
    card.card_number = card_update.card_number if card_update.card_number else card.card_number
    card.expires = card_update.expires if card_update.expires else card.expires
    card.amount = card_update.amount if card_update.amount else card.amount
    card.active = card_update.active if card_update.active else card.active

    session.commit()
    return "Card has been updated."


@router.delete("/bank/account/card/{card_id}")
async def delete_card(card_id: int):
    card = session.query(Card).filter(Card.id == card_id).first()
    if card is None:
        return f"Bank with name {card} does not exist."

    session.delete(card)
    session.commit()
    return "Bank has been deleted."






