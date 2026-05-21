def cm_to_inches(c):
    return c/2.54
c = int(input("Enter Inches that you want to convert: "))
print(f"Conversion is {round(cm_to_inches(c), 3)}")