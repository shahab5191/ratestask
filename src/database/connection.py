import os
from typing import Any, List, Optional, Tuple
from loguru import logger
import psycopg2
from dotenv import load_dotenv

from src.config import Config
from src.utils.retry_decorator import retry


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))


@retry
def get_db_connection():
    """
    Establish and return a connection to the database.

    This function uses the database configuration specified in the `Config` class to 
    create a connection to the PostgreSQL database. The connection object is used for 
    executing queries and interacting with the database.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
    """ # noqa
    logger.debug("Creating new database connection...")
    conn = psycopg2.connect(**Config().DATABASE_CONFIG)
    logger.debug("Database connection created")
    return conn


def execute_query(
    query,
    params=None
) -> Tuple[Optional[List[str]], Optional[List[Any]]]:
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
    """ # noqa

    logger.debug("Execute query requested")
    conn = get_db_connection()
    rows = None
    colnames = None
    try:
        logger.debug("Executing query...")
        with conn.cursor() as cur:
            cur.execute(query, params)

            if cur.description:
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
            else:
                logger.warning("No description found in query result")
    except Exception as e:
        logger.error(f"Database error: {e}")
    finally:
        logger.debug("Closing database connection")
        conn.close()
        logger.debug("Connection closed successfully")
    return colnames, rows
