from collections import defaultdict
from datetime import datetime
from dtos.advance_dto import AdvanceDto
from services.load_data_service import LoadDataService
import unittest


class BillingTests(unittest.TestCase):
    def test_load_data_service(self):
        loading = LoadDataService()
        mandate_to_advances = defaultdict(set)
        advances_ids = set()
        mandates = defaultdict(None)

        api_response = {
            "advances": [
                {
                    "id": 1,
                    "customer_id": 1,
                    "mandate_id": 2,
                    "created": "2022-01-02",
                    "total_advanced": "60000.00",
                    "fee": "2500.00",
                    "repayment_start_date": "2022-01-02",
                    "repayment_percentage": 11,
                }
            ]
        }

        loading.load_advances(api_response, advances_ids, mandate_to_advances)

        self.assertIsNotNone(mandate_to_advances, "Test load not none")
        self.assertEqual(
            len(mandate_to_advances), 1, "Test load to map with correct length"
        )
        self.assertEqual(
            len(advances_ids), 1, "Test load to advances tracker with correct length"
        )
        advance = AdvanceDto(
            1, 1, "2022-01-02", "60000.00", "2500.00", 2, "2022-01-02", 11
        )

        mandate_id = advance.mandate_id
        for adv in mandate_to_advances[mandate_id]:
            self.assertEqual(adv.fee, advance.fee, "Test correct fee mapping")
            self.assertEqual(
                adv.created, advance.created, "Test correct created date mapping"
            )
            self.assertEqual(
                adv.total_advanced,
                advance.total_advanced,
                "Test correct total_advanced mapping",
            )
            self.assertEqual(
                adv.repayment_start_date,
                advance.repayment_start_date,
                "Test correct repayment_start_date mapping",
            )
            self.assertEqual(
                adv.repayment_percentage,
                advance.repayment_percentage,
                "Test correct repayment_percentage mapping",
            )

        loading.update_mandates_advances(mandate_to_advances, mandates)

        self.assertIsNotNone(mandates, "Test mandates list not none")
        self.assertEqual(len(mandates), 1, "Test load to mandates with correct length")
        self.assertEqual(
            list(mandates.keys())[0], mandate_id, "Test correct mandate id mapping"
        )

        self.assertEqual(
            list(mandates.values())[0].id, 2, "Test correct mandate id mapping"
        )
        self.assertEqual(
            len(list(mandates.values())[0].advances),
            1,
            "Test correct mandate advances len mapping",
        )
        self.assertEqual(
            list(mandates.values())[0].revenues, [], "Test correct revenues mapping"
        )
        self.assertEqual(
            list(mandates.values())[0].dates_without_revenue,
            [],
            "Test correct dates_without_revenue mapping",
        )


if __name__ == "__main__":
    unittest.main()
