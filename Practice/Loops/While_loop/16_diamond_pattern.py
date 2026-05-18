n = int(input("Enter number: "))
i = 1
while(i<=n):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print()
    i += 1
j = 1
k = n-1
while(n>0):
    print(" "*j, end="")
    print("*"*(2*k-1), end="")
    print()
    n -= 1
    j += 1
    k -= 1