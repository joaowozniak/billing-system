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
    
    def test_load_advances(self):
        billing = LoadDataService()
        mandate_to_advances = defaultdict(set)
        advances_ids = set()

        api_response = { 
                "advances": [
                    {
                        "id": 1,
                        "customer_id": 1,
                        "mandate_id": 2,
                        "created": "2022-01-02",
                        "total_advanced": "60000.00",
                        "fee": "2500.00",
                        "repayment_start_date": "2022-01-05",
                        "repayment_percentage": 11
                    }
                ]
            }

        billing.load_advances(api_response, advances_ids, mandate_to_advances)

        self.assertIsNotNone(mandate_to_advances, "Test load not none")
        self.assertEqual(len(mandate_to_advances), 1, "Test load to map with correct length")
        self.assertEqual(len(advances_ids), 1, "Test load to advances tracker with correct length")
        advance = AdvanceDto(1, 1, "2022-01-02", "60000.00", "2500.00", 2, "2022-01-05", 11)

        mandate_id = advance.mandate_id
        for adv in mandate_to_advances[mandate_id]:
            self.assertEqual(adv.fee, advance.fee, "Test correct fee mapping")
            self.assertEqual(adv.created, advance.created, "Test correct created date mapping")
            self.assertEqual(adv.total_advanced, advance.total_advanced, "Test correct total_advanced mapping")
            self.assertEqual(adv.repayment_start_date, advance.repayment_start_date, "Test correct repayment_start_date mapping")
            self.assertEqual(adv.repayment_percentage, advance.repayment_percentage, "Test correct repayment_percentage mapping")

if __name__ == "__main__":
    unittest.main()
