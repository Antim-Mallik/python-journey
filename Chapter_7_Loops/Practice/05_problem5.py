# Printing the sum of entered natural numbers with while loop

n = int(input("Enter number: "))
i = 1
sum = 0
while(i<=n):
    sum += i # This means sum = sum+i
    i += 1 # This means i = i+1
print(sum)