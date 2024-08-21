DOCKER_COMPOSE = docker-compose
FLAKE8 = flake8
PYTEST = pytest

# Default to install
.PHONY: all
all: install

# Build and run containers
.PHONY: install
install:
	$(DOCKER_COMPOSE) up --build -d

# Remove containers and clean up
.PHONY: clean
clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

# Run tests
.PHONY: test
test:
	$(DOCKER_COMPOSE) run --rm web $(PYTEST) test/

# Run flake8 linter
.PHONY: lint
lint:
	$(FLAKE8) .
