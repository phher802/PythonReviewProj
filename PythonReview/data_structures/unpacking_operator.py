##

numbers = [1, 2, 3]
## to print individual numbers or get an output 1, 2, 3
## use unpacking operator *
print(*numbers)

## another useful application of unpacking is when creating lists
##instead of this:
values = list(range(5))
print(values)

## use unpacking & can also unpack a string
values_2 = [*range(5), *"hello"]
print(values_2)
print(values_2[1])

## can combine multiple lists
first = [1, 2]
second = [3]
third = [*first, "a", *second, *"hey"]
print(third)

## can also unpack dictionairies by using two ** or combine multiple dicts
one = {"x": 1}
two = {"x":10, "y": 2}
combined = {**one, **two, "z": 1}
print(combined)

##the last value of the same key will be used in the new dict
## use unpack operator to take out individual values in any iterable