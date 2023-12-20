



IN REGULA FALSI A AND B ARE 2 AND 3



############################SLIP-1########################
Q.1. Attempt any two of the following.
#Maximum Marks: 35
#[10]
1. Use Python code to evaluate each of the following expression.

a. 20 modulus 2 + 7 - (3 +7) × 20 ÷ 2
  a=20%2 + 7 - (3 +7)*20/2
  print(a)
>>-93.0

// floar division=//
b. 30 × 10 floor division 3 + 10 modulus 3
  a=30*10//3 + 10%3
  print(a)
>>101

c. 2^5 - 2^4 + 4 floor division 4
  a=2**5-2**4+4//4
  print(a)
>>

2. Write Python code to repeat the following string 9 times using the string operator
‘*’.
a. Python
  s="Python"
  s1=s*9
  print(s1)
>>PythonPythonPythonPythonPythonPythonPythonPythonPython
b. Mathematics
s="mathematics"
  s1=s*9
  print(s1)
>>
3. Write Python program to generate the square of numbers from 1 to 10.
for i in range(1,11):
    s=i*i
    print(s)
    or.......................
    for i in range(1,11):
     print("square of",i,"=",i*i)
     

Q.2. Attempt any two of the following.
[10]
1. Using Python code construct the following matrices.

1. An identity matrix of order 10 × 10.
import numpy as np
print(np.eye(10*10))

2. Zero matrix of order 7 × 3.
from sympy import *
print(zeros(7,3))
>>
Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])

3. Ones matrix of order 5 × 4.
from sympy import *
print(ones(5,4))

2. Write Python program to find the 10 term of the sequence of function f (x) = x^2+x.
for x in range(1,11):
        c=x**2+x
        print(c)

3. Generate all the prime numbers between 1 to 100 using Python code.
#prime no=gcd=1 or tya sankhela tinech bhag jato.............
from math import *
for x in range(1,101):
        if gcd(100,x)==1:
            print(x)


############################SLIP-2########################
Q.1. Attempt any two of the following.
[10]

1. Write Python code to calculate the volume of a sphere with radius r = 7 (V = 4/3 πr**3 ).
def sphere(r):
    v=4//3*3.14*r**3
    print("volume of sphere=",v)

r=int(input("Enter radius of sphere"))
sphere(r)

>>Enter radius of sphere7
>>volume of sphere= 1077.02

2. Use Python code to construct string operation ‘+’ below string.

a. string1 = Hello, string2 = World!
  string1 ="Hello"
  string2 ="World!"
  string=string1+string2
  print(string)
>>HelloWorld!

b. string1 = Good, string2 = Morning
  string1 ="Hello"
  string2 ="World!"
  string=string1+string2
  print(string)
  HelloWorld!

3. Write Python code to generate the square of numbers from 20 to 30.
 for i in range(20,31):
    s=i*i
    print("square of",i,"=",s)

Q.2. Attempt any two of the following.
[10]
1. Use python code nd value of f (−2), f (0), f (2) where f (x) = x^2 –5x + 6.
  def f(x):
    f=x**2-5*x+6
    print(f)
x=int(input("Emter th value of x"))
f(x)

>>Emter th value of x0
6
>>Emter th value of x2
0

2. Write Python program to find the 10 term of the sequence of function f(x)=x^3+5x.
for x in range(1,11):
        c=x**2+x
        print(c)
3. Using sympy module of python, find the eigenvalues and corresponding eigenvectors
e of python,
  [4 2 2]
A=|2 4 2|
  [2 2 4]
>>A=Matrix([[4,2,2],[2,4,2],[2,2,4]])
>>print(A)
Matrix([[4, 2, 2], [2, 4, 2], [2, 2, 4]])
>>A.eigenvals()
{8: 1, 2: 2}
>>A.eigenvects()
[(2, 2, [Matrix([
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 1]])]), (8, 1, [Matrix([
[1],
[1],
[1]])])]

##########################slip-3##########################################
Q.1. Attempt any two of the following.
[10]
1. Write python code to test whether given number is divisible by 2 or 3 or 5
def divide(n):
    if n%2==0 or n%3==0 or n%5==0:
        print("Number is Divisible by 2 or 3 or 5")
    else:
        print("Number is not divsible by 2 or 3 or 5")
        
n=int(input("Enter Number-"))
divide(n)
    
2. Repeat the following string 11 times using the string operator ‘*’ on Python.
a. LATEX
  s="LSTEX"
  s1=s*11
  print(s1)
  
b. MATLAB
  s="MATLAB"
  s1=s*11
  print(s1)
  
3. Use Python code to find sum of first thirty natural numbers.
sum=0
for i in range(1,31):
    sum=sum+i
print("Sum of first thirty natural numbers",sum)


Q.2. Attempt any two of the following.
[10]
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
>>import numpy as np
print(np.eye(10*10))
[[1. 0. 0. ... 0. 0. 0.]
 [0. 1. 0. ... 0. 0. 0.]
 [0. 0. 1. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 1. 0. 0.]
 [0. 0. 0. ... 0. 1. 0.]
 [0. 0. 0. ... 0. 0. 1.]]

2. Zero matrix of order 7 × 3.
>>>2. Zero matrix of order 7 × 3.
from sympy import *
print(zeros(7,3))           #coma impppppppppppp

3. Ones matrix of order 5 × 4.
from sympy import *
print(ones(5,4))

2. Using python, nd the eigenvalues and corresponding eigenvectors of the matrix
from sympy import*
A=Matrix( [ [3,-2],[6,-4] ] )
print(A)
Matrix([[3, -2], [6, -4]])
A.eigenvals()
{-1: 1, 0: 1}
A.eigenvects()
[(-1, 1, [Matrix([
[1/2],
[  1]])]), (0, 1, [Matrix([
[2/3],
[  1]])])]
3. Generate all the prime numbers between 1 to 100 using Python code.
from math import *
for x in range(1,101):fromfrom math import *
for i in range(1,150):
    if gcd(111,i)==1:
         print(i,end=" ")
         


