def fahrenheit_to_celsius(f):
    return (5/9)*(f-32)
f = int(input("Enter Fahrenheit that you want to convert: "))
print(f"Conversion is {round(fahrenheit_to_celsius(f), 2)}")