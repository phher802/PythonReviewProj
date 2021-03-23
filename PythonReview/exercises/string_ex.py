
#Task: Given a string,S, of length N that is indexed from 0 to N -1, 
# print its even-indexed and odd-indexed characters as 2 space-separated 
# strings on a single line (see the Sample below for more detail).
#Note:  is considered to be an even index.
#Example: s = adbcf Print abc def
s = "adbecf"
s_sorted = sorted(s)
print(s_sorted)

string_one = "Hacker"
string_two = "Rank"


for i in string_one:
    print(string_one[::2], string_one[1::2])
    

## solution:

for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])