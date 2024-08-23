# About
This server is designated for the [xeneta.com](https://xeneta.com) assignment "RatesTask."

For more information about the API and functions, please visit the [Documentaion](https://shahab5191.github.io/ratestask).
## Getting Started

Welcome to Rates Task! Here\'s how to get started:

1.  **Install Docker**

    Follow the Docker documentation to install Docker. You can use
    either Docker Engine or Docker Desktop. You should also install
    Docker Compose for building and running the database and server
    together.

    [Docker Engine installation
    document](https://docs.docker.com/engine/install/)

2.  **Run Tests and Lint**

    First, run Tests and Linter to make sure everything works fine.

    If you are using Unix-based operating systems, you can use \`make\`:

    ``` bash
    make lint
    make tests
    ```

    On Windows, you can use Docker Compose:

    ``` bash
    docker-compose run --rm web pytest
    docker-compose down --volumes --remove-orphans

    # AND

    docker-compose run --rm web flake8
    docker-compose down --volumes --remove-orphans
    ```

3.  **Run Server and Database**

    Then you can build Docker containers and run them.

    On Unix-based systems:

    ``` bash
    make all
    # or
    make install
    ```

    On Windows:

    ``` bash
    docker-compose up --build -d
    ```

4.  **Send Request**

    Now you can send HTTP requests to the server.

     **Request Example**

    -   **URL:** [/v1/rates](.title-ref)

    -   **METHOD:** GET

    -   **PARAMS:**

        -   date_to
        -   date_from
        -   origin
        -   destination

    -   **RESULT:**

        -   Array of average_price and
            day ([yyyy-mm-dd])


    > **_NOTE:_** When running the server, wait for a couple of seconds
    before sending requests because it takes time for the database
    container to get ready for receiving requests.

## Technical debts
You can read about the technical debts and current state of the project [here](technical-debt.md)

## Proposal for Query Optimization: Leveraging Indexing and Denormalization
You can read this part in document format [here](https://shahab5191.github.io/ratestask/optimization.html)

### Objective
To enhance query performance by optimizing indexing strategies and proposing a denormalization approach, considering the limited write operations (only four times a day).

### Current Strategy
Given the low frequency of write operations, we can focus on optimizing read performance through indexing. To achieve this, I added several indexes to the `rates.sql` script:

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

### Proposed Denormalization
To further optimize performance, I propose denormalizing the data instead of relying on recursive queries to compile sub-regions for each requested region. The new `regions` table structure would be:

```sql
CREATE TABLE regions (
    slug text NOT NULL,
    name text NOT NULL,
    parent_slug text,
    port_codes text[]
);
```

### Example Query Using Denormalization
With the denormalized structure, we can simplify the process of retrieving all ports within a region without the need for recursion:

```sql
WITH port_codes AS (
    SELECT DISTINCT unnest(r.port_codes)
    FROM regions AS r
    WHERE r.slug = 'GBSOU'

    UNION ALL

    SELECT p.code
    FROM ports p
    WHERE p.code = 'GBSOU'
)
SELECT * FROM port_codes;
```

This query effectively lists all ports in the specified region, including sub-regions, and then allows us to calculate the average price per day for all identified ports. The `UNION ALL` operation with `ports.code` ensures that the query returns the correct result, even if a port code is entered instead of a region name.

### Advantages
- **Improved Performance:** Reduces the need for expensive recursive queries, lowering computational costs.
- **Simplified Query Structure:** Makes queries more straightforward and easier to maintain.

### Drawbacks
- **Data Maintenance:** This approach requires updating the `regions` table whenever a new port or sub-region is added. However, such updates are infrequent, making this a manageable concern.

### Performance Analysis
To evaluate the effectiveness of the indexing strategy, I compared the `EXPLAIN` results before and after adding the indexes. The results showed minimal impact on overall query costs:

- **Before Indexes:** Total cost ranged between 1509.03 and 1517.08.
- **After Indexes:** Total cost ranged between 1509.34 and 1517.39.

This slight increase suggests that, while indexing is important, it may not be sufficient alone to optimize this complex query.

### Conclusion
Given the limited impact of indexing on query performance, the best approach for optimizing these complex queries is through denormalization and data redundancy. This strategy will significantly reduce the need for recursive operations and improve overall query efficiency.


## Author
Shahab Oveysi
[oveysi.shahab@gmail.com](mailto:oveysi.shahab@gmail.com)
