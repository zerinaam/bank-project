from fastapi import APIRouter
from app.db.session import session
from app.models.account import Account
from app.models.bank import Bank
from app.schemas.account import AccountModel

router = APIRouter()


@router.get("/bank/{bank_name}/account")
async def get_account_by_bank_name(bank_name: str):
    bank = session.query(Bank).filter(Bank.name == bank_name).first()
    account = session.query(Account).filter(Account.bank_id == bank.id).first()
    return account


@router.post("/bank/{bank_name}/account")
async def add_account(account_model: AccountModel):
    account = Account(
        id=account_model.id,
        created_at=account_model.created_at,
        active=account_model.active,
        bank_id=account_model.bank_id,
        client_id=account_model.client_id
    )

    session.add(account)
    session.commit()
    return "Account has been added."


@router.get("/bank/{bank_name}/account/{account_id}")
async def get_account_by_id(bank_name: str, account_id: int):
    account = (
       session.query(Account)
       .join(Bank, Account.bank_id == Bank.id)
       .filter(Bank.name == bank_name, Account.id == account_id)
       .first()
    )

    return account


@router.put("/bank/{bank_name}/account/{account_id}")
async def update_account_by_id(bank_name: str, account_id: int, account_update: AccountModel):
    account = (
        session.query(Account)
        .join(Bank, Account.bank_id == Bank.id)
        .filter(Bank.name == bank_name, Account.id == account_id)
        .first()
    )

    if account is None:
        return "Account with provided id does not exist."

    account.created_at = account_update.created_at if account_update.created_at else account.created_at
    account.active = account_update.active if account_update.active else account.active
    account.bank_id = account_update.bank_id if account_update.bank_id else account.bank_id
    account.client_id = account_update.client_id if account_update.client_id else account.client_id

    session.commit()
    return "Account has been updated."


@router.delete("/bank/{bank_name}/account/{account_id}")
async def delete_account_by_id(bank_name: str, account_id: int):
    account = (
        session.query(Account)
        .join(Bank, Account.bank_id == Bank.id)
        .filter(Bank.name == bank_name, Account.id == account_id)
    )
    if account is None:
        return f"Account with id {account_id} does not exist."

    session.delete(account)
    session.commit()
    return "Account has been deleted."









