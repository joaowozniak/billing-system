import datetime

"""
class of constants
"""


class Constants:

    BILLING_URL = "https://billing.eng-test.wayflyer.com/v2"

    ADVANCES_ENDPOINT = BILLING_URL + "/advances"

    def REVENUES_ENDPOINT(id: int, date: datetime.date) -> str:
        return (
            f"https://billing.eng-test.wayflyer.com/v2/customers/{id}/revenues/{date}"
        )

    def CHARGES_ENDPOINT(id: str) -> str:
        return f"https://billing.eng-test.wayflyer.com/v2/mandates/{id}/charge"

    def BILLING_COMPLETE_ENDPOINT(id: str) -> str:
        return (
            f"https://billing.eng-test.wayflyer.com/v2/advances/{id}/billing_complete"
        )

    START_DATE = datetime.date(2022, 1, 1)

    END_DATE = datetime.date(2022, 6, 30)

    MAX_DAILY_CHARGES = 10000
