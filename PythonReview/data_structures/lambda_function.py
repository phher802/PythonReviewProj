##sorting when you have a list of tuples, e.g. product name and its price
items = [
    ("Product1", 10),
    ("Product2", 9), 
    ("Product3", 12)
]

##lambda expression - a one line anonymous function that can pass other functions
## improve items.sort(key=sort.item) without having to define the sort_item function

##instead of:
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)


#do this: syntax:  key=lambda <parameter>:<expression>

items.sort(key=lambda item:item[1])
print(items)