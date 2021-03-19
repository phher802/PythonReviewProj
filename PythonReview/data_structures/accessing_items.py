letters = ["a", "b", "c", "d"]

#print item at the end of the list
#print(letters[-1])

letters[0] = "A"

#print first item up to 3rd index, but excluding index 3
#print(letters[0:3])
#print(letters[2:])
#skip index 1
#print(letters[::2])

numbers = list(range(20))
#print(numbers) 

#returns all even numbers in the list
#print(numbers[::2])

#return the list starting at the end of the list
print(numbers[::-1])