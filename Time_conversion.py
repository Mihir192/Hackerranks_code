import math
import os
import random
import re
import sys

def timeConversion(s):
    if s[-2:] == "AM" and s[:2]== "12":
        s = "00" +s[2:]  
    elif s[-2:] == "PM" and s[:2] != "12":
        x = int(s[:2]) + 12
        s = str(x) + s[2:]

    return(s[:-2])    
    
    return s   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
