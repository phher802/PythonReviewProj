items = [
    ("Product1", 10),
    ("Product2", 9), 
    ("Product3", 12)
]

##we want to return the items that are equal to or great than $10
##use the built-in filter() function; it has two parameters: function or none, iterable -> filter object
##use the lambda function; syntax: lambda <parameter>:<expression>

filter(lambda item: item[1] >= 10, items)

##then store the function in a variable

x = filter(lambda item: item[1] >= 10, items)
print(x)

## if lambda function returns true, a filter object will return
## loop over the filter object by turning the function into a list

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


