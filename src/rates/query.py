from src.database.connection import execute_query
from src.database.convert_to_dict import convert_to_dict
from src.rates.schema import RateQueryParams


def get_rates(params: RateQueryParams):
    query = """
        WITH RECURSIVE orig_sub_regions AS (
            SELECT slug
            FROM regions
            WHERE slug = %(origin)s

            UNION ALL

            SELECT r.slug
            FROM regions r
            JOIN orig_sub_regions osr ON r.parent_slug = osr.slug
        ),
        dest_sub_regions AS (
            SELECT slug
            FROM regions
            WHERE slug = %(destination)s

            UNION ALL

            SELECT r.slug
            FROM regions r
            JOIN dest_sub_regions dsr ON r.parent_slug = dsr.slug
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
                (CASE WHEN COUNT(p.price) > 2 THEN round(AVG(p.price), 2) ELSE NULL END) AS average_price
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
        )
        SELECT d.day, average_price
        FROM price_data pd
        RIGHT JOIN (
            SELECT date::date AS day
            FROM generate_series(
                %(date_from)s::date,
                %(date_to)s::date,
                '1 day'::interval
            ) AS date
        ) d ON d.day = pd.day
        ORDER BY d.day;
    """# noqa

    colnames, rows = execute_query(query, params.model_dump())

    rates = convert_to_dict(colnames, rows)
    return rates
