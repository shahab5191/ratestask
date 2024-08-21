import os
import psycopg2
from dotenv import load_dotenv

from src.config import Config


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(basedir, '.env'))


def get_db_connection():
    """Establish and return a database connection"""
    print(Config().DATABASE_CONFIG)
    conn = psycopg2.connect(**Config().DATABASE_CONFIG)
    return conn


def execute_query(query, params=None):
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
