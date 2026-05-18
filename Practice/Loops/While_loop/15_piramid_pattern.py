n = int(input("Enter number: "))
i = 1
while(i<=n):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print()
    i += 1