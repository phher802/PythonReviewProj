#looping over lists
letters = ["a", "b", "c"]

##use for loop to loop over list
#for letter in letters:
   # print(letter)

##get the index of each item
##enumerate returns a tuple, which is read only
#for letter in enumerate(letters):
   # print(letter)

    ##to print index, print item of the tuple
   # print(letter[0], letter[1])

##can use list unpacking to unpack into two variables
#items = [0, "a"]
#index, letter = items  #unpack items

##can also unpack if items is a tuple list which is stored with ()
#items = (0, "a")

##unpack in foreach loop
for index, letter in enumerate(letters):
    print(index, letter)
