#Write Function which give sin,cos and log of given number,
from math import*
def matho(a):
    s=sin(a)
    c=cos(a)
    l=log(a)
    print("Sin of given no=",s)
    print("Cos of given no=",c)
    print("Log of given no=",l)
a=int(input("Enter No="))
matho(a)
