class TemperatureConversor:
    #celsius and fahrenheit
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    #celsius and kelvin
    def celsius_to_kelvin(celsius):
        return celsius+ 273.15
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    #kelvin and fahrenheit
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15