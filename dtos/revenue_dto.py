from datetime import datetime

"""
Class RevenueDto that maps the amount of revenue of a given day, the date and its debit status.
"""


class RevenueDto:
    def __init__(self, amount: str, date: datetime.date):
        self.amount = amount
        self.date = date
        self.debited = False
