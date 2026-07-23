celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda x : (x * 9/5) + 32, celsius_temps))
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)