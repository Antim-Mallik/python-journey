def celsius_to_fahrenheit(c):
    return (9/5)*c + 32
c = int(input("Enter Celsius that you want to convert: "))
print(f"Conversion is {round(celsius_to_fahrenheit(c), 2)}")