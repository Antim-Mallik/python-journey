def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.word)       
    return n
l = ["Antim", "Messi", "Neymar", "Ronaldinho", "Ronaldo"]
n = input("Enter word: ")
print(remove(l, n))