import datetime
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger


def convert_to_dict(
    colnames: Optional[List[str]],
    rows: Optional[List[Tuple[Any, ...]]],
    date_format: Optional[str] = None,
) -> List[Dict[str, str]]:
    """
    Convert database query results into a list of dictionaries.

    This function transforms the result of a database query, where `colnames` represent 
    the column names and `rows` represent the data rows, into a list of dictionaries. 
    Each dictionary maps column names to their corresponding values in each row.

    Args:
        colnames (Optional[List[str]]): A list of column names. If `None`, no conversion 
                                     is performed.
        rows (Optional[Tuple[str]]): A tuple of rows, where each row is a tuple of column 
                                  values. If `None`, no conversion is performed.
        date_format (Optional[str]): An string containing formatting for date objects
                                    returned from database. if None, it will not format dates

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary represents 
                              a row of data with column names as keys and row values 
                              as values. Returns an empty list if `colnames` or `rows` 
                              is `None`.
    """ # noqa

    logger.debug("Converting data to dict format")
    if rows is None or colnames is None:
        logger.debug("Either row or colnames are empty. returning empty arary")
        return []

    data = []
    for row in rows:
        validated_row = []
        if date_format:
            for item in row:
                if isinstance(item, (datetime.datetime, datetime.date)):
                    validated_row.append(item.strftime(date_format))
                else:
                    validated_row.append(item)
        else:
            validated_row = row
        data.append(dict(zip(colnames, validated_row)))

    return data
