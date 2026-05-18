c1 = "make a lot of money"
c2 = "buy now"
c3 = "subcribe now"
c4 = "click this"

message = input("Type your comment: ")

if (c1 in message or c2 in message or c3 in message or c4 in message):
    print("This is a spam comment")

else:
    print("Thank you for your comment")