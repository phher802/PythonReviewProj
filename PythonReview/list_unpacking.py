#get individual items in the list and assign them to different variables

#example of how to assign
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

#using list unpacking is cleaner
#unpack into multiple variables
#variables on the left s/b equal to number of items in the list; will get error if not equal
first, second, third = numbers

#if there are too many items in the list and we only want to assign the first two, use *other
#the items in other is packed into a list stored separately
new_numbers = [1, 2, 3, 5, 6, 7, 9]
first, second, *other = new_numbers
#print(first)
#print(other)

#if you want first and last item
first, *other, last = new_numbers
print(first, last)
print(other)