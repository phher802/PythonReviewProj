## tuples is a read only list and can be defined with parenthesis or w/o parenthesis but has commas

point = (1, 2, 3)
##or
point_two = 4, 5, 6,
print(type(point)) ##find the type of this list

## can concatenate lists into tuples
point_three = point + point_two
point_four = (1, 2) + (3, 4)

## use muliplier to repeat a tuple
point_five = (1, 2) * 3

print(point_three)
print(point_four)
print(point_five)

##convert a list to a tuple
point_six = tuple([1, 2, 3])
print(point_six)

##create each character as a tuple item
point_seven = tuple("Hello world")  
print(point_seven)

##create each word as a tuple item; use brackets
point_eight = tuple(["hello", "world"])   
print(point_eight)

## get the items in a tuple
print(point_eight[0])
print(point_eight[0:2])

## unpack the tuple by defining variables for tuple items
point_ten = (1, 2, 3)
x, y, z = point_ten

##use in operator to check existence of an item
if 10 in point_ten:
    print("exists")
else:
    print("does not exists")

## a good example of when to use tuples in the real world is when you work with a sequence
## and don't want to accidentally add or remove any existing items from the list