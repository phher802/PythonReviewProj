items = [
    ("Product1", 10),
    ("Product2", 9), 
    ("Product3", 12)
]

##transform tuple list in the price of the items; transform list into list of numbers
## you can do this by:

prices = []
for item in items:
    prices.append(item[1])
print(prices)

## map() is a built-in function; use for cleaner code to acheive same result
## map() takes two parameters: map(func, iterables) 
## pass a lambda function as the function parameter: lambda <parameter>:<expression>
##lambda function will transform each item in the list
##this map function will iterate over the items list and it will call the lambda function on each item in the list
map(lambda item: item[1], items)

## assign it to a variable

x = map(lambda item: item[1], items)
print(x)

## this will return an iterable so iterate over x

for item in x:
    print(item)

## you can also convert the map function into a new list

prices = list(map(lambda item: item[1], items))
print(prices)