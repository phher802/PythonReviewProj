## this code can be changed in a cleaner code by using comprehension
values = []
for x in range(5):
    values.append(x * 2)

## list comprehension syntax: [expression for item in items]
## iterate over an list(items) and in each iteration we get an item, and then we do something with it (expression)
## items (list) --> item --> (do something) expression
values = [x * 2 for x in range(5)]
print(values)

## get a set:
values = {x * 2 for x in range(5)}
print(values)

## get a dictionary: use x as a key and x * 2 as the value
values = {x: x * 2 for x in range(5)}
print(values)

## comprehension can be used with list(), set(), and dict()