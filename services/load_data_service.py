from datetime import datetime, timedelta
from dtos.advance_dto import AdvanceDto
from dtos.mandate_dto import MandateDto
from dtos.revenue_dto import RevenueDto
from utils.utils import Utils
from utils.contants import Constants


class LoadDataService:
    def get_advances(self, date: datetime.date):
        # print(f"Getting advances for: {date}")

        response = Utils.execute_get_request(
            Constants.ADVANCES_ENDPOINT, str(date)
        ).json()

        return response

    def load_advances(self, response, advances_ids: set, mandate_to_advances: dict):

        for adv in response["advances"]:
            if adv["id"] not in advances_ids:
                advances_ids.add(adv["id"])
                mandate_to_advances[adv["mandate_id"]].add(
                    AdvanceDto(
                        adv["id"],
                        adv["customer_id"],
                        adv["created"],
                        adv["total_advanced"],
                        adv["fee"],
                        adv["mandate_id"],
                        adv["repayment_start_date"],
                        adv["repayment_percentage"],
                    )
                )

    def update_mandates_advances(
        self, mandate_to_advances: dict, mandates: dict
    ) -> None:
        # print("Updating customers advances...")

        for mandate_id, advs in mandate_to_advances.items():
            if mandate_id not in mandates.keys():
                mandates[mandate_id] = MandateDto(mandate_id, advs)
            else:
                mandates[mandate_id].advances = advs

    # TODO testing this service by mocking http requests
    def get_revenue_for_date(self, date: datetime.date, mandates: dict) -> None:
        # print(f"Retrieving revenues...")

        for cust in mandates.values():
            charging_dates = cust.dates_without_revenue[:]
            charging_dates.append(date - timedelta(1))
            # print(f"Customer Id: {cust.id} missing revenue dates {charging_dates}")
            for charge_date in charging_dates[:]:
                response = Utils.execute_get_request(
                    Constants.REVENUES_ENDPOINT(cust.id, str(charge_date)), str(date)
                )

                if response:
                    # print(response.json(), charge_date)
                    cust.revenues.append(
                        RevenueDto(response.json()["amount"], charge_date)
                    )
                    charging_dates.remove(charge_date)
                    # print("OK, days left: ", charging_dates)
                else:
                    # print(response)
                    # print("KO, days left: ", charging_dates)
                    pass

            cust.dates_without_revenue = charging_dates
