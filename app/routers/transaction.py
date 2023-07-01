from fastapi import APIRouter
from app.db.session import session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionModel

router = APIRouter()


@router.post("/bank/transaction")
async def add_transaction(transaction_model: TransactionModel):
    transaction = Transaction(
        sender_id=transaction_model.sender_id,
        receiver_id=transaction_model.receiver_id,
        amount=transaction_model.amount
    )

    session.add(transaction)
    session.commit()

    return "The transaction has been recorded."


@router.delete("/bank/transaction/{sender_id}")
async def delete_transaction(sender_id: int):
    transaction = session.query(Transaction).filter(Transaction.sender_id == sender_id).first()
    if transaction is None:
        return f"Sender with provided id {sender_id} does not exist."

    session.delete(transaction)
    session.commit()
    return "Transaction has been deleted."

