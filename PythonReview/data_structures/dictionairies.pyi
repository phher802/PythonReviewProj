## dictionaries a very powerful data structure that uses key value pairs
## dictionary maps a key to a value like a phone book maps a name to a contact number

point = {"X": 1, "y": 2}
## keys has to be immutable types, so string is often used
## value can be any type
## can use dict() function to create a dictionary

## redefine point variable by passing in keyword arguments
## defining a dictionary w/this syntax is cleaner by avoiding the quotes 
point = dict(x=1, y=2)
print(point)
## b/c dictionaries are collections of key,value pairs, cannot access dictionary with an index number
## must access by indicating key 
print(point["x"])

## can change the value of a key
point["x"] = 10
print(point)

## add a new key
point["z"] = 20
print(point)

## when reading a value, if the key doesn't exist, you'll get an error
## so you should check for the existence of the item first
if "a" in point:
    print(point["a"])

##another solution to check is use the get method, and pass in a default 0 if a doesn't exist
print(point.get("a", 0))

## to delete use the del method
del point["x"]
print(point )

## loop over dictionaries
## simple statement:
for x in point:
    print(x)

## the loop variable x holds the key so better to emphasize key as:
for key in point:
    print(key)

## can print the value associated with the key as well by passing in point of key:
for key in point:
    print(key, point[key])


## another way to iterate of a dictionary, which returns a tuple of the key and the value:
for x in point.items():
    print(x)

## unpack this tuple like so:
for key, value in point.items():
    print(key, value)