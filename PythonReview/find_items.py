letters = ["a", "b", "c"]

##when you want to find the index of an object/item of a list
#print(letters.index("a")) 

##when you try to find an item that doesn't exist in the list, you'll get an error
#print(letters.index("d"))

## prevent this by checking to see if the item is in the list 
if "d" in letters:
    print(letters.index("d"))

## can also use count, which will return the number of occurrences of the item
print(letters.count("d"))