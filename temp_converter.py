class TemperatureConverter:
  def to_fahrenheit(self, celcius):
    return (celsius * 9/5) + 32

  def to_celsius(self, fahrenheit):
    return (fahrenheit - 32) * 5/9
