#accept n numbers in an array amd search number.
n=int(input("Enter Limit"))
a=[]
for i in range(0,n,1):
    num=int(input("Enter no in an array"))
    a.append(num) #it can use to join&store num in array
#end of for loop
print("Numbers=",a)
x=int(input("Enter no to search"))
if x in a:
    print("Number is found")
else:
    print("Number  is not found")
    
