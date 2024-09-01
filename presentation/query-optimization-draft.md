# Query Optimization Strategies
## 1. Denormalization:
### Objective:
- Reduce the complexity of queries and improve performance by avoiding recursive CTEs.

### Approach:
1. Materialized View Creation:
    - A materialized view `region_ports` is created to list all ports for each region and its subregions.
    - This eliminates the need for recursive CTEs and multiple joins on `prices.orig_code` and `prices.dest_code`.
    - Because original tables (ports, regions) has FOREIGN KEY constraint data integrity is applied to this view too.

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

2. Refresh View:
    - then each time we need updating this table we can just refresh it:

    ```sql
        REFRESH MATERIALIZED VIEW region_ports;
    ```

3. Query Optimization:
    - Now we can query without RECURSIVE CTE:

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
                pr."day" >= '2016-01-01'
            AND 
                pr."day" <= '2016-01-30'
            AND
                pr.orig_code IN (select port from origin_ports_list)
            AND
                pr.dest_code IN (select port from destination_ports_list)
            GROUP BY pr."day"
            HAVING COUNT(*) > 2
        )
        SELECT to_char(d.day, 'yyyy-mm-dd') as day, COALESCE(average_price, NULL) as average_price
        FROM generate_series(
                '2016-01-01'::date,
                '2016-01-30'::date,
                '1 day'::interval
            ) AS d(day)
        LEFT JOIN prices_list pd
        ON d.day = pd.day;
    ```
4. Indexing:
    - Indexing `region_slug` on the materialized view for better performance.

    ```sql
        CREATE INDEX idx_region_ports_region_slug ON region_ports(region_slug);
    ```

### Results:

after analyzing several times to average execution and planning time for this approach these are results:
Both execution time and planning time for query are reduced.

| INITIAL PLAN  |                   | DE NORMALIZATION |        | DE NORMALIZATION with INDEX | |
|---------------|-------------------|----------------|-----------|----------------|-----------|
| Planning      |   execution       |   planning     | execution |    planning    | execution |
| 1.10          | 6.14              | 0.52           | 5.06      | 0.80           | 5.13      |
| 1.11          | 7.87              | 0.74           | 7.12      | 0.79           | 7.25      |
| 1.07          | 5.86              | 0.52           | 4.55      | 0.93           | 7.43      |
| 0.77          | 5.76              | 0.78           | 7.32      | 0.53           | 4.75      |
| 1.03          | 5.90              | 0.50           | 4.81      | 0.79           | 5.02      |
| 1.05          | 8.42              | 0.50           | 4.72      | 0.50           | 4.61      |
| 0.76          | 5.87              | 0.77           | 7.19      | 0.52           | 4.86      |
|               |                   |                |           |                |           |
| 0.98          | 6.55              | 0.62           | 5.82      | 0.69           | 5.58      |

## Table Partitioning

### Objective:
- Improve performance of queries filtering by date on the large `prices` table.

### Approach:
1. Partitioning the Table:
    - Partition the `prices` table by date to optimize query performance and manageability

    ```sql
        CREATE TABLE prices (
            day DATE NOT NULL,
            orig_code TEXT,
            dest_code TEXT,
            price NUMERIC,
            PRIMARY KEY (day, orig_code, dest_code)
        ) PARTITION BY RANGE (day);

        CREATE TABLE prices_2016_01 PARTITION OF prices
            FOR VALUES FROM ('2016-01-01') TO ('2016-02-01');
    ```

    - Consider further partitions for each month or season depending on data volume and query patterns.

    - To test this approach we can generate fake data by duplicating available data and changing its date to 2nd month of 2016:

    ```sql
        INSERT INTO prices (orig_code, dest_code, day, price)
        SELECT
            orig_code,
            dest_code,
            REPLACE(day::text, '2016-01-', '2016-02-')::date AS day,
            price
        FROM prices
        WHERE day >= '2016-01-01' AND day < '2016-01-29';
    ```

    - by creating more data now query execution time increases to 7.1ms without partitioning.
    
    - After Partitioning tables we need to remove `ONLY` keyword when adding `FOREIGN KEY` constraint to `prices` table to let it apply to its partitions.


### Impact:
1. Reduced I/O Operations:

    - **Smaller Data Segments**: By partitioning a table, you break it into smaller, more manageable pieces. Each partition holds a subset of the data (e.g., data for a specific month or year).

    - **Targeted Scans**: When a query is executed, the database can limit its search to only the relevant partitions. For instance, if you query for data from January 2016, only the partition containing January 2016 data is scanned, not the entire table.

    - **Reduced Disk Access**: This targeted scanning reduces the number of disk pages that need to be read, minimizing the amount of data that must be loaded into memory and processed.

2. Faster Query Times:

    - **Improved Index Efficiency**: Indexes on partitioned tables are smaller and more efficient because they only index data within each partition. This makes index searches faster.

    - **Parallel Processing**: Some databases support parallel processing across partitions. This means that multiple partitions can be scanned simultaneously, speeding up query execution.

    - **Efficient Maintenance**: Maintenance operations such as vacuuming, analyzing, or backing up are more efficient when applied to smaller partitions rather than a massive table. This results in less downtime and quicker maintenance processes.

3. Manageability and Maintenance:

    - **Easier Data Management**: Partitioning makes it easier to manage data lifecycle events, such as archiving old data or purging obsolete records. You can drop or archive entire partitions without affecting the rest of the data.

    - **Simplified Backup and Restore**: Backing up and restoring individual partitions can be more manageable and quicker than dealing with a large table in its entirety.

### Results:
1. As data in the prices table grows, I observed a significant increase in query execution time. The table's performance started to degrade, making it evident that a more efficient data management strategy was needed:
    - Planning Time: 0.797 ms
    - Execution Time: 10.446 ms
2. After implementing partitioning on the prices table, query execution time was drastically reduced. The execution time dropped from 10.446 ms to 5.727 ms, nearly halving the time required to retrieve data. This demonstrates the effectiveness of partitioning in optimizing query performance, especially as the dataset scales:    
    - Planning Time: 0.920 ms
    - Execution Time: 5.727 ms

