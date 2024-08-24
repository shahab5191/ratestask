DOCKER_COMPOSE = docker-compose
FLAKE8 = flake8
PYTEST = pytest

# Default to install
.PHONY: all
all: install

# Build and run containers
.PHONY:
install:
	@echo "Starting the server ..."
	$(DOCKER_COMPOSE) up --build -d
	@echo "Server is ready, go to http://localhost:5000/playground"

# Remove containers and clean up
.PHONY: clean
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

# Check code quality
.PHONY:
test-all: install
	$(DOCKER_COMPOSE) run --rm web $(PYTEST)
	$(DOCKER_COMPOSE) run --rm web $(FLAKE8)
	$(MAKE) clean

# Run tests
.PHONY: test
test: install
	$(DOCKER_COMPOSE) run --rm web $(PYTEST)
	$(MAKE) clean

# Run flake8 linter
.PHONY: lint
lint: install
	$(DOCKER_COMPOSE) run --rm web $(FLAKE8)
	$(MAKE) clean
