from collections import defaultdict
from pandas import date_range
from services.billing_service import BillingService
from services.load_data_service import LoadDataService
from utils.contants import Constants
from collections import defaultdict


def main():

    data_load = LoadDataService()
    billing_service = BillingService()
    customer_to_advances = defaultdict(set)
    advances_ids = set()
    mandates = defaultdict(None)

    for today in date_range(Constants.START_DATE, Constants.END_DATE).date:
        print("\nTODAY: ", today)

        # load daily data
        data_load.get_advances(today, advances_ids, customer_to_advances)
        data_load.update_mandates_advances(customer_to_advances, mandates)
        data_load.get_revenue_for_date(today, mandates)

        # run billing
        for mandate in mandates.values():
            billing_service.run_billing(today, mandate)


if __name__ == "__main__":
    main()
