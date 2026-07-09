from pydantic import BaseModel

class Transaction(BaseModel):

    transaction_id: int

    account_number: str

    amount: float

    transaction_type: str

    status: str