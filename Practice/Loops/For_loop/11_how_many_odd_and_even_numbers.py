n = int(input("Enter number: "))
odd_count = 0
even_count = 0
for i in range(1, n+1):
    if(i%2!=0):
        odd_count += 1
    elif(i%2==0):
        even_count += 1
print(odd_count)
print(even_count)