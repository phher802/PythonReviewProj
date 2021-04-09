from pprint import pprint
##find the most repeated character 
##1. find how many time a character is repeated
##what data structure is useful for storing this information?  a dictionary for key,value pairs

sentence = "This is a common interview question"
## define an empty dictionary
## iterate over the string, get each character, and update its frequency in the dictionary
## use a for loop to iterate of the string, get each character,and update the frequency in the new dict
## if we don't have it, then need to set frequency to 1, otherwise we need to increment the frequency by 1

 ##see if we have the charachter in the dict, 
       ## if yes, get the value and increment by 1
             ##otherwise add it to the dict by setting to one
char_frequency = {}
for char in sentence:
    if char in char_frequency:          
        char_frequency[char] += 1  
    else: 
        char_frequency[char] = 1  
print(char_frequency)

## make it more readable by using pretty printing module called pprint
## pprint module gives you more control over printing on the terminal
## syntax: pprint(dict, width)
pprint(char_frequency, width=1)

## dictionaries are unrdered collections, but they can not be sorted
## you can only sort list
## so you need to pull out the items of the dictionary and put them into a list for sorting
## which means, take out each key/value pair, convert it into a tuple, then put it into a list

## call sorted function; .items() return all the key/value pairs as tuples
print(sorted(char_frequency.items()))
## list is not sorted because tuples can't be sorted, so you can pass in a lambda expression as a 2nd argument
## the lambda expression takes a keyvalue pair and returns the value which is in the index [1] (becaue the key in keyvalue is in the [0] index)
## the value is the frequency which is used for sorting
pprint(sorted(char_frequency.items(), key=lambda kv:kv[1]))

## answer is that T is the least repeated and i and space are the most repeated

## to reverse the sorting, pass in a 3rd argument with reverse = true 
## save it as a list
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv:kv[1], reverse = True)
print(char_frequency_sorted[0])