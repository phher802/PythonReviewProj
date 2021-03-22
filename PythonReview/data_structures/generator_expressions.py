## use generator expression to create a generator object when dealing with a large data set, 
## or potentially an infinite stream of data
## it is more efficient to store data in a generator object
## use for loop to iterate over the generator object and for each iteration, you can spit out new values
## use parenthesis around a comprehension expression to get an generator object
## 
##this module will get the size of a generator object in bytes of memory
from sys import getsizeof

##this creates a generator object that takes 112 bytes
values = (x * 2 for x in range(100))
print("gen:", getsizeof(values))
## generator objects don't store all the items in memories so you won't be able to get the total of number of items you're working with
## e.g. len() won't work
#print(len(values))
## use for loop to generator objects to generate new value and access 
## can only access items/values when you iterate over the items
for x in values:
    print(x)


##this create a list that takes 920 bytes of memory
values_2 = [x * 2 for x in range(100)]
print("list:", getsizeof(values_2))

