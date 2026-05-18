s = {10, 7, 13, 333, 7, 69, 11, 7, 67, 9, 333}

s.add("Antim")
print(s)
print(s.union({10, 99, 100}))
print(s.intersection({10, 7, 69}))
s.remove(333)
print(s)
print(s.clear())