import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    arr = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i] == a[j]:
                k = (i - j)
                if k < 0:
                    k = k *(-1)
                arr.append(k)
    if len(arr) == 0:
        return(-1)
    arr.sort()
    return arr[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
