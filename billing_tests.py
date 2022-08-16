from collections import defaultdict
from email.policy import default
import unittest
from unittest.mock import Mock, patch
from dtos.advance_dto import AdvanceDto
from dtos.mandate_dto import MandateDto
from dtos.revenue_dto import RevenueDto
from services.billing_service import BillingService
from services.load_data_service import LoadDataService
from utils.contants import Constants

import unittest
import responses
from responses import GET, POST
import re


class BillingTests(unittest.TestCase):
    def test(self):
        billing = LoadDataService()
        self.responses = responses.RequestsMock()  # creating a mock object
        self.responses.start()  # activate

        with open("tests/tes.json", "r") as f:
            data = f.read()
            f.close()

        self.responses.add(
            GET, url=Constants.ADVANCES_ENDPOINT, body=data
        )  # queue a response

        # this line makes a request but is redirected to the queued response
        resp = billing.get_advances("", set(), defaultdict(set))
        print(resp)
        self.assertIsNotNone(resp)

        # deactivate (future requests will not redirected to our queued response)
        self.addCleanup(self.responses.stop)
        self.addCleanup(self.responses.reset)  # queued response is deleted


if __name__ == "__main__":
    unittest.main()
