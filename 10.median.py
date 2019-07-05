#to find the median of the given elements
list=[10,23,35,44,56,45]

#sorting the list in ascending order
list.sort()

length=len(list)
if length%2==0:
    median1=list[length//2]
    median2=list[length//2-1]
    median=(median1+median2)/2
else:
    median=list[length//2]
print("the median is " +str(median))
