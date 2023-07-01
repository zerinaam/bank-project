from fastapi import APIRouter
from app.db.session import session
from app.models.loan import Loan
from app.schemas.loan import LoanModel

router = APIRouter()


@router.get("/bank/account/loan/{loan_id}")
async def get_loan(loan_id: int):
    loan = session.query(Loan).filter(Loan.id == loan_id).first()
    return loan


@router.post("/bank/account/loan")
async def post_loan(loan_model: LoanModel):
    loan = Loan(
        id=loan_model.id,
        created_at=loan_model.created_at,
        type=loan_model.type,
        interest_rate=loan_model.interest_rate,
        duration=loan_model.duration,
        expected_end_date=loan_model.expected_end_date,
        rate=loan_model.rate,
        amount=loan_model.amount,
        active=loan_model.active
    )

    session.add(loan)
    session.commit()
    return "Loan has been added."


@router.put("/bank/account/loan/{loan_id}")
async def update_loan(loan_id: int, loan_update: LoanModel):
    loan = session.query(Loan).filter(Loan.id == loan_id).first()

    if loan is None:
        return "Loan with provided name does not exist."

    loan.created_at = loan_update.created_at if loan_update.created_at else loan.created_at
    loan.type = loan_update.type if loan_update.type else loan.type
    loan.interest_rate = loan_update.interest_rate if loan_update.interest_rate else loan.interest_rate
    loan.duration = loan_update.duration if loan_update.duration else loan.duration
    loan.expected_end_date = loan_update.expected_end_date if loan_update.expected_end_date else loan.expected_end_date
    loan.rate = loan_update.rate if loan_update.rate else loan.rate
    loan.amount = loan_update.amount if loan_update.amount else loan.amount
    loan.active = loan_update.active if loan_update.active else loan.active

    session.commit()
    return "Loan has been updated."


@router.delete("/bank/account/loan/{loan_id}")
async def delete_loan(loan_id: int):
    loan = session.query(Loan).filter(Loan.id == loan_id).first()

    if loan is None:
        return f"Loan with provided id {loan_id} does not exist."

    session.delete(loan)
    session.commit()
    return "Loan has been deleted."



