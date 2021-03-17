#data structures
letters = ["a", "b", "c"]

#list in a list, a matrix is a two dimensional list
matrix = [[0, 1],[2,3]]

#list of a hundred zeros
zeros = [0] * 100
#print(zeros)

combined = zeros + letters
#print(combined)

#lists can have different data types
#list function that takes a iterable list(iterable)
#create a list from 0 to 20 (this is up to 20 but not including 20)
numbers = list(range(20))
#print(numbers)
chars = list("hello world")
#print (chars)
#print(len(chars))