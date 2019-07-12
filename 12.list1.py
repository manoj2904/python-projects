#program using list
list=[1,2]

#to add elements to the list
list.append(3)
print("\nList after addition of elements :" +str(list))

#to add tuple in a list
tup1=('a','b')
list.append(tup1)
print("\nList after addition of tuples :" +str(list))

#to add a list in a list
list1=['appple','mango']
list.append(list1)
print("\nList after addition of list :" +str(list))

#to insert an element into the list
list.insert(3,'x')
print("\nList after insertion of element :" +str(list))
