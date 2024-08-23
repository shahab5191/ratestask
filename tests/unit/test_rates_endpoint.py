from typing import Dict, List
import unittest
from unittest.mock import patch

from loguru import logger
from src.config import Config
from src.rates import bp
import flask
from flask.testing import FlaskClient


class TestRatesEndpoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = flask.Flask(__name__)
        app.config.from_object(["TESTING"])
        app.register_blueprint(bp)
        cls.client: FlaskClient = app.test_client()

    @classmethod
    def tearDownClass(cls):
        patch.stopall()

    def setUp(self):
        self.mock_get_rates = patch("src.rates.routes.get_rates").start()
    
    def test_success_with_result(self):
        params = {
            "date_from": "2016-01-01",
            "date_to": "2016-01-30",
            "origin": "china_main",
            "destination": "scandinavia"
        }
        expected_result = [{
            "average_price": "1154.67",
            "day": "2016-01-01"
        },
        {
            "average_price": "1154.67",
            "day": "2016-01-02"
        }]
        self.mock_get_rates.return_value = expected_result

        response = self.client.get(f'{Config.API_PREFIX}/rates', query_string=params)

        self.assertEqual(response.status_code, 200)
        result = response.json
        self.assertIsNotNone(result)
        assert isinstance(result, Dict)
        self.assertIn("rates", result)
        rates = result.get('rates')
        assert isinstance(rates, List)
        self.assertDictEqual(rates[0], expected_result[0])


    def test_unsuccessful_validation_error(self):
        params = {
            "date_from": "",
            "date_to": "2016-01-30",
            "origin": "test",
            "destination": "test"
        }

        expected_result = {"error": "query parameters are not valid!"}
        
        response = self.client.get(f"{Config.API_PREFIX}/rates", query_string=params)
        self.assertEqual(response.status_code, 400)
        result = response.json
        assert isinstance(result, Dict)
        self.assertDictEqual(result, expected_result)

    def test_unsuccessful_validation_error_wrong_date(self):
        params = {
            "date_from": "test",
            "date_to": "2016-01-30",
            "origin": "test",
            "destination": "test"
        }

        expected_result = {"error": "query parameters are not valid!"}
        
        response = self.client.get(f"{Config.API_PREFIX}/rates", query_string=params)
        self.assertEqual(response.status_code, 400)
        result = response.json
        assert isinstance(result, Dict)
        self.assertDictEqual(result, expected_result)

    def test_unsuccessful_validation_error_missing_param(self):
        params = {
            "date_to": "2016-01-30",
            "origin": "test",
            "destination": "test"
        }

        expected_result = {"error": "query parameters are not valid!"}
        
        response = self.client.get(f"{Config.API_PREFIX}/rates", query_string=params)
        self.assertEqual(response.status_code, 400)
        result = response.json
        assert isinstance(result, Dict)
        self.assertDictEqual(result, expected_result)

    def test_unsuccessful_internal_error(self):
        params = {
            "date_from": "2016-01-01",
            "date_to": "2016-01-30",
            "origin": "test",
            "destination": "test"
        }

        expected_result = {"error": "Internal error"}
        self.mock_get_rates.side_effect = Exception()
        response = self.client.get(f"{Config.API_PREFIX}/rates", query_string=params)
        self.assertEqual(response.status_code, 500)
        result = response.json
        assert isinstance(result, Dict)
        self.assertDictEqual(result, expected_result)
