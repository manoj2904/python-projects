#to find all the divisors of a number
num=int(input("Enter the number :"))

#to list the numbers from 1 to num
x=range(1,num+1)
print("the divisors are")
for div in x:
    if num%div==0:
        print(div)
