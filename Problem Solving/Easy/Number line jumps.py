#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Check if kangaroos start at the same position with the same jump rate
    if x1 == x2 and v1 == v2:
        return "YES"
    
    # Check if kangaroos start at different positions and have the same jump rate
    if x1 != x2 and v1 == v2:
        return "NO"
    
    # Check if kangaroos have different jump rates and the relative distance changes accordingly
    if (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) >= 0:
        return "YES"
    
    return "NO"
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
