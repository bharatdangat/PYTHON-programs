#ARITHMATIC OPERATION
a=int(input("Entrer First No="))
b=int(input("Entrer Second No="))
op=input("Enter  operator(+,-,*,/,%)")

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="/":
    print(a/b)
elif op=="*":
    print(a*b)
elif op=="%":
    print(a%b)
else:
    print("INVALID OPERATION")
