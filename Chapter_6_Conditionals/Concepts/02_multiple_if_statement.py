a = int(input("Enter your age: "))
# if statement no: 1
if(a%2==0):
    print("It is an even number")

else:
    print("It is an odd number")
# End of if statement number: 1

# If statement number:2
if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an negative number which is an invalid age")

elif(a==0):
    print("You are entering 0 which is a invalid age")

else:
    print("You are below the age of consent")
# End of if statement number: 2


print("End of program")