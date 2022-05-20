import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = 0 
    lst = []
    for i in range(n):
        x  = ar.count(ar[i])
        
        if ar[i] in lst:
            continue
        lst.append(ar[i])
        if x > 1:
            if x % 2 !=0:
                count += x - (x%2)
            else:
                count += x
    return (count//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