######################slip-4####################
Q.1. Attempt any two of the following.
[10]
1. Using python code sort the tuple in ascending and descending order 5, -3, 0, 1, 6,
-6, 2.
>>a=[5, -3, 0, 1, 6,-6, 2]
print(a)
[5, -3, 0, 1, 6, -6, 2]
sorted(a)
[-6, -3, 0, 1, 2, 5, 6]
sorted(a,reverse=True) #impppppppppppppppp not reversed vvvvvvvvvvv imp
[6, 5, 2, 1, 0, -3, -6]
 or#######################
a=(5,-3,0,1,6,-6,2)
print(a)
print("Ascending order=",sorted(a))
print("Descending order=",sorted(a,reverse=True))
      
2. Write python program which deals with concatenation and repetition of lists.
List1 = [15, 20, 25, 30, 35, 40]
List2 = [7, 14, 21, 28, 35, 42]
(a) Find List1 + List2
(b) Find 9*List1
(c) Find 7*List2

>>>>>>>>>>>
List1 = [15, 20, 25, 30, 35, 40]
List2 = [7, 14, 21, 28, 35, 42]
List1 + List2
[15, 20, 25, 30, 35, 40, 7, 14, 21, 28, 35, 42]
List1*8
[15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40, 15, 20, 25, 30, 35, 40]
List2*7
[7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42, 7, 14, 21, 28, 35, 42]


3. Write Python code to nd the square of odd numbers from 1 to 20 using while loop.
i=1
while i<=20:
    if i%2==1:
        print("squre of",i,"=",i*i)
    i=i+1product=1





#while i<=10:
 #   product=product*i
  #  i=i+1
#print("product=",product)
    

    

>>>squre of 1 = 1
squre of 3 = 9
squre of 5 = 25
squre of 7 = 49
squre of 9 = 81
squre of 11 = 121
squre of 13 = 169
squre of 15 = 225
squre of 17 = 289
squre of 19 = 361

  
Q.2. Attempt any two of the following.
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10
import numpy as np
zeros(10*10)
2. Zero matrix of order 7 × 3.
from sympy import *
print(zeros(7,3)).
3. Ones matrix of order 5 × 4.

2. Find the data type of the following data by using Python code.
a. number
b. 31.25
c. 8 + 4j
d. Mathematics
e. 49

>>number=55
type(number)
<class 'int'>
a=32.35
type(a)
<class 'float'>
a=8+4j
type(a)
<class 'complex'>
a="mathematics"
type(a)
<class 'str'>

  
3. Write Python program to find the determinant of matrices.
A=Matrix([[1,0,5],[2,1,6],[3,4,0]])
print(A)
Matrix([[1, 0, 5], [2, 1, 6], [3, 4, 0]])
B=Matrix([[2,5],[-1,4]])
print(B)
Matrix([[2, 5], [-1, 4]])
A.det()
1
B.det()
13

##############slip-5###########################
Q.1. Attempt any two of the following.
[10]
1. Using sympy module of python nd the following for the matrices
(a) 2A + B.
(b) 3A – 5B.
(c) A−1 .
(d) B 3 .
(e) AT + B T .
>>A=Matrix([[-1,1,0],[8,5,2],[2,-6,2]])
print(A)
Matrix([[-1, 1, 0], [8, 5, 2], [2, -6, 2]])
B=Matrix([[9,0,3],[1,4,1],[1,0,-1]])
print(B)
Matrix([[9, 0, 3], [1, 4, 1], [1, 0, -1]])
2*A+B
Matrix([
[ 7,   2, 3],
[17,  14, 5],
[ 5, -12, 3]])

3*A-5*B
Matrix([
[-48,   3, -15],
[ 19,  -5,   1],
[  1, -18,  11]])
A**-1
Matrix([
[-11/17, 1/17, -1/17],
[  6/17, 1/17, -1/17],
[ 29/17, 2/17, 13/34]])
B**3
Matrix([
[780,  0, 228],
[148, 64,  52],
[ 76,  0,  20]])

Transpose(A)
Matrix([
[-1,  1, 0],
[ 8,  5, 2],
[ 2, -6, 2]]).T
Transpose(B)
Matrix([
[9, 0,  3],
[1, 4,  1],
[1, 0, -1]]).T
Transpose(A)+Transpose(B)
Matrix([
[8, 9,  3],
[1, 9, -6],
[3, 3,  1]])



2. Evaluate following expression on Python.
>>>>>>M=[1,2,3,4]
print(len(M))
4
L="XYZ"+"pqr"
print(L)
XYZpqr
s="Make In India"
s[:7]
'Make In'
s[:9]
'Make In I'


3. Use Python code to generate the square root of numbers from 21 to 49.
from math import *
for i in range(21,50):
    print("Suare root of",i,"=",sqrt(i))

Q.2. Attempt any two of the following.
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
2. Zero matrix of order 7 × 3.
3. Ones matrix of order 5 × 4.
>simpleeeeeeeeeeeeee
2. Using linsolve command in python, solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4           
−3x + 2y − 2z = -10

>>Tough
 
3. Generate all relatively prime numbers to 111 which are less than 150 using Python
code.
from math import *
for i in range(1,150):
    if gcd(111,i)==1:
         print(i,end=" ")
         
