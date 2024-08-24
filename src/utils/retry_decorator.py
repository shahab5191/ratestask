import time
from loguru import logger
from src.config import Config


def retry(func):
    """
    A decorator to retry a function multiple times if it raises an exception.

    This decorator retries the execution of the decorated function up to a maximum number of attempts 
    specified by `Config.RETRY_MAX`. If an exception is raised during the execution, it logs the error 
    and retries after a delay specified by `Config.RETRY_DELAY`. If all attempts fail, it raises an 
    exception indicating that the function could not be executed successfully.

    Args:
        func (Callable): The function to be decorated and retried.

    Returns:
        Callable: The decorated function with retry logic.

    Raises:
        Exception: If the function fails to execute successfully after the maximum number of retries.

    Example:
        @retry
        def connect_to_database():
            # Function implementation here

        connect_to_database()
    """
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
