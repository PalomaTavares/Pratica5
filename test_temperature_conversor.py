import unittest
from temperature_conversor import TemperatureConversor

class TestTemperatureConversor(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConversor.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(TemperatureConversor.celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(TemperatureConversor.celsius_to_fahrenheit(-40), -40)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_celsius(-40), -40)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConversor.celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(TemperatureConversor.celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(TemperatureConversor.celsius_to_kelvin(-273.15), 0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_celsius(373.15), 100)
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_celsius(0), -273.15)
    
    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_kelvin(-459.67), 0)
        self.assertAlmostEqual(TemperatureConversor.fahrenheit_to_kelvin(212), 373.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_fahrenheit(373.15), 212)
        self.assertAlmostEqual(TemperatureConversor.kelvin_to_fahrenheit(0), -459.67)

if __name__ == '__main__':
    unittest.main()