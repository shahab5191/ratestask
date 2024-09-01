WHERE clause on price_data CTE is expensive because it is a sequential scan over all rows
to mitigate this bottle neck we can partition table by range on year


## Denormalization:
Created a MATERIALIZED VIEW listing all the ports belonging to each region and its subregions
this way we don't need RECURSIVE CTE

```sql
CREATE MATERIALIZED VIEW region_ports AS
WITH RECURSIVE region_hierarchy AS (
    SELECT
        r.slug AS region_slug,
        r.slug AS root_slug
    FROM
        regions r

    UNION ALL

    SELECT
        r.slug AS region_slug,
        rh.root_slug AS root_slug
    FROM
        regions r
    JOIN
        region_hierarchy rh ON r.parent_slug = rh.region_slug
)
SELECT
    rh.root_slug AS region_slug,
    ARRAY_AGG(p.code ORDER BY p.code) FILTER (WHERE p.code IS NOT NULL) AS ports
FROM
    region_hierarchy rh
LEFT JOIN
    ports p ON rh.region_slug = p.parent_slug
GROUP BY
    rh.root_slug;
```

then each time we need to updating this table we can just refresh it:

```sql
REFRESH MATERIALIZED VIEW region_ports;
```

because original tables (ports, regions) has FOREIGN KEY constraint data integrity is applied to this view too.

Now we can query without RECURSIVE CTE:

```sql
    WITH origin_ports_list as (
        SELECT
            unnest(ports) as port
        FROM region_ports
        WHERE region_ports.region_slug = 'china_main'

        UNION ALL
        
        SELECT
            code as port
        FROM ports
        WHERE ports.code = 'china_main'

    ),
    destination_ports_list as (
        SELECT
            unnest(ports) as port
        from region_ports
        where region_ports.region_slug = 'uk_main'

        UNION ALL
        
        SELECT
            code as port
        from ports
        WHERE ports.code = 'uk_main'
    ),
    prices_list as (
        SELECT pr."day", ROUND(AVG(pr.price), 2) as average_price
        FROM prices pr
        WHERE 
            pr.orig_code IN (select port from origin_ports_list)
        AND
            pr.dest_code IN (select port from destination_ports_list)
        AND
            pr."day" >= '2016-01-01'
        and 
            pr."day" <= '2016-01-30'
        GROUP BY pr."day"
        HAVING COUNT(*) > 2
        ORDER BY DAY
    )
    SELECT to_char(d.day, 'yyyy-mm-dd') as day, COALESCE(average_price, NULL) as average_price
    FROM generate_series(
            '2016-01-01'::date,
            '2016-01-16'::date,
            '1 day'::interval
        ) AS d(day)
    LEFT JOIN prices_list pd
    ON d.day = pd.day
    ORDER BY d.day;
```

to further optimizing we can index region_slug on this view:

```sql
CREATE INDEX idx_region_ports_region_slug ON region_ports(region_slug);
```

this index can improve performance because we are filtering our CTE's by this column

|    INITIAL PLAN      |  DE NORMALIZATION   | DE NORMALIZATION with INDEX |
|----------|-----------|---------|-----------|--------------|--------------|
| Planning | execution | planing | execution | planing      | execution    |
|----------|-----------|---------|-----------|--------------|--------------|
| 1.10     | 6.14      | 0.52    | 5.06      | 0.80         | 5.13         |
| 1.11     | 7.87      | 0.74    | 7.12      | 0.79         | 7.25         |
| 1.07     | 5.86      | 0.52    | 4.55      | 0.93         | 7.43         |
| 0.77     | 5.76      | 0.78    | 7.32      | 0.53         | 4.75         |
| 1.03     | 5.90      | 0.50    | 4.81      | 0.79         | 5.02         |
| 1.05     | 8.42      | 0.50    | 4.72      | 0.50         | 4.61         |
| 0.76     | 5.87      | 0.77    | 7.19      | 0.52         | 4.86         |
|----------|-----------|---------|-----------|--------------|--------------|
| 0.98     | 6.55      | 0.62    | 5.82      | 0.69         | 5.58         |


after analyzing several times to average execution and planning time for this approach these are results:
Both execution time and planning time for query are reduced.

