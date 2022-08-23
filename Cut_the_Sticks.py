#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):

    length = [len(arr)]
    while len(arr) > 1:
        temparr = []
        arr.sort()
        t  = arr[0]
        for j in range(len(arr)):
            if arr[j] == t:
                continue
            temparr.append(arr[j] - t)
        arr = temparr
        if len(arr) == 0:
            break
        length.append(len(arr))
    return(length)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
