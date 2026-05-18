letter = '''Dear <|Name|>
 You are selected!
  <|Date|>'''
print(letter.replace("Name", "Antim").replace("Date", "3 May 2026"))

# Anothe way (with f funtion)
name = input("Enter your name ")
print(f"Dear {name}\nYou are selected!\nDate: 5 May 2026")