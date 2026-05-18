n = int(input("Enter number: "))
i = 1
odd_count = 0
even_count = 0
while(i<=n):
    if(i%2!=0):
        odd_count += 1
    elif(i%2==0):
        even_count += 1
    i += 1
print(odd_count)
print(even_count)