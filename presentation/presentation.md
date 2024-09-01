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
                             _    ____ ___   ____            _             
                            / \  |  _ \_ _| |  _ \  ___  ___(_) __ _ _ __  
                           / _ \ | |_) | |  | | | |/ _ \/ __| |/ _` | '_ \ 
                          / ___ \|  __/| |  | |_| |  __/\__ \ | (_| | | | |
                         /_/   \_\_|  |___| |____/ \___||___/_|\__, |_| |_|
                                                               |___/       

```

# Technical debts


