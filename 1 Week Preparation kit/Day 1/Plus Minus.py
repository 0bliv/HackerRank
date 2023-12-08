#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_0, count_p, count_n = 0, 0, 0
    n = len(arr)
    
    for i in arr:
        if i > 0:
            count_p+=1
        elif i < 0:
            count_n+=1
        else:
            count_0+=1
            
    print("{:.6f}".format(count_p / n))
    print("{:.6f}".format(count_n / n))
    print("{:.6f}".format(count_0 / n))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
