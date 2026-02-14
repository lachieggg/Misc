# Restaurant Order System

A Django-based POS order processing system with a CLI interface. The project demonstrates proper separation of concerns with services, models, and CLI interfaces.

## Getting Started

### Initial Setup

Set up the virtual environment and install dependencies:

```bash
make setup
```

This creates a Python virtual environment and installs all dependencies from `requirements.txt`.

### Running the Application

Start the order processing CLI:

```bash
make run
```

This launches the interactive menu-driven order entry system.

### Testing & Code Quality

Run tests:

```bash
make test
```

Check code style:

```bash
make lint
```

Auto-format code:

```bash
make format
```

Fix linting issues automatically:

```bash
make lint-fix
```

Run all checks (format, fix, lint):

```bash
make lint-all
```

### Model Generation

The project uses [datamodel-codegen](https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/) (oapi) to generate Django models from the OpenAPI specification:

```bash
make apigen
```

This regenerates `ordersystem/pos/models.py` from `ordersystem/pos/openapi.yaml`.

### Cleanup

Remove cache files and build artifacts:

```bash
make clean
```

## Project Structure

### Key Files

- **`ordersystem/pos/models.py`** - Pydantic models generated from OpenAPI spec (auto-generated via `make apigen`)
- **`ordersystem/pos/services/menu_service.py`** - Loads and manages menu items from YAML configuration
- **`ordersystem/pos/services/order_service.py`** - Processes orders, groups items, and calculates totals with tax
- **`ordersystem/pos/interfaces/cli.py`** - Interactive CLI for taking orders
- **`ordersystem/pos/config/menu.yaml`** - Menu configuration (items and tax rate)
- **`ordersystem/pos/openapi.yaml`** - OpenAPI specification for model generation

### Architecture

The application follows a clean architecture pattern:

- **Models** - Data structures (auto-generated from OpenAPI)
- **Services** - Business logic (menu management, order processing)
- **Interfaces** - User interactions (CLI)

The `MenuService` loads menu items from YAML, the `OrderService` processes orders and calculates totals, and the `CLI` provides the user interface for order entry.
