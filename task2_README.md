# Task 2 - Pytest Demonstration

This branch contains example code used to demonstrate the functionality of the Pytest framework for our software testing assignment.

## Files

- 'temp_converter.py': Contains a simple class 'Temperature Converter' to convert Celsius to Fahrenheit and vice versa.
- 'test_temp_converter.py': Unit tests using Pytest, showcasing fixture and parameterization testing.
- 'test_basic.py': Example of basic parameterized testing and fixture usage.
- 'test_mock_example.py': Demonstrates how to use mocking in Pytest with the 'pytest-mock' plugin.

## Running Tests

```bash
pip install test pytest pytest-cov
pytest --cov=converter
