def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 / 1.609344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344
    liters_per_100km = 3.785411784 / (km_per_gallon / 100)
    return liters_per_100km

# Тестування функцій
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
