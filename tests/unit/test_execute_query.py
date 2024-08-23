import unittest
from unittest.mock import MagicMock, patch

from src.database.connection import execute_query


class TestExecuteQuery(unittest.TestCase):
    def setUp(self):
        self.mock_get_db_connection = patch(
            "src.database.connection.get_db_connection"
        ).start()
        self.mock_conn = MagicMock()
        self.mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value.__enter__.return_value = self.mock_cursor
        self.query = "SELECT * from regions"

    def test_execute_query_success(self):

        self.mock_cursor.description = [('slug',), ('name',), ('parent_slug',)]
        self.mock_cursor.fetchall.return_value = [
            (1, 'test'),
            (2, 'test'),
            (3, 'test')
        ]
        
        colnames, rows = execute_query(self.query)
        self.assertEqual(colnames, ['slug', 'name', 'parent_slug'])
        self.assertEqual(rows, [
            (1, 'test'),
            (2, 'test'),
            (3, 'test')
        ])

    def test_execute_query_exception(self):
        self.mock_cursor.execute.side_effect = Exception("Database error:")

        colnames, rows = execute_query(self.query)

        self.assertIsNone(colnames)
        self.assertIsNone(rows)

    def test_execute_query_empty_result(self):
        self.mock_cursor.description = [('slug',), ('name',), ('parent_name',)]
        self.mock_cursor.fetchall.return_value = []

        colnames, rows = execute_query(self.query)

        self.assertEqual(colnames, ['slug', 'name', 'parent_name'])
        self.assertEqual(rows, [])
