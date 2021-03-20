## Arrays takes less memory and performs faster but
##use arrays only when there is a large list of numbers AND there are performance problems
## you can try to solve the problem by replacing the list with an array
## but if you don't have any performance problems, don't try to optimize your list
## which means don't solve a problem that doesn't exist

## import array from array module
from array import array

## array() syntax: <typecode>, <list>
## google array typecode to get list of typecode in python
numbers = array("i", [1, 2, 3])

## like list, can use the following:
numbers.append()  ## append to end of the list
numbers.pop()
numbers.remove()
numbers.insert()  #add at a specific index
numbers[0]    ##access items at the index in the array
numbers[0] = 1.0  ## changing the index at 0 to 1.0 will get an error because the types must be the same; int != float