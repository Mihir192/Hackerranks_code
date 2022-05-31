import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    count = 0
    a = []
    for i in s:
        if i in a:
            continue
        x = s.count(i)
        a.append(i)
        if x % 2 != 0:
            count += 1
            
        if count > 1:
       
            return("NO")

    return("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
