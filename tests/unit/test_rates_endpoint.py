from typing import Dict, List
import unittest
from unittest.mock import patch
from src.config import Config
from src.rates import bp
import flask
from flask.testing import FlaskClient


class TestRatesEndpoint(unittest.TestCase):
    """
    Unit tests for the `/rates` endpoint of the application.

    This test suite includes the following test cases:

    1. **test_success_with_result**:
        - Tests the scenario where valid query parameters are provided.
        - Mocks the `get_rates` function to return a predefined result.
        - Verifies that the endpoint returns a 200 status code with the expected JSON structure.

    2. **test_unsuccessful_validation_error**:
        - Tests the scenario where invalid query parameters are provided (e.g., an empty `date_from`).
        - Ensures the endpoint returns a 400 status code with an appropriate validation error message.

    3. **test_unsuccessful_validation_error_wrong_date**:
        - Tests the scenario where the `date_from` parameter is not a valid date.
        - Ensures the endpoint returns a 400 status code with a validation error message.

    4. **test_unsuccessful_validation_error_missing_param**:
        - Tests the scenario where a required query parameter is missing (e.g., `date_from`).
        - Ensures the endpoint returns a 400 status code with a validation error message.

    5. **test_unsuccessful_internal_error**:
        - Tests the scenario where an internal server error occurs (e.g., an exception is raised in `get_rates`).
        - Mocks the `get_rates` function to raise an exception.
        - Ensures the endpoint returns a 500 status code with an appropriate internal error message.

    Each test case uses Flask's `test_client` to make HTTP requests to the `/rates` endpoint, verifying that the application behaves correctly under different conditions.
    """
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
        """Test successful response with valid query parameters and mocked data."""
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
        """Test validation error response for missing or invalid query parameters."""
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
        """Test validation error response for an invalid date format in query parameters."""
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
        """Test validation error response for a missing required query parameter."""
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
        """Test internal server error response when `get_rates` raises an exception."""
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
