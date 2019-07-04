#to get the sqaure root of a quadratic function
from math import sqrt
print("Quadratic function: a*x^2+bx+c")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
r=b**2-4*a*c
if r>0:
    numofroots=2
    x1=(((-b)+sqrt(r))/(2*a))
    x2=(((-b)-sqrt(r))/(2*a))
    print("%f and %f are the roots" %(x1,x2))
elif r==0:
    numofroots=1
    x=-b/(2*a)
    print("%f is the root" %x)
else:
    numofroots=0
    print("no roots, discriminant <0")
