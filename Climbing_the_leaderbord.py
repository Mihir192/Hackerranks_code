import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranks = []
    newranks = []
    for i in range(ranked_count):
        if ranked[i] in ranks:
            continue
        ranks.append(ranked[i])
    for j in player:
        if j in ranks:
            ranks.remove(j)
        ranks.append(j)
        ranks.sort(reverse= True)
        for k in range(len(ranks)):
            if ranks[k] == j:
                newranks.append(k+1)
        ranks.remove(j)
    return(newranks)    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
