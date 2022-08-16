from datetime import datetime
from dtos.mandate_dto import MandateDto
from utils.utils import Utils
from utils.contants import Constants
import json


class BillingService:
    def run_billing(self, date: datetime.date, mandate: MandateDto) -> None:
        # print("Starting billing...")

        for revenue in mandate.get_not_debited_revenues():

            rev_amount = float(revenue.amount)

            for advance in mandate.get_active_advances(revenue.date):

                # print("Advance ID:", advance.id)
                debited_amount = round(
                    rev_amount * advance.repayment_percentage / 100, 2
                )
                # print('Amount to debit: ', debited_amount, "Revenue date: ", revenue.date)

                if debited_amount > Constants.MAX_DAILY_CHARGES:
                    print("Max debit amount reached for advance ID:", advance.id)
                    debited_amount = Constants.MAX_DAILY_CHARGES

                if debited_amount > rev_amount:
                    print("Insufficient funds...")
                    continue

                # print("Executing...")
                metadata = json.dumps({"amount": str(debited_amount)})
                # print(metadata)
                response = Utils.execute_post_request(
                    Constants.CHARGES_ENDPOINT(mandate.id), metadata, str(date)
                )

                if response:
                    # print(response)
                    revenue.debited = True
                    rev_amount -= debited_amount
                    advance.pay_amount(date, debited_amount)

                else:
                    print(
                        "Error while applying charges for advance id : ",
                        advance.id,
                        " revenue date:",
                        revenue.date,
                    )
