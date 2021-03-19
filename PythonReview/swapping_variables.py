## swap two variables 
x = 10
y = 11

## solution:

z = x  ## store x in a new variable as a backup
x = y   ## overwrite x with y adn copy y to x
y = z   ##overwrite y wtih z which has the old x stored

print("x", x)
print("y", y)

## pyton way:

a = 10
b = 11

a , b = b, a    ## this is the way to swap variables, and it is also defining a tuple
a, b = (11, 10)   ## this is the equivalent
print("a", a)
print("b", b)

## it is also unpacking b/c you define the tuple on the right 
## and unpacking it on the left side (set tuple items to variables with the left side)