from typing import Dict
import unittest
from unittest.mock import patch

from src.healthcheck.routes import healthcheck

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.is_db_connection_healthy = patch(
                "src.healthcheck.routes.is_db_connection_healthy"
            ).start()

    def test_db_healthy(self):
        """Test healthy response when the database connection is healthy."""

        self.is_db_connection_healthy.return_value = True

        result, status = healthcheck()
        assert isinstance(result, Dict)
        self.assertDictEqual(result, {
            "status": "healthy"
        })
        self.assertEqual(status, 200)

    def test_db_unhealthy(self):
        """Test unhealthy response when the database connection is unhealthy."""

        self.is_db_connection_healthy.return_value = False

        result, status = healthcheck()
        assert isinstance(result, Dict)
        self.assertDictEqual(result, {
            "status": "unhealthy"
        })
        self.assertEqual(status, 503)

    def test_db_unhealthy_with_exception(self):
        """Test unhealthy response and exception handling for database connection errors."""

        self.is_db_connection_healthy.side_effect = Exception("error")
        with self.assertRaises(Exception):
            result, status = healthcheck()
            assert isinstance(result, Dict)
            self.assertDictEqual(result, {
                "status": "unhealthy"
            })
            self.assertEqual(status, 500)
