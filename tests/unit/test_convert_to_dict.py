import datetime
from typing import List, Tuple
import unittest

from src.utils.convert_to_dict import convert_to_dict


class TestConvertTotDict(unittest.TestCase):
    def test_valid_data(self):
        colnames = ["col1", "col2", "col3", "col4"]
        rows: List[Tuple[str, ...]] = [
                ("1", "2", "3", "4"),
                ("1", "2", "3", "4")
            ]

        expected_result = [{
            "col1": "1",
            "col2": "2",
            "col3": "3",
            "col4": "4"
        },
        {
            "col1": "1",
            "col2": "2",
            "col3": "3",
            "col4": "4"
        }]

        result = convert_to_dict(colnames, rows)

        self.assertEqual(len(result), 2)
        self.assertDictEqual(result[0], expected_result[0])
        self.assertDictEqual(result[1], expected_result[0])


    def test_empty_data(self):
        colnames = []
        rows = []

        result = convert_to_dict(colnames, rows)
        self.assertEqual(len(result), 0)

    def test_with_date_formatting(self):
        colnames = ["col1", "col2", "col3", "col4"]
        rows = [("1", datetime.date(2016, 2, 1), "2", "3")]
        format = "%Y-%m-%d"
        expected_result = {
            "col1": "1",
            "col2": "2016-02-01",
            "col3": "2",
            "col4": "3"
        }

        result = convert_to_dict(colnames, rows, format)

        self.assertDictEqual(result[0], expected_result)

    def test_with_date_without_formatting(self):
        colnames = ["col1", "col2", "col3", "col4"]
        rows = [("1", datetime.date(2016, 2, 1), "2", "3")]
        expected_result = {
            "col1": "1",
            "col2": datetime.date(2016, 2, 1),
            "col3": "2",
            "col4": "3"
        }

        result = convert_to_dict(colnames, rows)

        self.assertDictEqual(result[0], expected_result)
