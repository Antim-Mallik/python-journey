a = int(input("Enter your score in Bangla: "))
b = int(input("Enter your score in English: "))
c = int(input("Enter your score in Math: "))

gpa1 = (a+b+c)
gpa2 = (gpa1/3)

if(a>=33 and b>=33 and c>=33 and gpa2>=40):
    print("You Passed. Congratulation!")
else:
    print("You Failed. Try again next year!")