import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    num = 0
    vally = 0
    for i in range (steps):
        if num <= 0:
            if path[i] == "D":
                num -= 1
            else:
                num += 1
            if num == 0:
                vally +=1
        else:
            if path[i] == "D":
                num -= 1
            else:
                num += 1
                        
        
    return  vally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
