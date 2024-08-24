import time
from loguru import logger
from src.config import Config


def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(Config.RETRY_MAX):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(
                    f"Error trying to establish database connection: {e}"
                )
                time.sleep(Config.RETRY_DELAY)
                logger.debug(f"Retrying database connection {i+1}")
        raise Exception(
            f"Could not establish a connection after {Config.RETRY_MAX} tries!"
        )
    return wrapper
