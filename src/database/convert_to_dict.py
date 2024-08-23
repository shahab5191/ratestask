import datetime
from typing import Dict, List, Tuple


def convert_to_dict(
    colnames: List[str] | None,
    rows: Tuple[str] | None,
    date_format: str | None,
) -> List[Dict[str, str]]:
    """
    Convert database query results into a list of dictionaries.

    This function transforms the result of a database query, where `colnames` represent 
    the column names and `rows` represent the data rows, into a list of dictionaries. 
    Each dictionary maps column names to their corresponding values in each row.

    Args:
        colnames (List[str] | None): A list of column names. If `None`, no conversion 
                                     is performed.
        rows (Tuple[str] | None): A tuple of rows, where each row is a tuple of column 
                                  values. If `None`, no conversion is performed.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary represents 
                              a row of data with column names as keys and row values 
                              as values. Returns an empty list if `colnames` or `rows` 
                              is `None`.
    """ # noqa
    if rows is None or colnames is None:
        return []

    data = []
    for row in rows:
        validated_row = []
        if date_format:
            for item in row:
                if isinstance(item, datetime.date):
                    validated_row.append(item.strftime(date_format))
                else:
                    validated_row.append(item)
        else:
            validated_row = row
        data.append(dict(zip(colnames, validated_row)))

    return data
