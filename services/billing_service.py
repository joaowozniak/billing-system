from datetime import datetime
from dtos.mandate_dto import MandateDto
from dtos.charge_dto import ChargeDto
from utils.utils import Utils
from utils.contants import Constants
import json

# TODO testing this service by mocking http requests
class BillingService:
    def run_billing(self, date: datetime.date, mandate: MandateDto) -> None:
        # initialize charges for the day for all the active advances
        charges = {}
        for revenue in mandate.get_not_debited_revenues():
            for advance in mandate.get_active_advances(revenue.date):
                charges[advance.id] = ChargeDto(
                    date=date, amount=0, advance_id=advance.id
                )
        # start billing
        for revenue in mandate.get_not_debited_revenues():
            rev_amount = float(revenue.amount)
            for advance in mandate.get_active_advances(revenue.date):
                charge = charges[advance.id]
                print("Starting billing Advance ID:", advance.id)
                debited_amount = round(
                    rev_amount * advance.repayment_percentage / 100, 2
                )
                print(
                    "Amount to debit: ", debited_amount, "Revenue date: ", revenue.date
                )
                debit_completed = True
                if (charge.amount + debited_amount) > Constants.MAX_DAILY_CHARGES:
                    print("Max debit amount reached for advance ID:", advance.id)
                    debited_amount = max(0, Constants.MAX_DAILY_CHARGES - charge.amount)
                    debit_completed = False
                print("Executing...")
                metadata = json.dumps({"amount": str(debited_amount)})

                response = Utils.execute_post_request(
                    Constants.CHARGES_ENDPOINT(mandate.id), metadata, str(date)
                )
                if response:
                    print(response)
                    advance.pay_amount(date, debited_amount)
                    charge.amount += debited_amount
                    if debit_completed:
                        revenue.debited = True
                    else:
                        amount_aux = float(revenue.amount) - debited_amount
                        revenue.amount = str(amount_aux)
                else:
                    print(
                        "Error while applying charges for advance id : ",
                        advance.id,
                        " revenue date:",
                        revenue.date,
                    )
