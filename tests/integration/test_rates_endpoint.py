from typing import Dict, List

from src.config import Config
from tests.utils.data_is_empty import is_empty


def test_unsuccessful_empty_args(client):
    """Test that missing query parameters return a 400 error with an error message."""

    response = client.get(f'{Config.API_PREFIX}/rates')

    assert response.status_code == 400
    result = response.json
    assert result is not None
    assert isinstance(result, Dict)
    assert "error" in result
    assert result["error"] == "query parameters are not valid!"


def test_successfull_empty_data(client):
    """Test valid parameters result in an filled rates list with null average_price when no data is available."""

    params = {
        "date_from": "2016-01-01",
        "date_to": "2016-01-30",
        "origin": "uk_main",
        "destination": "scandinavia"
    }
    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert is_empty(rates)


def test_successfull_available_data_port_port(client):
    """Test valid port-to-port parameters return correct data for a specific route."""

    params = {
        "date_from": "2016-01-01",
        "date_to": "2016-01-02",
        "origin": "CNCWN",
        "destination": "NOOSL"
    }

    expected_result = {
        "day": "2016-01-01",
        "average_prices": "1807.33"
    }

    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert rates[0]['day'] == expected_result["day"]
    assert rates[0]['average_price'] == expected_result["average_prices"]


def test_successfull_available_data_region_port(client):
    """Test valid region-to-port parameters return correct data for a specific route."""

    params = {
        "date_from": "2016-01-01",
        "date_to": "2016-01-02",
        "origin": "china_main",
        "destination": "NOOSL"
    }

    expected_result = {
        "day": "2016-01-01",
        "average_prices": "1708.29"
    }

    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert rates[0]['day'] == expected_result["day"]
    assert rates[0]['average_price'] == expected_result["average_prices"]


def test_successfull_available_data_port_region(client):
    """Test valid port-to-region parameters return correct data for a specific route."""

    params = {
        "date_from": "2016-01-01",
        "date_to": "2016-01-02",
        "origin": "CNGGZ",
        "destination": "uk_main"
    }

    expected_result = {
        "day": "2016-01-01",
        "average_prices": "1480.83"
    }

    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert rates[0]['day'] == expected_result["day"]
    assert rates[0]['average_price'] == expected_result["average_prices"]


def test_successfull_available_data_region_region(client):
    """Test valid region-to-region parameters return correct data for a specific route."""

    params = {
        "date_from": "2016-01-01",
        "date_to": "2016-01-02",
        "origin": "china_main",
        "destination": "uk_main"
    }

    expected_result = {
        "day": "2016-01-01",
        "average_prices": "1245.70"
    }

    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert rates[0]['day'] == expected_result["day"]
    assert rates[0]['average_price'] == expected_result["average_prices"]


def test_successfull_available_data_less_than_two_data(client):
    """Test valid region-to-region parameters return correct data for a specific route."""

    params = {
        "date_from": "2016-01-04",
        "date_to": "2016-01-04",
        "origin": "china_main",
        "destination": "uk_main"
    }

    expected_result = {
        "day": "2016-01-04",
        "average_prices": None
    }

    response = client.get(f'{Config.API_PREFIX}/rates', query_string=params)
    result = response.json
    assert result is not None
    rates = result.get("rates")
    assert rates is not None
    assert isinstance(rates, List)
    assert rates[0]['day'] == expected_result["day"]
    assert rates[0]['average_price'] == expected_result["average_prices"]
