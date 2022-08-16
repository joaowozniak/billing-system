from datetime import datetime


class RevenueDto:

    def __init__(self, amount: str, date: datetime.date):
        self.amount = amount        
        self.date = date
        self.debited = False