## Sets are an unordered collection of items with no duplicates
## sets are defined by curly brackets {}
## can use set function to get a list w/0 duplicates

numbers = [1, 1, 2, 3, 4]  ## remove duplicates by setting the set function
uniques = set(numbers)
print (uniques)

new_nums = {1, 5} ##deine a new set of items w/ curly brackets
new_nums.add(6)
print(new_nums)

new_nums.remove(1)
print(new_nums)

len_new_nums = len(new_nums)
print(len_new_nums)

## sets has powerful mathmatical operations
first = set(numbers)
second = {1, 5}

print(first | second)  ## get the union of two sets, w/o duplicates
print(first & second)  ## return a new set of items that are the same in the two sets
print(first - second)  ## get the difference between the two sets, which are numbers in the first set that are not in the 2nd set
print(first ^ second)  ## return symetric difference, which are numbers that are either in the first or 2nd set but not both

## since sets are unordered, sets cannot be accessed by the index
## CAN check to see if there is a specific item in the set by using the in function:

if 1 in first:
    print("yes")
