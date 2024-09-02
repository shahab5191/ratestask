```html










                   _____ _           _           _        ____                      _ 
                  / ____| |         | |         | |      / __ \                    (_)
                 | (___ | |__   __ _| |__   __ _| |__   | |  | |_   _____ _   _ ___ _ 
                  \___ \| '_ \ / _` | '_ \ / _` | '_ \  | |  | \ \ / / _ \ | | / __| |
                  ____) | | | | (_| | | | | (_| | |_) | | |__| |\ V /  __/ |_| \__ \ |
                 |_____/|_| |_|\__,_|_| |_|\__,_|_.__/   \____/  \_/ \___|\__, |___/_|
                                                                           __/ |      
                                                                          |___/       




                Email: oveysi.shahab@gmail.com

                Linkedin: linkedin.com/in/shahab-oveysi

                GitHub: github.com/shahab5191
```




---

```

     _            _                                  _      ___                       _               
    / \   ___ ___(_) __ _ _ __  _ __ ___   ___ _ __ | |_   / _ \__   _____ _ ____   _(_) _____      __
   / _ \ / __/ __| |/ _` | '_ \| '_ ` _ \ / _ \ '_ \| __| | | | \ \ / / _ \ '__\ \ / / |/ _ \ \ /\ / /
  / ___ \\__ \__ \ | (_| | | | | | | | | |  __/ | | | |_  | |_| |\ V /  __/ |   \ V /| |  __/\ V  V / 
 /_/   \_\___/___/_|\__, |_| |_|_| |_| |_|\___|_| |_|\__|  \___/  \_/ \___|_|    \_/ |_|\___| \_/\_/  
                    |___/                                                                             
```

## Objective:
> Develop an HTTP-based API using Python and SQL to calculate and return average daily prices between ports or regions based on given date ranges and port/region inputs.
```html

```
### 1. Data Provided:
```html
```
> - **Ports**:
    - 5-character port code
    - Port name
    - Region slug (indicating the region the port belongs to)
```html
```
> - **Regions**:
    - Hierarchical structure, regions can contain ports or other regions
    - Slug (machine-readable region name)
    - Region name
    - Parent region slug (for hierarchical relationships)
```html
```
> - **Prices**:
    - Daily prices between ports in USD
    - Origin and destination port codes (5-character)
    - Date of the price
    - Price in USD
---
```

     _            _                                  _      ___                       _               
    / \   ___ ___(_) __ _ _ __  _ __ ___   ___ _ __ | |_   / _ \__   _____ _ ____   _(_) _____      __
   / _ \ / __/ __| |/ _` | '_ \| '_ ` _ \ / _ \ '_ \| __| | | | \ \ / / _ \ '__\ \ / / |/ _ \ \ /\ / /
  / ___ \\__ \__ \ | (_| | | | | | | | | |  __/ | | | |_  | |_| |\ V /  __/ |   \ V /| |  __/\ V  V / 
 /_/   \_\___/___/_|\__, |_| |_|_| |_| |_|\___|_| |_|\__|  \___/  \_/ \___|_|    \_/ |_|\___| \_/\_/  
                    |___/                                                                             





                  ┼---------------------┼                  ┼---------------------┼      
                  |       regions       |                  |       ports         |      
                  |---------------------|                  |---------------------|      
                  |                     |                  |                     |      
            ----->| slug: text NOT NULL |<--------         | code: text NOT NULL |<----┐
            |     | name: text NOT NULL |         \        | name: text NOT NULL |     |
            ------| parent_slug text    |          \-------| parent_slug text    |     |
                  |                     |                  |                     |     |
                  ┼---------------------┼                  ┼---------------------┼     |
                                                                                       |
                                                                                       |
                                   ┼---------------------------┼                       |
                                   |       prices              |                       |
                                   |---------------------------|                       |
                                   |                           |                       |
                                   | orig_code: text NOT NULL  |-----------------------|
                                   | dest_code: text NOT NULL  |-----------------------┘
                                   | day: date NOT NULL        |                        
                                   | price: integer NOT NULL   |                        
                                   |                           |                        
                                   ┼---------------------------┼                        
```
---

```

     _            _                                  _      ___                       _               
    / \   ___ ___(_) __ _ _ __  _ __ ___   ___ _ __ | |_   / _ \__   _____ _ ____   _(_) _____      __
   / _ \ / __/ __| |/ _` | '_ \| '_ ` _ \ / _ \ '_ \| __| | | | \ \ / / _ \ '__\ \ / / |/ _ \ \ /\ / /
  / ___ \\__ \__ \ | (_| | | | | | | | | |  __/ | | | |_  | |_| |\ V /  __/ |   \ V /| |  __/\ V  V / 
 /_/   \_\___/___/_|\__, |_| |_|_| |_| |_|\___|_| |_|\__|  \___/  \_/ \___|_|    \_/ |_|\___| \_/\_/  
                    |___/                                                                             


```
### 2. Assignment Details:

- #### API Endpoint Requirements:
    - **Parameters**: date_from, date_to, origin, destination
    - **Output**: List of average daily prices for the specified route and date range.
    - **Edge Cases**: Return null for days with fewer than 3 price records.
    - **Flexibility**: The API should handle both port codes and region slugs for origin and destination parameters.
```html
```
- #### Key Evaluation Criteria:
    - Code clarity, organization, and simplicity
    - Ease of setup and testing
    - Proper error handling and edge case management
    - Use of raw SQL in addition to or instead of ORM
    - Comprehensive documentation (README.md)

### 3. Additional Notes:

- The task is expected to take 2-6 hours for an experienced developer.
- The solution should be version-controlled and easily clonable.
- Modifying the database schema is encouraged if it better suits the task.

---
```html
                             _    ____ ___   ____            _             
                            / \  |  _ \_ _| |  _ \  ___  ___(_) __ _ _ __  
                           / _ \ | |_) | |  | | | |/ _ \/ __| |/ _` | '_ \ 
                          / ___ \|  __/| |  | |_| |  __/\__ \ | (_| | | | |
                         /_/   \_\_|  |___| |____/ \___||___/_|\__, |_| |_|
                                                               |___/       

```

# Technologies & Tools:

- **Programming Language**:                     • **Framework**:
    | 󰌠  Python                                 |   Flask
- **Database**:                                 • **Containerization**:
    |   PostgreSQL (via psycopg2)              | 󰡨  Docker & Docker Compose
- **Testing**:                                  • **Linting**:
    | Pytest, Unittest                          | Flake8
- **Documentation**:                            • **Continuous Integration**:
    | Sphinx                                    |   GitHub Actions

```html

```

# Key Features:

- **Structured Documentation**:
    > Generated using Sphinx for easy navigation and understanding.
- **Automated CI/CD**:
    > Integrated with GitHub Actions to ensure code quality and automate testing.
- **Comprehensive Testing**:
    > Implemented with Pytest and Unittest to cover both unit and integration tests.

---
```html
                             _    ____ ___   ____            _             
                            / \  |  _ \_ _| |  _ \  ___  ___(_) __ _ _ __  
                           / _ \ | |_) | |  | | | |/ _ \/ __| |/ _` | '_ \ 
                          / ___ \|  __/| |  | |_| |  __/\__ \ | (_| | | | |
                         /_/   \_\_|  |___| |____/ \___||___/_|\__, |_| |_|
                                                               |___/       

```

# Modular Structure:
> Utilized Flask Blueprints for better structure management and modularity

```python
# rates/__init__.py
    from flask import Blueprint
    bp = Blueprint('rates', __name__)
    from src.rates import routes  # noqa: F401, E402

# rates/routes.py
    ...
    from src.rates import bp

    @bp.get(f"{Config.API_PREFIX}/rates")
    def rates_endpoint():
...


```

# File Tree:
```html
 db                                     Database sql file and dockerfile
├── 󱧊 docs                               Sphinx documentation source and build files
├── 󰣞 logs                               Loguru logs
├── 󰲂 src                                Source of API Application
│   ├── 󱋣 database                       Database connection creation and functions
│   ├── 󰉗 healthcheck                    Healthcheck route for API
│   ├── 󱞊 playground                     Simple frontend to check API
│   ├──  rates                          Rates Route to fetch data with GET method
│   ├── 󱧶 static                         Static resources for playground
│   ├── 󰉏 templates                      Playground html file
│   └── 󱁿 utils                          Utility function for data conversion, Retry decorator and ...
└── 󱥾 tests                              Tests for pytest and unittest
    ├── 󱥾 integration
    └── 󱥾 unit
```
---
```html
                      _____         _           _           _   ____       _     _       
                     |_   _|__  ___| |__  _ __ (_) ___ __ _| | |  _ \  ___| |__ | |_ ___ 
                       | |/ _ \/ __| '_ \| '_ \| |/ __/ _` | | | | | |/ _ \ '_ \| __/ __|
                       | |  __/ (__| | | | | | | | (_| (_| | | | |_| |  __/ |_) | |_\__ \
                       |_|\___|\___|_| |_|_| |_|_|\___\__,_|_| |____/ \___|_.__/ \__|___/
                                                                                         
```

1. **Centralized Logging Service**
> Currently, logs are stored within the logs folder inside the server container.
> This approach is not scalable or efficient for production environments. A centralized service should be implemented to manage, monitor, and store logs effectively.

2. **Databse Connection Pooling**
> A connection pool for the database was not implemented in this setup.
> While creating a new connection each time may suffice for testing and development, this approach could lead to performance issues in a production environment. Implementing connection pooling is recommended for scalability and efficiency.

3. **Limited Deployment Setup**
> The current setup is designed for testing and development purposes only. 
> For deployment, a more robust solution is needed, such as using serverless architecture or Kubernetes to
> handle scaling, orchestration, and maintenance.

4. **Route Organization**
> All API routes should be organized within the routes/ folder to maintain a clean and manageable project structure.

---

```
                              ____   ___  _        ___                        
                             / ___| / _ \| |      / _ \ _   _  ___ _ __ _   _ 
                             \___ \| | | | |     | | | | | | |/ _ \ '__| | | |
                              ___) | |_| | |___  | |_| | |_| |  __/ |  | |_| |
                             |____/ \__\_\_____|  \__\_\\__,_|\___|_|   \__, |
                                                                        |___/ 
```

# Current Strategy
> **Recursive Query Explanation**

## Objective:
- The goal of this query is to calculate the daily average prices between two specified regions (or ports) over a given time period.
- It also ensures that data is available for each day within the date range, even if no prices are recorded on certain days.
```html
```
## Steps:
### 1. Defining Sub-Regions
- **orig_sub_regions**:
    - This Common Table Expression (CTE) recursively gathers all sub-regions under the specified origin region.
    - It starts with the given origin (WHERE slug = %(origin)s), then continues to fetch all regions that have the origin as their parent.
```html
```
- **dest_sub_regions**:
    - Similarly, this CTE collects all sub-regions under the destination region using the same recursive approach.

### 2. Handling Ports
- **orig_ports:**
    - Identifies if the origin is a specific port rather than a region by checking the ports table.

- **dest_ports**:
    - Does the same for the destination, looking up the corresponding port code.
---
```
                              ____   ___  _        ___                        
                             / ___| / _ \| |      / _ \ _   _  ___ _ __ _   _ 
                             \___ \| | | | |     | | | | | | |/ _ \ '__| | | |
                              ___) | |_| | |___  | |_| | |_| |  __/ |  | |_| |
                             |____/ \__\_\_____|  \__\_\\__,_|\___|_|   \__, |
                                                                        |___/ 
```
## Steps:
### 3. Calculating Average Prices:
- **price_data:**
    - This part of the query calculates the average price for each day `(AVG(p.price)) from the prices table`.
    - It filters the data based on the `regions` and `ports` identified earlier.
    - It also filters by the specified date range `(p.day BETWEEN %(date_from)s AND %(date_to)s)`.
    - Prices are only considered if there are more than two records for that day `(HAVING COUNT(p.price) > 2)`.

### 4. Generating Date Series:
- **generate_series:**
    - This function creates a continuous series of dates within the specified range `(%(date_from)s to %(date_to)s)`.
    - This ensures that every day in the range is represented, even if no prices were recorded.

### 5. Final Selection:
- **Final Data Output:**
    - The final `SELECT` statement combines the date series with the price data.
    - It uses a `LEFT JOIN` to ensure all dates are included, and fills in missing prices with NULL if there were no records for that day.
    - The output is ordered by date.

---
```
                  ____            __                                                
                 |  _ \ ___ _ __ / _| ___  _ __ _ __ ___   __ _ _ __   ___ ___      
                 | |_) / _ \ '__| |_ / _ \| '__| '_ ` _ \ / _` | '_ \ / __/ _ \     
                 |  __/  __/ |  |  _| (_) | |  | | | | | | (_| | | | | (_|  __/     
                 |_|   \___|_|  |_|  \___/|_|  |_| |_| |_|\__,_|_| |_|\___\___|     
                   ____                _     _                _   _
                  / ___|___  _ __  ___(_) __| | ___ _ __ __ _| |_(_) ___  _ __  ___ 
                 | |   / _ \| '_ \/ __| |/ _` |/ _ \ '__/ _` | __| |/ _ \| '_ \/ __|
                 | |__| (_) | | | \__ \ | (_| |  __/ | | (_| | |_| | (_) | | | \__ \
                  \____\___/|_| |_|___/_|\__,_|\___|_|  \__,_|\__|_|\___/|_| |_|___/
                                                                                                      
```
# Objective

To enhance query performance by optimizing indexing strategies and proposing a denormalization approach, considering the limited write operations (only four times a day).

# Current Strategy

Given the low frequency of write operations, we can focus on optimizing read performance through indexing. To achieve this, I added several indexes to the rates.sql script:

```sql
CREATE INDEX idx_ports_parent_slug ON ports(parent_slug);
CREATE INDEX idx_regions_parent_slug ON regions(parent_slug);
CREATE INDEX idx_prices_orig_code ON prices(orig_code);
CREATE INDEX idx_prices_dest_code ON prices(dest_code);
CREATE INDEX idx_prices_day ON prices(day);
CREATE INDEX idx_prices_orig_dest_day ON prices(orig_code, dest_code, day);

```
In addition, I implemented unique constraints to ensure data integrity:
```sql
ALTER TABLE ports
    ADD CONSTRAINT unique_code UNIQUE (code);

ALTER TABLE regions
    ADD CONSTRAINT unique_slug UNIQUE (slug);
```
---
```
                  ____            __                                                
                 |  _ \ ___ _ __ / _| ___  _ __ _ __ ___   __ _ _ __   ___ ___      
                 | |_) / _ \ '__| |_ / _ \| '__| '_ ` _ \ / _` | '_ \ / __/ _ \     
                 |  __/  __/ |  |  _| (_) | |  | | | | | | (_| | | | | (_|  __/     
                 |_|   \___|_|  |_|  \___/|_|  |_| |_| |_|\__,_|_| |_|\___\___|     
                   ____                _     _                _   _
                  / ___|___  _ __  ___(_) __| | ___ _ __ __ _| |_(_) ___  _ __  ___ 
                 | |   / _ \| '_ \/ __| |/ _` |/ _ \ '__/ _` | __| |/ _ \| '_ \/ __|
                 | |__| (_) | | | \__ \ | (_| |  __/ | | (_| | |_| | (_) | | | \__ \
                  \____\___/|_| |_|___/_|\__,_|\___|_|  \__,_|\__|_|\___/|_| |_|___/
                                                                                                      
```

# Performance Analysis
To evaluate the effectiveness of the indexing strategy, I compared the EXPLAIN results before and after adding the indexes. The results showed minimal impact on overall query costs:

- Before Indexes: Total cost ranged between `1509.03` and `1517.08`.
- After Indexes: Total cost ranged between `1509.34` and `1517.39`.

This slight increase suggests that, while indexing is important, it may not be sufficient alone to optimize this complex query.

---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
1. **De Normalization**
## Objective:
- Reduce the complexity of queries and improve performance by avoiding recursive CTEs.

## Approach:
1. **Materialized View Creation**:
    - A materialized view `region_ports` is created to list all ports for each region and its subregions.
    - This eliminates the need for recursive CTEs and multiple joins on `prices.orig_code` and `prices.dest_code`.
    - Because original tables (ports, regions) has FOREIGN KEY constraint data integrity is applied to this view too.
    
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
With following query, I created a MATERIALIZED VIEW to hold a list of all ports inside each region and its subregions
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
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
2. **Query Optimization:**
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
```
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
```sql
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
3. **Indexing**:
- Indexing `region_slug` on the materialized view for better performance.

```sql
    CREATE INDEX idx_region_ports_region_slug ON region_ports(region_slug);
```
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
## Results:
> after analyzing several times to average execution and planning time for this approach these are results:
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

---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
# Table Partitioning
## Objective:
- Improve performance of queries filtering by date on the large `prices` table.

## Approach:
- **Partitioning the Table**:
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
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
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
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
## Impact:
1. **Reduced I/O Operations:**

    - **Smaller Data Segments**: By partitioning a table, you break it into smaller, more manageable pieces. Each partition holds a subset of the data (e.g., data for a specific month or year).

    - **Targeted Scans**: When a query is executed, the database can limit its search to only the relevant partitions. For instance, if you query for data from January 2016, only the partition containing January 2016 data is scanned, not the entire table.

    - **Reduced Disk Access**: This targeted scanning reduces the number of disk pages that need to be read, minimizing the amount of data that must be loaded into memory and processed.
```
```
2. **Manageability and Maintenance:**

    - **Easier Data Management**: Partitioning makes it easier to manage data lifecycle events, such as archiving old data or purging obsolete records. You can drop or archive entire partitions without affecting the rest of the data.

    - **Simplified Backup and Restore**: Backing up and restoring individual partitions can be more manageable and quicker than dealing with a large table in its entirety.
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```
3. **Faster Query Times:**

    - **Improved Index Efficiency**: Indexes on partitioned tables are smaller and more efficient because they only index data within each partition. This makes index searches faster.

    - **Parallel Processing**: Some databases support parallel processing across partitions. This means that multiple partitions can be scanned simultaneously, speeding up query execution.

    - **Efficient Maintenance**: Maintenance operations such as vacuuming, analyzing, or backing up are more efficient when applied to smaller partitions rather than a massive table. This results in less downtime and quicker maintenance processes.
---
```
                      _____           _   _                                    
                     |  ___|   _ _ __| |_| |__  _   _ _ __                     
                     | |_ | | | | '__| __| '_ \| | | | '__|                    
                     |  _|| |_| | |  | |_| | | | |_| | |                       
                     |_|   \__,_|_|   \__|_| |_|\__,_|_|             
                       __         _   _           _          _   _
                      / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __  
                     | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \ 
                     | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | |
                      \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|
                           |_|                                                 
```

## Results:
1. As data in the prices table grows, I observed a significant increase in query execution time. The table's performance started to degrade, making it evident that a more efficient data management strategy was needed:
    - Planning Time: **0.797 ms**
    - Execution Time: **10.446 ms**
```
```
2. After implementing partitioning on the prices table, query execution time was drastically reduced. The execution time dropped from 10.446 ms to 5.727 ms, nearly halving the time required to retrieve data. This demonstrates the effectiveness of partitioning in optimizing query performance, especially as the dataset scales: 
    - Planning Time: **0.920 ms**
    - Execution Time: **5.727 ms**
---
```
                      ____       _             _   _       _                              
                     |  _ \ ___ | |_ ___ _ __ | |_(_) __ _| |                             
                     | |_) / _ \| __/ _ \ '_ \| __| |/ _` | |                             
                     |  __/ (_) | ||  __/ | | | |_| | (_| | |                             
                     |_|   \___/ \__\___|_| |_|\__|_|\__,_|_|
                      _____       _                                               _
                     | ____|_ __ | |__   __ _ _ __   ___ ___ _ __ ___   ___ _ __ | |_ ___ 
                     |  _| | '_ \| '_ \ / _` | '_ \ / __/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
                     | |___| | | | | | | (_| | | | | (_|  __/ | | | | |  __/ | | | |_\__ \
                     |_____|_| |_|_| |_|\__,_|_| |_|\___\___|_| |_| |_|\___|_| |_|\__|___/

```
# Query Caching
- **In-Memory Caching**
> Implement caching mechanisms like Redis or Memcached to store the results of frequent queries, reducing database load and speeding up response times.

- **Database Query Caching**
> Leverage built-in database query caching for expensive queries to avoid recalculating the same results repeatedly.

# Scalability Enhancements
- **Database Sharding**
> Introduce sharding to distribute data across multiple databases, enhancing scalability and ensuring that the system can handle a growing amount of data and traffic.
- **Load Balancing**
> Implement load balancing strategies for handling increased traffic, ensuring that the system remains responsive under heavy load.
---
```













                      _____ _                 _                           __             
                     |_   _| |__   __ _ _ __ | | __  _   _  ___  _   _   / _| ___  _ __  
                       | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | |_ / _ \| '__| 
                       | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |  _| (_) | |    
                       |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_|  \___/|_|    
                                                     |___/             _   _             
                      _   _  ___  _   _ _ __    __ _| |_| |_ ___ _ __ | |_(_) ___  _ __  
                     | | | |/ _ \| | | | '__|  / _` | __| __/ _ \ '_ \| __| |/ _ \| '_ \ 
                     | |_| | (_) | |_| | |    | (_| | |_| ||  __/ | | | |_| | (_) | | | |
                      \__, |\___/ \__,_|_|     \__,_|\__|\__\___|_| |_|\__|_|\___/|_| |_|
                      |___/

                                I'm now open to any questions you might have.
```
