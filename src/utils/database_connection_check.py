from loguru import logger
from src.database.connection import get_db_connection


def is_db_connection_healthy():
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
        return True
    except Exception as e:
        logger.error("Error checking database connection health:", e)
        return False
