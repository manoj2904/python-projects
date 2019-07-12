#program to remove an element from a list
list=[1,2,3,4,5,6,7,8,9,10,11,12]
print("\nInitial list = " +str(list))

#to remove the 9 in the list
list.remove(9)
print("\nThe list after removing an element in the list : " +str(list))

#to remove elements using the iteration operation
for i in range(1,5):
    list.remove(i)
print("\nlist after removing elements using iteration : " +str(list))

#to remove a list using pop method
#to remove the last element in the list
list.pop()
print("\nThe list after poping an element in the list : " +str(list))
#to remove the 3rd element in the list
list.pop(2)
print("\nThe list after poping an element in the list : " +str(list))
