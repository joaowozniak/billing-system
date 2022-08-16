from datetime import datetime
import json
from utils.utils import Utils
from utils.contants import Constants

"""
Class AdvanceDto that maps the advance info and keeps track of payment status.
Notifies API once it reaches full repayment.
"""


class AdvanceDto:
    def __init__(
        self,
        id: int,
        customer_id: int,
        created: datetime.date,
        total_advanced: str,
        fee: str,
        mandate_id: int,
        repayment_start_date: datetime.date,
        repayment_percentage: int,
    ):

        self.id = id
        self.customer_id = customer_id
        self.created = created
        self.total_advanced = total_advanced
        self.fee = fee
        self.mandate_id = mandate_id
        self.repayment_start_date = repayment_start_date
        self.repayment_percentage = repayment_percentage
        self.total_paid = 0
        self.to_be_paid = float(total_advanced) + float(fee)
        self.repaid = False

    def pay_amount(self, date: datetime.date, amount: float) -> None:

        if self.to_be_paid <= amount:
            self.to_be_paid = 0
            self.total_paid += self.to_be_paid
            self.repaid = True

            print(f"Advance ID:{self.id} paid in full. Updating billing status...")

            metadata = json.dumps({})
            response = Utils.execute_post_request(
                Constants.BILLING_COMPLETE_ENDPOINT(self.id), metadata, str(date)
            )

            if response:
                print("Billing notification complete for Advance id: ", self.id)

            else:
                print("Error while notifying billing complete...: ", response)

        else:

            self.total_paid += amount
            self.to_be_paid -= amount
            print(
                f"Updating advance {self.id} debt. Current: {round(self.to_be_paid,2)}"
            )
