list1 = [1, 2, 3]
list2 = [10, 20, 30]

## combine these two list into a single tuple list like this: [(1, 10), (2, 20), (3, 30)]
## cannot use map() or filter() functions because they work with single lists
## use the built-in zip() function: it takes in multiple lists or iterables

print(zip(list1, list2))

## a zip object will return that can be iterated over so can turn it into a list right away

print(list(zip(list1, list2)))

## since the zip() function can take in one or more iterable, a string can also be passed in like so:

print(list(zip("abc", list1, list2)))

## abc is then spread over the tuples