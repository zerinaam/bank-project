from enum import Enum


class CardTypeEnum(Enum):
    debit_card = "debit card"
    credit_card = "credit card"
    prepaid_card = "prepaid card"


class LoanTypeEnum(Enum):
    non_purpose_loan = "non purpose loan"
    housing_loan = "housing loan"
    business_loan = "business loan"
