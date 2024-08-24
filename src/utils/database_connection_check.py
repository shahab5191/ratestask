from loguru import logger
from src.database.connection import get_db_connection


def is_db_connection_healthy():
    try:
        logger.debug("Checking database connection health")
        conn = get_db_connection()
        logger.debug("Database connection object created")
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        logger.debug("Query run on database successfully")
        conn.close()
        logger.debug("Database connection closed successfully!")
        return True
    except Exception as e:
        logger.error("Error checking database connection health:", e)
        return False
