# example 3
# Write pseudo code that performs the following: Ask a user to enter a number. If the number is between 0
#and 10, write the word blue. If the number is between 10 and 20, write the word red. if the number is between
#20 and 30, write the word green. If it is any other number, write that it is not a correct color option.

def enter_num():
    x = int(input("Enter a number"))
    if 0 < x < 10:
        print("blue")
    elif 10 <= x < 20:
        print("red")
    elif 20 <= x < 30:
        print("green")
    else: 
        print("that is not a correct color option")

#enter_num()

#example 4
#Write pseudo code to print all multiples of 5 between 1 and 100 (including both 1 and 100).

new_list = []
for i in range(1,101):
    if i == 1:
        new_list.append(i)
    if i % 5 == 0:
        new_list.append(i)       
   
print(new_list)

