a = int(input("Enter your score in Bangla: "))
b = int(input("Enter your score in English: "))
c = int(input("Enter your score in Math: "))

gpa1 = (a+b+c)
gpa2 = (gpa1/3)

if(a>=33):
    print("You Passed in Bangla")
else:
    print("You Failed in Bangla")
if(b>=33):
    print("You Passed in English")
else:
    print("You Failed in English")
if(c>=33):
    print("You Passed in Math")
else:
    print("You Failed in Math")

if(gpa2>=40):
    print("Your total gpa is",gpa2,":Passed")
else:
    print("Failed")