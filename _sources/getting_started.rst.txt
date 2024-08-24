Getting Started
===============

Welcome to Rates Task! Here's how to get started:

1. **Install Docker**

   Follow the Docker documentation to install Docker. You can use either Docker Engine or Docker Desktop.
   You should also install Docker Compose for building and running the database and server together.

   `Docker Engine installation document <https://docs.docker.com/engine/install/>`_

2. **Clone Repository**
   First clone this repository:

   .. code-block:: bash

       git clone https://github.com/shahab5191/ratestask

3. **Set Environment Variables**
   You can either create `.env` file like `.env-example` file.

   Or set environment variables in your terminal.

   On linux you can use this command:
    
   .. code-block:: bash

       export DB_USER="username for database"
       export DB_PASSWORD="password for database"

   Or on windows:

   .. code-block:: powershell

       $env:DB_USER = "username for database"
       $env:DB_PASSWORD = "password for database"

4. **Run Tests and Lint**

   First, run Tests and Linter to make sure everything works fine.

   If you are using Unix-based operating systems, you can use `make`:

   .. code-block:: bash

      make lint
      make tests

   On Windows, you can use Docker Compose:

   .. code-block:: bash

      docker-compose run --rm web pytest
      docker-compose down --volumes --remove-orphans

      # AND

      docker-compose run --rm web flake8
      docker-compose down --volumes --remove-orphans

5. **Run Server and Database**

   Then you can build Docker containers and run them.

   On Unix-based systems:

   .. code-block:: bash

      make all
      # or
      make install

   On Windows:

   .. code-block:: bash

      docker-compose up --build -d

6. **Send Request**

   Now you can send HTTP requests to the server.

   **Request Example:**

   - **URL:** `/v1/rates`
   - **METHOD:** `GET`
   - **PARAMS:**
      - `date_to`
      - `date_from`
      - `origin`
      - `destination`
   - **RESULT:**
      - Array of `average_price` and `day` (`yyyy-mm-dd`)

   **Note:** When running the server, wait for a couple of seconds before sending requests because it takes time for the database container to get ready for receiving requests.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
