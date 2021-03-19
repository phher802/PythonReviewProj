numbers = [3, 51, 2, 8, 6]

## sort the list in ascending order by calling .sore()
numbers.sort()

##sort list in descending order
numbers.sort(reverse=True)
print(numbers)

## built-in function called sorted(), which returns a new list, pass passing in the list, and 
sorted(numbers)

## to change the sort order
sorted(numbers, reverse=True)

print(sorted(numbers))

## sorting when you have a list of tuples, e.g. product name and its price

items = [
    ("Product1", 10),
    ("Product2", 9), 
    ("Product3", 12)
]
## nothing will change b/c python will not know how to sort this list
items.sort()
print(items)

##define a function to sort these kind of lists
##pass in an item of the tuple, to sort by price
def sort_item(item):
    return item[1]

## this function will take an item and return its price
## now python is dealing a list of numbers and can easily sort the list

##pass a reference to the function as the key parameter -- this is done by not using the ()
##when python attempts to sort the list, it gets each item and it will pass each item for a sort function
items.sort(key=sort_item)
print(items)

##use lambda functions for cleaner code -- go to lambda functions file
