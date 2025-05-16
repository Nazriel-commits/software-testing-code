import pytest
from temp_converter import Temperature converter

@pytest.fixture
def temp_converter():
  return TemperatureConverter()

@pytest.mark.parametrize("celsius, expected", [(0, 32), (100, 212), (-40, -40)])
def test_to_fahrenheit(temp_converter, celcius, expected):
  assert temp_converter.to_fahreinheit(celsius) == expected
  
