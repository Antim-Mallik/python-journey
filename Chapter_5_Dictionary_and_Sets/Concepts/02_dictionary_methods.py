marks = {"Antim": 100, 
         "Niloy": 98,
         "Sabbir":35,
         "Adif":85,
         "Shrabon":33}
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Antim")) # Prints none if key is not found
#print(marks["Antim"]) # Prints error if key is not found
marks.update({"Niloy": 96, "Fahad": 32})
print(marks)
print(len(marks))