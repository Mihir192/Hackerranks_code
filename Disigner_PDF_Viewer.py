import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    lst = []
    x = ord(word[-1]) - 96
    count = 0
    
    for i in range(len(word)):
        if word[i] == " ":
            count += 0
        else:
            count += 1
            x = ord(word[i]) - 97
            lst.append(h[x])
    lst.sort()
    area = (lst[-1] * 1 * count)
    return (area)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
