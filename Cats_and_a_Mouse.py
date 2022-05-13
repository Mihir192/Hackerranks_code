import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if (z - x) < 0:
        A  = (z-x)* -1
    else:
        A = (z-x)
    if (z - y) < 0:
        B  = (z-y)* -1
    else:
        B = (z-y)
    if A == B:
        return ("Mouse C")
    elif A < B:
        return("Cat A")
    else:
        return("Cat B")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