1. Write Python code to nd eigenvalues and corresponding eigenvectors of the matrix
and hence nd matrix P with diagonalize to A.
>>A=Matrix([[1,3,3],[2,2,3],[4,2,1]])
>>A.eigenvals()
{7: 1, -1: 1, -2: 1}
>>A.eigenvects()
[(-2, 1, [Matrix([
[-1/2],
[-1/2],
[   1]])]), (-1, 1, [Matrix([
[ 0],
[-1],
[ 1]])]), (7, 1, [Matrix([
[1],
[1],
[1]])])]
>>P=A.diagonalize()
print(P)
(Matrix([
[-1,  0, 1],
[-1, -1, 1],
[ 2,  1, 1]]), Matrix([
[-2,  0, 0],
[ 0, -1, 0],
[ 0,  0, 7]]))



##########################slip-6##################################
Q.1. Attempt any two of the following.
1. Using Python evaluate each of the following expression.
a. 23 modulus 2 + 9 - (3 +7) × 10 ÷ 2
b. 35 × 10 oor division 3 + 15 modulus 3
c. 35 − 25 + 4 oor division 7
==>
a. 23 modulus 2 + 9 - (3 +7) × 10 ÷ 2
  a=23%2 + 9 - (3 +7)*10/2
  print(a)
b. a=35-25+4//7
  print(a)
  
2. Write Python code to list name and roll number of 5 students in B.Sc.
(Computer science).
a1=[{"roll no":101,"name":"om"},{"roll no":102,"name":"sai"},{"roll no":103,"name":"ram"},{"roll no":104,"name":"sham"},{"roll no":105,"name":"aman"}]
print(a1)
[{'roll no': 101, 'name': 'om'}, {'roll no': 102, 'name': 'sai'}, {'roll no': 103, 'name': 'ram'}, {'roll no': 104, 'name': 'sham'}, {'roll no': 105, 'name': 'amanfor i in range(20,31):
'}]
##################orrrrrrrrrrrrrrrrrrrrrrrrrrr
for i in range(5):
    r=int(input("Enter roll nos of five students-"))
    n=(input("Enter names of five student-"))
    print("Roll no=",r,"Name=",n)
    >>>>>>>>>
    Enter roll nos of five students-1
Enter names of five student-om
Roll no= 1 Name= om
Enter roll nos of five students-2
Enter names of five student-sai
Roll no= 2 Name= sai
Enter roll nos of five students-3
Enter names of five student-ram
Roll no= 3 Name= ram
Enter roll nos of five students-4
Enter names of five student-sham
Roll no= 4 Name= sham
Enter roll nos of five students-5
Enter names of five student-aman
Roll no= 5 Name= aman


3. Write Python code to nd maximum and minimum element in the given list.
[7, 8, 71, 32, 49, −5, 7, 7, 0, 1, 6]

a=[7, 8, 71, 32, 49, -5, 7,-7, 0, 1, 6]
max(a)
>>>>71
min(a)
>>>>>-7
Q.2. Attempt any two of the following.
[10]
1. Using Python code construct identity matrix of order 10 and hence nd determinant,
trace and transpose of it.
import numpy as np
>>A=np.eye(10)
print(A)
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
 
1]-np.linalg.det(A)
1.0

2]-np.trace(A)
10.0
3]-np.transpose(A)
array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
       
       
2. Write Python code to find the value of function f (x, y) = x2 − 2xy + 4 at the points
(2,0) (1,-1).
>>>>>def function(x,y):
    f=x**2-2*x*y+4
    print(f)
x=int(input("Enter value of x="))
y=int(input("Enter value of y="))
function(x,y)
>>>>>>
Enter value of x2
Enter value of y0
8
Enter value of x=1
Enter value of y=-1
7

3. Find number between 1 to 200 which are divisible by 7 using Python code.
for i in range(1,201):
    if i%7==0:
        print(i,end=" ")
        

Q.3. a. Attempt any one of the following.
2. Write Python code to diagonalize matrix
and nd matrix P with diagonalize of A and diagonal matrix D.
>>>>
A=Matrix([[3,-2],[6,-4]])
P,D=A.diagonalize()
print(P)
Matrix([[1, 2], [2, 3]])
print(D)
Matrix([[-1, 0], [0, 0]])


####################slip-7############################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Using Python, evaluate the following expression of two complex number 
z1 = 5 + 3j
and z2 = −5 + 7j
a. z1 + z2
b. z1 − z2
c. z1 ∗ z2

>>
z1+z2
10j
z1-z2
(10-4j)
z1*z2
(-46+20j)

2. Repeat the following string 7 times using the string operator ‘*’ on Python.
a. Complex Number
b. Real Number
>>>>>>>>>simple
3. Write Python code to generate cube of numbers from 1 to 50.
 for i in range(1,51):
   cube=i*i*i
   print("Cube of",i,"=",cube)


Q.2. Attempt any two of the following.
[10]
1. Using Python code construct 0nes matrix of order 10 × 10 and hence nd determi-
nant, trace and transpose of it.
>>
A=print(ones(10,10))
Matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])





>>A=np.eye(10)
print(A)
[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
 
1]-np.linalg.det(A)
1.0

2]-np.trace(A)
10.0
3]-np.transpose(A)
array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
       
2. Write Python code to obtained f (−1), f (0), f (1) of the f (x) = x^3 − 4x − 9.
def f(x):
    f=x***3-4x-9
    print(f)
x=int(input("Emter th value of x"))
f(x)

3. Generate all the prime numbers between 500 to 1000 using Python program.
from math import *
for x in range(500,1001):
    if gcd(1000,x)==1:
        print(x)
        
########################slip-8###################################
.1. Attempt any two of the following.
[10]
1. Use Python code to nd a + c, ab, c^d , a/b and a(b + c),
where a = 5, b = 7, c = 9, d = 11.
a = 5
b =7
c = 9
d = 11.
a+c
14
c*d
99
c^d
2
a/b
0.7142857142857143
a*(b+c)
80


2. The following two statements using the ‘+’string operation on Python.
a. string1 = India Won, string2 = World Cup
b. string1 = God, string2 = is Great
string1 = "India Won"
string2= "World Cup"
string1+string2
'India WonWorld Cup'


