from datetime import datetime
from .revenue_dto import RevenueDto

"""
Class MandateDto that maps the list of advances for a given mandate. 
Also keeps track of daily business revenues and of uncontrolled not debited revenues percentage.
"""


class MandateDto:
    def __init__(self, id: int, advances: list):

        self.id = id
        self.advances = advances
        self.revenues = []
        self.dates_without_revenue = []

    def get_active_advances(self, day: datetime.date) -> list:

        active_advances = []
        for advance in self.advances:
            if str(day) >= advance.repayment_start_date and not advance.repaid:
                active_advances.append(advance)

        return active_advances

    def get_revenue_by_day(self, day: datetime.date) -> RevenueDto:

        for revenue in self.revenues:
            if revenue.date == str(day):
                return revenue

        return None

    def get_not_debited_revenues(self) -> list:

        non_debited_revenues = []
        for revenue in self.revenues:
            if revenue.debited == False:
                non_debited_revenues.append(revenue)

        return non_debited_revenues
