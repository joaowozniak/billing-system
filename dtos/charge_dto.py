from datetime import datetime

"""
Class ChargeDto keeps track of amount charged on a advance on any given day.
"""


class ChargeDto:
    def __init__(self, amount: str, date: datetime.date, advance_id: int):
        self.amount = amount
        self.date = date
        self.advance_id = advance_id
