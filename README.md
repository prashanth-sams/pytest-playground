# Python Testing Framework

A simple pytest-based testing framework for mathematical operations, Playwright UI tests, and Selenium UI tests.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

Run all tests:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run tests with coverage:
```bash
pytest --cov=math_operations
```

Run specific test file:
```bash
pytest test_math_operations.py
```

Run specific test class:
```bash
pytest test_math_operations.py::TestAddition
```

Run only Playwright tests:
```bash
pytest test_playwright_calculator.py
```

Run Playwright tests in headed mode (see browser):
```bash
pytest test_playwright_calculator.py --headed
```

Run Playwright tests with browser slowdown (for debugging):
```bash
pytest test_playwright_calculator.py --headed --slowmo 1000
```

Run only Selenium tests:
```bash
pytest test_selenium_google.py
```

## Test Structure

### Unit Tests (pytest)
- `math_operations.py` - Contains simple mathematical functions
- `test_math_operations.py` - Contains pytest test cases for the mathematical functions

### UI Tests (Playwright)
- `sample_page.html` - A simple calculator web page for testing
- `test_playwright_calculator.py` - Contains Playwright test cases for the calculator UI

### UI Tests (Selenium)
- `test_selenium_google.py` - Contains Selenium WebDriver test for Google search
