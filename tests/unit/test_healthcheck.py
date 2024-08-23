from typing import Dict, Tuple
import unittest
from unittest.mock import Mock, patch

from src.healthcheck.routes import healthcheck

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.is_db_connection_healthy = patch(
                "src.healthcheck.routes.is_db_connection_healthy"
            ).start()

    def test_db_healthy(self):
        self.is_db_connection_healthy.return_value = True

        result, status = healthcheck()
        assert isinstance(result, Dict)
        self.assertDictEqual(result, {
            "status": "healthy"
        })
        self.assertEqual(status, 200)

    def test_db_unhealthy(self):
        self.is_db_connection_healthy.return_value = False

        result, status = healthcheck()
        assert isinstance(result, Dict)
        self.assertDictEqual(result, {
            "status": "unhealthy"
        })
        self.assertEqual(status, 503)

    def test_db_unhealthy_with_exception(self):

        self.is_db_connection_healthy.side_effect = Exception("error")
        with self.assertRaises(Exception):
            result, status = healthcheck()
            assert isinstance(result, Dict)
            self.assertDictEqual(result, {
                "status": "unhealthy"
            })
            self.assertEqual(status, 500)
