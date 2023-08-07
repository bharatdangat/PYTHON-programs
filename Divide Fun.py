#write Function To calculate Quotient and ramainder when a divided by b
def divide(a,b):
    c=a/b
    d=a%b
    print("Quetient=",c)
    print("Reminder=",d)

a=int(input("Enter Number First="))
b=int(input("Enter Number Second="))
divide(a,b)
