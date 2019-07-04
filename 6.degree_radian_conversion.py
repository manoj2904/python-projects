#conversion between degree and radian
x=int(input("press 1 to convert degree to radian and 2 to convert radian to degree :"))
pi=22/7
if x==1:
    deg=float(input("Enter the value of the degree that you want to convert :"))
    rad=float(deg*pi/180)
    print("%f is the value in radians" %rad)
elif x==2:
    rad=float(input("Enter the value of the radian that you want to convert :"))
    deg=float(rad*180/pi)
    print("%f is the value in radians" %deg)
else:
    print("you didn't press 1 or 2, please try again")