3. Write Python code to nd area and circumference of circle with radius 14.
def circle(r):
    a=3.14*r*r
    c=2*3.14*r
    print("Area Of Circle=",a)
    print("Circumference Of Circle=",c)

r=int(input("Enter Radius ="))
circle(r)
 
Q.2. Attempt any two of the following.
[10]
1. Using Python code logically verify associativity of matrices with respective to matrix
addition (use proper matrices).
>>>>>>>>
from sympy import*
A=Matrix([[2,3],[1,3]])         #logiccccccc logicccccccccc
B=Matrix([[1,2],[3,4]])
C=Matrix([[3,3],[2,1]])
r1=A+(B+C)
r2=(A+B)+C
print(r1)
Matrix([[6, 8], [6, 8]])
print(r2)
Matrix([[6, 8], [6, 8]])




/impppppppppppppppppppppppppppppppppppppppppppp
///////imppppppppp2. Write Python code to generate 10 terms of Fibonacci Sequence using loop.
>>>a=0
b=1
for i in range(10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

    
0 1 1 2 3 5 8 13 21 34 

3. Using Python code, nd determinant and inverse of the matrix if exist.

  4 2 2
A=2 4 2 
  2 2 4
 from sympy import*
A=Matrix([[4,2,2],[2,4,2],[2,2,4]])
print(A)
Matrix([[4, 2, 2], [2, 4, 2], [2, 2, 4]])
 >>A.det() #|A|!=0 then A inverse is exit.....................
32
A.inv()
Matrix([
[ 3/8, -1/8, -1/8],
[-1/8,  3/8, -1/8],
[-1/8, -1/8,  3/8]])

##################slip-9########################################
.1. Attempt any two of the following.
[10]
1. Using Python evaluate each of the following expression.
a. 30 modulus 2 + 7 - (3 +9) × 20 ÷ 5
b. 30 × 10 oor division 3 + 30 modulus 3
c. 55 - 53 + 7 oor division 7
>>simple...........................
2. Use print command on Python to nd
(a) sin30
(b) pi
(c) e
(d) cos30
>>>
 from math import *
sin(30)
-0.9880316240928618
pi
3.141592653589793
e
2.718281828459045
cos(30)
0.15425144988758405



#modulus=abs()
3. Write Python code to generate modulus value of -10 ,10, -1,1,0
>>>>>>>>>>
abs(-10)
10
abs(-1)
1
abs(10)
10
abs(1)
1
abs(0)
0

#**********or******************
mod=0
list=[-10,10,-1,1,0]
for i in list:
    mod=abs(i)
    print(mod)

    
10
10
1
1
0




Q.2. Attempt any two of the following.
[10]
1. Use Python code to generate second, fifth, eight characters from string
‘MATHEMATICS ’
>>>a="MATHEMATICS"
a[2]
'T'
a[5]
'M'
a[8]
'I'
 
2. Using python find the eigenvalues and corresponding eigenvectors of the matrix
>>>>>>>>simpleeeeee
3. Write Python code to verify (AB)−1 = B −1 A−1 (Use proper matrices A and B).
>>>>>Tough
####################slip-10##############################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Using Python evaluate each of the following expression.
a. 50 modulus 5 + 11 - (13 +7) × 10 ÷ 5
>>a=50%5 + 11 - (13 +7) *10/5
print(a)
-29.0

b. 60 × 20 oor division 3 + 15 modulus 3
>>b=60*20//3 + 15%3
print(b)
400
 
c. 27 - 23 + 8 floor division 4
>>c=27 - 23 + 8 // 4
print(c)
6

2. Using Python code
List1 = [5, 10, 15, 20, 25, 30] and List2 = [7, 14, 21, 28, 35, 42]
Evaluate
(a) List1 + List2
(b) 3*List1
(c) 5*List2
>>>List1 = [5, 10, 15, 20, 25, 30]
List2 = [7, 14, 21, 28, 35, 42]
List1 + List2
[5, 10, 15, 20, 25, 30, 7, 14, 21, 28, 35, 42]
List1*3
[5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]

  
3. Write Python code to nd area of triangle whose base is 10 and height is 15.
#we know area of traingle=1/2bh
def traingle(h,b):
    a=1/2*b*h
    print("Area of trangle=",a)
    
h=int(input("Enter height-"))
b=int(input("Enter base-"))
traingle(h,b) 
    

Q.2. Attempt any two of the following.
[10]
1. Using Python construct the following matrices.
1. An identity matrix of order 10 × 10.
import numpy as np
print(np.eye(10*10))
[[1. 0. 0. ... 0. 0. 0.]
 [0. 1. 0. ... 0. 0. 0.]
 [0. 0. 1. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 1. 0. 0.]
 [0. 0. 0. ... 0. 1. 0.]
 [0. 0. 0. ... 0. 0. 1.]]
2. Zero matrix of order 7 × 3.
>>from sympy import*
print(zeros(7,3))
3. Ones matrix of order 5 × 4.
>>from sympy import*
print(ones(5,4))

2. Write Python program to fnd the value of function f (x) = x^2 + x, (−5 ≤ x ≤ 5).
>>for x in range(-5,6):
        f=x**2+x
        print(f,end=" ")
>>20 12 6 2 0 0 2 6 12 20 30 

3. Write Python program to nd the determinant of matrix
>>>A.det()
##############################slip-11#####################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Evaluate following expression on Python.
(a) M =[1,2,3,4,5,6,7], Find length M.
>>>len(M)
>>7

 List1 = [5, 10, 15, 20, 25, 30]
List2 = [7, 14, 21, 28, 35, 42]
List1 + List2
[5, 10, 15, 20, 25, 30, 7, 14, 21, 28, 35, 42]
List1*3
[5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]


(b) L=“XY”+“pqr”, Find L.
a="XY"
b="pqr"
L=a+b
print(L)
>>>>>>>>>XYpqr

(c) s=‘Make In India’, Find (s[:5]) & (s[:9]).
>>>>>>>>simple
2. Use Python to evaluate expression of the following matrix.
(a) Eigen Value of A.
(b) determinant of A.
(c) inverse of A.
>>>>>>>>>>>>>>>>>simple
3. Write Python code to reverse the string S=[3,4,5,6,7,8,9,10,11,12,13].
S=[3,4,5,6,7,8,9,10,11,12,13]
sorted(S,reverse=True)
[13,12,11,10,9, 8, 7, 6, 5, 4, 3]

Q.2. Attempt any two of the following.
[10]
1. Using Python code to list Name of 5 teacher in your college with their subject.
 >>>simpleeeeeeeeee
2. Use linsolve command in python to solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4
−3x + 2y − 2z = −10
3. Generate all the prime numbers between 51 to 100 using Python program.
simple...............
from math import*
for i in range(51,100):
    if gcd(100,i)==1:
        print(i)

#################################slip-12###############################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Using Python evaluate each of the following expression.
a. 23 modulus 2 + 9 - (3 +7) × 10 ÷ 2
b. 35 × 10 oor division 3 + 15 modulus 3
c. 35 - 25 + 4 oor division 7
>>>>simpleeeeeeeeeeeee
>>>>>>>>>>>>simple
2. Use while command on Python to nd odd positive integer between 25 to 50.
i=25
while(i<=50):
    if i%2==1:
        print(i)
    i=i+1

3. For matrix apply the following operations by using python.
a. Delete 2nd row.
b. Delete 1st column.
c. Add column [9, 9] as 2nd column.
>>>>>>>>>>Toughhh
Q.2. Attempt any two of the following.
[10]
1. Write Python nd the eigenvalues and corresponding eigenvectors of the matrix
>>>>>>>simpleeeeeeee
2. Write Python program to nd the product of n natural numbers using while loop.
product=1
i=1
while i<=10:
    product=product*i
    i=i+1
print("product=",product)
    

3. Generate all prime numbers between 1 to 200 using Python code.
>>simple................
#############################slip-13#############################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Using Python code, evaluate the following expression of two complex number z1 =
3 + 2j and z2 = −4 + 1j
a. z1 + z2
b. z1 − z2
c. z1 ∗ z2
>>>>>>>>>>
z1=3+2j
z2=-4+1j
z1+z2
(-1+3j)
z1-z2
(7+1j)
z1z2
z1*z2
(-14-5j)

2. Use Python code to nd area and circumference of square whose length is 5.
def squre(a):
    a=a**2
    c=4*a
    print("Area Of Square=",a)
    print("Circumference Of Square=",c)

a=int(input("Enter length="))
squre(a)

3. Write Python program to generate the square number from 1 to 10.
for i in range(20,31):
    s=i*i
    print("square of",i,"=",s)

Q.2. Attempt any two of the following.
[10]
1. Write Python code to reverse the string S=[1,2,3,4,5,6,7,8,9].
S=[1,2,3,4,5,6,7,8,9]
sorted(S,reverse=True)
[9, 8, 7, 6, 5, 4, 3, 2, 1]


2. Write Python program to nd f (x) = x^2+3x, Where (−1 ≤ x ≤ 3).
for x in range(-1,4):
    f=x^2+3*x
    print(f)
>>
 0
 2
 4
 10
 8
 
3. Write Python code to fnd average of number 50 to 100.
s=0
for i in range(50,101):
    s=s+i
    a=s/51

print("Avarage of numbers=",a)
>>>Avarage of numbers= 75.0

#######################slip-14#####################################

Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Use print code on Python (a=4,b=6,c=8,d=12).
(a) print(a+c)
(b) print(a*b)
(c) print(c**d)
(d) print(a/b)
(e) Expression: 3 + ( 9 - 2) / 7 * 2 ** 2
>>>>>>>>>>>>simpleeeeeeeeeeeee
2. For the following two statements use ‘+’string operation on Python.
a. string1 = Hello, string2 = World!
b. string1 = Good, string2 = Morning
3. Use Python loop to print(‘Hallo’,i,‘You Learn Python’)
where i = [‘Saurabh’,‘Akash’,‘Sandeep’,‘Ram’,‘Sai’]
>>>>>>>>>>>>>>>>simple
Q.2. Attempt any two of the following.
[10]
1. Using Python code construct any two matrices A and B
1. Show that A+B=B+A.
2. Find A-B.
2. Write Python program to nd the sequence of function f (x) = x + 5, (−5 ≤ x ≤ 5)
for x in range(-5,6):
    f=x+5
    print(f)
3. Using sympy module of python nd the eigenvalues and corresponding eigenvectors
>>>>>simple

#############################slp-15###########################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Using for loop on Python, nd range from 1 to 11 integers.
for i in range(1,12)
2. Use Python code to nd,
(a) sin75
(b) pi/2
(c) e
(d) cos56
>>simpleeeeeeeeeeee
3. Write Python program to nd diameter, area, circumference of the circle with radius
is 5.
>>>>>>>>>>>>>simpleeeeeeeeeeee
Q.2. Attempt any two of the following.
[10]
1. Using Python code construct any three matrices A,B and C to show that
(A+B)+C=A+(B+C).
2. Using python nd the eigenvalues and corresponding eigenvectors of the matrix
>simpleeeee
3. Generate all prime numbers between 1000 to 2000 using Python program.
from math import *
for x in range (1000,2000):
    if gcd(2000,x)==1:
        print(x,end=" ")



##########slip-22##################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python code to sort a tuples in ascending order (49, 17, 23, 54, 36, 72).
>>>>>>>>>>>>>>a=[49, 17, 23, 54, 36, 72]
sorted(a)
[17, 23, 36, 49, 54, 72]

2. Find the values of the following expressions if x and y are true and z is false.
(a) (x or y) and z.
>>>>>>(True or True) and False
False
(b) (x and y) or not z.
>>>>>>>>>>>(True and True) or not Flase
True
(c) (x and not y) or (x and z).
>>true

3. Write Python code to nd the tuple ‘MATHEMATICS’ from range 3 to 9.
a[3:9]
'HEMATI'

Q.2. Attempt any two of the following.
[10]
1. Write Python program that prints whether the given number is positive, negative
or zero.
>>>>>>>simpleeeee

2. Write Python program to nd the sum of rst n natural numbers.
>>>>>>>>>>>>>simple
3. Using Python accept the matrix
Find the Null space, Column space and rank of the matrix.
A.nullspace()
[ ]
A.columnspace()
[Matrix([
[ 1],
[-3],
[ 5],
[-4]]), Matrix([
[-3],
[ 9],
[-2],
[12]]), Matrix([
[ 2],
[-1],
[ 6],
[ 2]]), Matrix([
[-4],
[ 5],
[-3],
[ 7]])]

A.rank()
4





#*********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************


#########################slip-16############################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python program to find absolute value of a given real number(n).
int_num=-25
float_num=-10.50
print("absolute value for int num=",abs(int_num))
absolute value for int num= 25
print("absolute value for float num=",abs(float_num))
absolute value for float num= 10.5

2. Using Python program
List1 = [5, 10, 15, 20, 25, 30] and List2 = [7, 14, 21, 28, 35, 42]
Evaluate
(a) List1 + List2
(b) 7*List1
(c) 11*List2
3. Write Python program to nd the area and circumference of a circle(r=5).
>>>>>>>simpleeeeeeeeeeee
Q.2. Attempt any two of the following.
[10]
1. Using Python code, fnd percentage of marks 70,80, 55, 78, 65 in five subject out of
100 each.
.
m1=int(input("Enter First subject marks"))
m2=int(input("Enter Second subject marks"))
m3=int(input("Enter Third subject marks"))
m4=int(input("Enter Fourth subject marks"))
m5=int(input("Enter Fifth subject marks"))

sum=m1+m2+m3+m4+m5+m6

print("sum of marks=",sum)
print("per of marks=",(sum/5))
2. Using sympy module of python, nd the following terms of vector x = [1, -5, 0] and
y = [2, 3, -1].
a. 5x
b. x+y
c. x-3y
3. Write python code to nd the determinant and inverse of matrices
 >>>>>>from sympy import*
A=Matrix([[1,0,5],[2,1,6],[3,4,0]])
B=Matrix([[2,5],[-1,4]])
print(A)
Matrix([[1, 0, 5], [2, 1, 6], [3, 4, 0]])
print(B)
Matrix([[2, 5], [-1, 4]])
det(A)
1
A.inv()
Matrix([
[-24,  20, -5],
[ 18, -15,  4],
[  5,  -4,  1]])
det(B)
13
B.inv()
Matrix([
[4/13, -5/13],
[1/13,  2/13]])


######################slip-17################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write the Python code to print ‘Python is bad’ and ‘Python is wonderful’ , where
wonderful is global variable and bad is local variable.

2. Write Python code to evaluate eigen value and eigen vector of the following matrix.
>>>simpleeeeeee
3. Write Python code, nd a, b and c such that a^2 + b^2 = c^2 .(where 1 ≤ a, b, c ≤ 50)
>>>>>
   
Q.2. Attempt any two of the following.
[10]
1. Using Python code construct any two matrices A and B to show that
(AB)^-1 = B^-1*A^-1.
>>>>>>>Togh

2. Use linsolve code in python to solve the following system of linear equations.
x − 2y + 3z = 7
2x + y + z = 4
−3x + 2y − 2z = −10
>>>Tough
3. Write python code to find trace and transpose of matrixx.......
>>>>>from sympy import*
A=Matrix([[1,3,3],[2,2,3],[4,2,1]])
transpose(A)
Matrix([
[1, 2, 4],
[3, 2, 2],
[3, 3, 1]])
trace(A)
4


########################slip-18##############################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Use Python code to nd minimum value from the given numbers
16,3,5,48,2,4,5,6,78,12,5,6,24.
>>a=[16,3,5,48,2,4,5,6,78,12,5,6,24]
min(a)
2

2. Use Python code to nd hypotenuse of triangle whose sides are 12 and 5.
#hypotenus of traingle=sqrt(a^2+b^2)
from math import *
def traingle(a,b):
    hypo=sqrt(a**2+b**2)
    print("hypotenus of traingle=",hypo)

a=int(input("Enter First side"))
b=int(input("Enter second side"))
traingle(a,b)


3. Use Python code to remove all digits after decimal of the given Number 125312.3142.
>>>>>>Tough
Q.2. Attempt any two of the following.
[10]

1. Using Python code, nd the below matrices, where A =
(a) A+B
(b) AT
(c) A^−1
>>>>>>>>>>simpleeee
2. Use while code on Python to find sum of first twenty natural number.
sum=0
i=1
while i<=20:
    sum=sum+i
    i=i+1
print("sum of first 20 naural numbers=",sum)
  >>>>>>>>>>>sum of first 20 naural numbers= 210


>>simpleeeeeeeeeeeeeeeee
3. Write Python program to diagonalize the matrix
and nd matrix P and D.
>>>>>A=Matrix([[3,-2],[6,-4]])
P,D=A.diagonalize()
print(P)
Matrix([[1, 2], [2, 3]])
print(D)
Matrix([[-1, 0], [0, 0]])

##########################slip-19#########################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write python code to display multiplication tables of numbers 2 to 10.
for i in range(2,11):
    print("Multiplication tble of",i)
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
        

>>>>>>>> Multiplication tble of 2
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 
8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
Multiplication tble of 3
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
Multiplication tble of 4
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
4 X 10 = 40
Multiplication tble of 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
Multiplication tble of 6
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
6 X 10 = 60
Multiplication tble of 7
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
Multiplication tble of 8
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
8 X 10 = 80
Multiplication tble of 9
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90
Multiplication tble of 10
10 X 1 = 10
10 X 2 = 20
10 X 3 = 30
10 X 4 = 40
10 X 5 = 50
10 X 6 = 60
10 X 7 = 70
10 X 8 = 80
10 X 9 = 90
10 X 10 = 100


2. Write Python code to check if a number is Zero, Odd or Even

a=int(input("Enter number"))
if a%2==0:
    print("Number is even")
else:
    print("Number is odd")
    
3. Write Python code to list name and birth date of 5 students in your class.
print("Name-","om","birthdate-","20-5-2005")
print("Name-","sai","birthdate-","2-8-2006")
print("Name-","ram","birthdate-","4-1-2005")
print("Name-","sham","birthdate-","24-12-2004")
print("Name-","aman","birthdate-","19-3-2003")

>>>>>>>>simpleeeeeeeeeee
Q.2. Attempt any two of the following.
[10]
1. Write python code to nd transpose and inverse of matrix
>>>>>>>>>>simpleeeeeeee
2. Declare the matrix
 fnd a row echelon form and the rank of matrix A.
 >>>>>
 A=Matrix([[5,2,5,4],[10,3,4,6],[2,0,-1,11]])
print(A)
Matrix([[5, 2, 5, 4], [10, 3, 4, 6], [2, 0, -1, 11]])

A.rref()
(Matrix([
[1, 0, 0,   77/9],
[0, 1, 0, -104/3],
[0, 0, 1,   55/9]]), (0, 1, 2))

A.rank()
3
3. Declare the matrix
find the matrices L and U such that A = LU.
>>>>>>>Tough

Q.3. a. Attempt any one of the following.
##########################slip-20####################

Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python code to print rst n natural numbers and their square roots of input
integer n.
from math import *
n=int(input("Enter Limit-"))
print("first n natural numbers")
for i in range(1,n+1):
    print(i,end="  ")
    print("                                ")
print("square root of first n natural numbers-")
for i in range(1,n+1):
    print(i,"=",sqrt(i))

2. Use Python code to find sum of square of frst twenty five natural numbers
.sum=0
for i in range(1,26):
    sum=sum+i*i 
print("sum_of_square=",sum)

3. Write Python code to nd all positive divisors of given number n.
n=int(input("Enter number n"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        

Q.2. Attempt any two of the following.
[10]
1. Write python code to display tuple ‘I am Indian ’ and the second letter in this tuple
n=int(input("Enter number-"))
for i in range(1,n+1):
    if n%i==0:
        print("Divisors=")
        print(i,end=" ")


2. Write python code to display the matrix whose all entries are 10 and order is (4,6).
import numpy as np
print(np.full((4,6),10))
      
[[10 10 10 10 10 10]
 [10 10 10 10 10 10]
 [10 10 10 10 10 10]
 [10 10 10 10 10 10]]
3. Write Python program to diagonalize the matrx
and nd matrix P and D.
>>>>>>>>>>A=Matrix([[3,-2],[6,-4]])
P,D=A.diagonalize()
print(P)
Matrix([[1, 2], [2, 3]])
print(D)
Matrix([[-1, 0], [0, 0]])

#############slip-21#####################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python code to display multiplication tables of numbers 20 to 30.
for i in range(20,30):
    print("Multiplication tble of",i)
    for j in range(1,11):
        print(i,"X",j,"=",i*j)

  
Multiplication tble of 20
20 X 1 = 20
20 X 2 = 40
20 X 3 = 60
20 X 4 = 80
20 X 5 = 100
20 X 6 = 120
20 X 7 = 140
20 X 8 = 160
20 X 9 = 180
20 X 10 = 200
Multiplication tble of 21
21 X 1 = 21
21 X 2 = 42
21 X 3 = 63
21 X 4 = 84
21 X 5 = 105
21 X 6 = 126
21 X 7 = 147
21 X 8 = 168
21 X 9 = 189
21 X 10 = 210
Multiplication tble of 22
22 X 1 = 22
22 X 2 = 44
22 X 3 = 66
22 X 4 = 88
22 X 5 = 110
22 X 6 = 132
22 X 7 = 154
22 X 8 = 176
22 X 9 = 198
22 X 10 = 220
Multiplication tble of 23
23 X 1 = 23
23 X 2 = 46
23 X 3 = 69
23 X 4 = 92
23 X 5 = 115
23 X 6 = 138
23 X 7 = 161
23 X 8 = 184
23 X 9 = 207
23 X 10 = 230
Multiplication tble of 24
24 X 1 = 24
24 X 2 = 48
24 X 3 = 72
24 X 4 = 96
24 X 5 = 120
24 X 6 = 144
24 X 7 = 168
24 X 8 = 192
24 X 9 = 216
24 X 10 = 240
Multiplication tble of 25
25 X 1 = 25
25 X 2 = 50
25 X 3 = 75
25 X 4 = 100
25 X 5 = 125
25 X 6 = 150
25 X 7 = 175
25 X 8 = 200
25 X 9 = 225
25 X 10 = 250
Multiplication tble of 26
26 X 1 = 26
26 X 2 = 52
26 X 3 = 78
26 X 4 = 104
26 X 5 = 130
26 X 6 = 156
26 X 7 = 182
26 X 8 = 208
26 X 9 = 234
26 X 10 = 260
Multiplication tble of 27
27 X 1 = 27
27 X 2 = 54
27 X 3 = 81
27 X 4 = 108
27 X 5 = 135
27 X 6 = 162
27 X 7 = 189
27 X 8 = 216
27 X 9 = 243
27 X 10 = 270
Multiplication tble of 28
28 X 1 = 28
28 X 2 = 56
28 X 3 = 84
28 X 4 = 112
28 X 5 = 140
28 X 6 = 168
28 X 7 = 196
28 X 8 = 224
28 X 9 = 252
28 X 10 = 280
Multiplication tble of 29
29 X 1 = 29
29 X 2 = 58
29 X 3 = 87
29 X 4 = 116
29 X 5 = 145
29 X 6 = 174
29 X 7 = 203
29 X 8 = 232
29 X 9 = 261
29 X 10 = 290


2. Write Python code to list name and birth date of 5 students in your class.
>>>>>>>>>simpleeeeeeeee

3. Write Python function f (a, b) = 3(a–6b)
, nd the value of f (12, 25).
>>>>simple
Q.2. Attempt any two of the following.
[10]
1. Using Python construct the following matrices.
1. Matrix of order 5×6 with all entries 1.
import numpy as np
print(np.full((5,6),1))
[[1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]
 [1 1 1 1 1 1]]
2. Zero matrix of order 27 × 33.
>>>

from sympy import *
print(zeros(12,13))

3. Identity matrix of order 5.
import numpy as np
print(np.eye(5))
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]

2. Write python code to perform the R2 + 2R1 row operation on given matrix.
>>>>>>Tough
3. Write python code to nd all the eigen values and the eigen vectors of the matrix.
s>>>>>>>>>>>>>impleeee
##########slip-22##################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python code to sort a tuples in ascending order (49, 17, 23, 54, 36, 72).
>>>>>>>>>>>>>>a=[49, 17, 23, 54, 36, 72]
sorted(a)
[17, 23, 36, 49, 54, 72]

2. Find the values of the following expressions if x and y are true and z is false.
(a) (x or y) and z.
>>>>>>(True or True) and False
False
(b) (x and y) or not z.
>>>>>>>>>>>(True and True) or not Flase
True
(c) (x and not y) or (x and z).
>>true

3. Write Python code to nd the tuple ‘MATHEMATICS’ from range 3 to 9.
a[3:9]
'HEMATI'

Q.2. Attempt any two of the following.
[10]
1. Write Python program that prints whether the given number is positive, negative
or zero.
>>>>>>>simpleeeee

2. Write Python program to nd the sum of rst n natural numbers.
>>>>>>>>>>>>>simple
3. Using Python accept the matrix
Find the Null space, Column space and rank of the matrix.
A.nullspace()
[ ]
A.columnspace()
[Matrix([
[ 1],
[-3],
[ 5],
[-4]]), Matrix([
[-3],
[ 9],
[-2],
[12]]), Matrix([
[ 2],
[-1],
[ 6],
[ 2]]), Matrix([
[-4],
[ 5],
[-3],
[ 7]])]

A.rank()
4


###################slip-23################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python program to nd the sum of rst n natural numbers
>>>>simple.
2. Write Python code to prints all integers between 1 to 100 that are divisible by 3
and 7.
>>>>>>>simple
3. Write Python code to prints all integers between 1 to n, which are relatively prime
to n.
>>>>>>>>>>>>simple
Q.2. Attempt any two of the following.
[10]
1. Write Python code to nd determinant, transpose and inverse of matrix.
>>>Simpleeeeee
2. Write Python program to nd the roots of the quadratic equation ax2 + bx + c = 0.
3. Using Python solve the following system of equations using LU – Factorization
method
3x − 7y − 2z = −7
−3x + 5y + z = 5
6x − 4y = 2
####################################slip-24##############################
Time: 3 hour
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python program to calculate the surface area of sphere A = 4πr2
>>>>>>>>>>>>>simplee.
2. Use Python code to nd the remainder after dividing by ‘n’ to any integers.
3. Write Python program to prints all integers between 1 to 50 that are divisible by 3
>>>>>>>>>>>>simple
and 7.
Q.2. Attempt any two of the following.
[10]
1. Write Python program to nd perfect square between 1 to 100.
>>>>>>>>>simple
2. Write Python program to prints whether the given natural number is divisible by 5
and less than 100
>>>>>>>>>>>>>simple.
3. Write Python program to diagonalize the matrix
and nd matrix P and D.
>>>>>>simplee
##########################slip-25########################################
Q.1. Attempt any two of the following.
Maximum Marks: 35
[10]
1. Write Python program to print the integers between 1 and 1000 which are multiples
of 7.
>>>>>>>>>>>>>>>simple
2. Write Python program to prints whether the given number is divisible by 3 or 5 or
7.
>>simple
3. Write Python code to nd A + B and B ∗ A for the given Matrices.
>>>>>>>>simplee

Q.2. Attempt any two of the following.
[10]
1. Write Python program to nd the area and circumference of a circle with radius r.
>>>>>>>>>>>>>>>simple
2. Use Python code to solve the following system of equations by gauss elimination
method
x + y + 2z = 7
−x − 2y + 3z = 6
3x − 7y + 6z = 1
3. Write Python code to nd eigen values, eigen vectors of the matrix and determine
whether the matrix is diagonalizable.
A=Matrix([[1,-1,1],[-1,1,-1],[1,-1,1]])
print(A)
Matrix([[1, -1, 1], [-1, 1, -1], [1, -1, 1]])

A.eigenvals()
{3: 1, 0: 2}
A.eigenvects()
[(0, 2, [Matrix([
[1],
[1],
[0]]), Matrix([
[-1],
[ 0],
[ 1]])]), (3, 1, [Matrix([
[ 1],
[-1],
[ 1]])])]
A.is_diagonalizable()
True


