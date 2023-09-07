#!/bin/python3

import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    n = len(arr)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += arr[i][i] - arr[i][n - 1 - i]
    
    return abs(diagonal_sum)


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
