letters = ["a", "b", "c"]

##Add
## to add item to the end of the list, use append()
letters.append("d")

##add item at a specific position - use insert()
letters.insert(0, "-")


##remove
##remove one item at the end of the list, use pop()
letters.pop()
letters.pop(0)  #remove at a specific position

##when you don't know which index of position, remove() will delete the first occurrance
## if you want to remove all the b's in the list, you will need to loop over the list and remove each b individually
letters.remove("b")

##another way to delete items in a list
##del by index[] or remove items in a range 
del letters[0]
del letters [0:3]

##if you want to remove all the items in the list, use clear()
letters.clear()

print(letters)