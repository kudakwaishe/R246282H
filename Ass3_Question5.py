celsius_temps = [0, 10, 20, 30, 40]

# Use map() and a lambda function for conversion
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

# Run bit
print(f"Celsius temperatures: {celsius_temps}")
print(f"Fahrenheit temperatures: {fahrenheit_temps}")
