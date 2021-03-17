items = [
    ("Product1", 10),
    ("Product2", 9), 
    ("Product3", 12)
]

##list comprehension is an even cleaner way of writing map() and filter() functions
## basic syntax: 
## create an empty bracket to define a new list: []
## then apply an expression to each item: [<expression> for item in items]
prices = list(map(lambda item: item[1], items))
## to
prices = [item[1] for item in items]

## the filter example:
filtered = list(filter(lambda item: item[1] >= 10, items))
##to: (since we don't want to map the list of items to a list of prices, the expression would just be the "item" itself)
filtered = [item for item in items if item[1] >= 10]