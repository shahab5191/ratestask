import os
import psycopg2
from dotenv import load_dotenv

from src.config import Config


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))


def get_db_connection():
    """
    Establish and return a connection to the database.

    This function uses the database configuration specified in the `Config` class to 
    create a connection to the PostgreSQL database. The connection object is used for 
    executing queries and interacting with the database.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
    """
    conn = psycopg2.connect(**Config().DATABASE_CONFIG)
    return conn


def execute_query(query, params=None):
    """
    Execute a SQL query and return the results.

    This function establishes a connection to the database, executes the provided SQL 
    query with optional parameters, and fetches the results. It returns both the column 
    names and the rows of the result set.

    Args:
        query (str): The SQL query to be executed.
        params (tuple, list, or None): Optional parameters to be used with the query. 
                                        Defaults to None.

    Returns:
        tuple: A tuple containing two elements:
            - A list of column names (`list` of `str`).
            - A list of rows (`list` of `tuple`), where each row is a tuple of column values.

    Raises:
        Exception: Any exception raised during query execution or connection handling 
                   is caught and printed, but the function does not raise it further.
    """
    conn = get_db_connection()
    rows = None
    colnames = None
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)

            if cur.description:
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    return colnames, rows
