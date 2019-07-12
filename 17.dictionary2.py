# to remove elements from a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# to remove a particular item
print(squares.pop(4))
print(squares)

# to delete a particular item
del squares[5]
print(squares)

# to remove all items
squares.clear()
print(squares)

# to delete the dictionary itself
del squares
