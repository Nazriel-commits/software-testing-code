# Task 2 - Pytest Demonstration

This branch contains example code used to demonstrate the functionality of the Pytest framework for our software testing assignment.

## Files

- 'temp_converter.py': Contains a simple class to convert Celsius to Fahrenheit.
- 'test_temp_converter.py': Unit tests using Pytest with fixture and parameterization.
- 'test_basic.py': Example of basic parameterized testing and fixture usage.

## Running Tests

```bash
pip install test pytest pytest-cov
pytest --cov=converter
