from src.database.connection import execute_query
from src.utils.convert_to_dict import convert_to_dict
from src.rates.schema import RateQueryParams


def get_rates(params: RateQueryParams):
    """
    Retrieve rate data based on the provided query parameters.

    This function executes a complex SQL query to fetch the average price of rates 
    between specified origin and destination regions or ports within a given date range. 
    The query uses Common Table Expressions (CTEs) to recursively obtain sub-regions 
    for both origin and destination, and then aggregates price data from the `prices` table. 
    The results are returned as a list of daily average prices.

    The SQL query performs the following steps:
        1. `orig_sub_regions`: Recursively fetches all sub-regions of the origin region.
        2. `dest_sub_regions`: Recursively fetches all sub-regions of the destination region.
        3. `orig_ports`: Fetches the port codes for the origin.
        4. `dest_ports`: Fetches the port codes for the destination.
        5. `price_data`: Aggregates price data, calculating the average price per day, 
           if there are more than two prices available.
        6. Combines and orders the results by day.

    Args:
        params (RateQueryParams): An instance of `RateQueryParams` containing:
            - `date_from` (str): The start date for filtering prices (format: YYYY-MM-DD).
            - `date_to` (str): The end date for filtering prices (format: YYYY-MM-DD).
            - `origin` (str): The origin location code.
            - `destination` (str): The destination location code.

    Returns:
        List[dict]: A list of dictionaries where each dictionary represents a day and contains:
            - `day` (str): The date.
            - `average_price` (float or None): The average price for that day, or `None` if 
              there are fewer than two prices available for that day.
    """ # noqa

    query = """
        WITH RECURSIVE orig_sub_regions AS (
            SELECT slug
            FROM regions
            WHERE slug = %(origin)s

            UNION ALL

            SELECT r.slug
            FROM regions r
            JOIN orig_sub_regions osr ON r.parent_slug = osr.slug
            WHERE r.slug IS NOT NULL
        ),
        dest_sub_regions AS (
            SELECT slug
            FROM regions
            WHERE slug = %(destination)s

            UNION ALL

            SELECT r.slug
            FROM regions r
            JOIN dest_sub_regions dsr ON r.parent_slug = dsr.slug
            WHERE r.slug IS NOT NONE
        ),
        orig_ports AS (
            SELECT code AS slug
            FROM ports
            WHERE ports.code = %(origin)s
        ),
        dest_ports AS (
            SELECT code AS slug
            FROM ports
            WHERE ports.code = %(destination)s
        ),
        price_data AS (
            SELECT
                p.day,
                round(AVG(p.price)) AS average_price
            FROM prices p
            JOIN ports orig ON orig.code = p.orig_code
            JOIN ports dest ON dest.code = p.dest_code
            WHERE (orig.parent_slug IN (SELECT * FROM orig_sub_regions)
                    OR orig.code IN (SELECT * FROM orig_ports))
            AND (dest.parent_slug IN (SELECT * FROM dest_sub_regions)
                OR dest.code IN (SELECT * FROM dest_ports))
            AND p.day <= %(date_to)s
            AND p.day >= %(date_from)s
            GROUP BY p.day
            HAVING COUNT(p.price) > 2
        )
        SELECT d.day, COALESCE(average_price, NULL) as average_price
        FROM generate_series(
                %(date_from)s::date,
                %(date_to)s::date,
                '1 day'::interval
            ) AS d(day)
        LEFT JOIN price_data pd
        ON d.day = pd.day
        ORDER BY d.day;
    """# noqa

    colnames, rows = execute_query(query, params.model_dump())

    rates = convert_to_dict(colnames, rows, date_format="%Y-%m-%d")
    return rates
