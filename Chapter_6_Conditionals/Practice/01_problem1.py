a = int(input("Enter number "))
b = int(input("Enter number "))
c = int(input("Enter number "))
d = int(input("Enter number "))

if(a>=b and a>=c and a>=d):
    print(a, "is greater")
elif(b>=a and b>=c and b>=d):
    print(b, "is greater")
elif(c>=a and c>=b and c>=d):
    print(c, "is greater")
elif(d>=a and d>=b and d>=c):
    print(d, "is greater")