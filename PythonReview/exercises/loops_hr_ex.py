##hackerrank loop exercise

#Given an integer,n, print its first 10 multiples. 
# Each multiple n x i (where 1 <= i <= 10) should be printed on a 
# new line in the form: n x i = result.

import math
import os
import random
import re
import sys

#n = int(input())

#print( *['%d x %d = %d'%(n, i, n*i) for i in range(1, 11)], sep="\n" )
n = 3
for i in range(1, 11):
    print(n, "x", i, "=", n*i)