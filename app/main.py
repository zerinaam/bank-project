from fastapi import FastAPI

from app.routers import account, bank, card, client, loan, transaction

app = FastAPI(
    title="bank",
    version="0.1.0",
)

app.include_router(account.router)
app.include_router(bank.router)
app.include_router(card.router)
app.include_router(client.router)
app.include_router(loan.router)
app.include_router(transaction.router)
