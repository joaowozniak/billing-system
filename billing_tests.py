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


if __name__ == "__main__":
    unittest.main()
