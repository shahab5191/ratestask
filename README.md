# About
This server is designated for the [xeneta.com](https://xeneta.com) assignment "RatesTask."

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

## Author
Shahab Oveysi
[oveysi.shahab@gmail.com](mailto:oveysi.shahab@gmail.com)
