a = int(input("Enter your age: "))
# f elif else ladder
if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an negative number which is an invalid age")

elif(a==0):
    print("You are entering 0 which is a invalid age")

else:
    print("You are below the age of consent")

print("End of program")