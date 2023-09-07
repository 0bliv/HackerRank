#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    n = len(grades)
    resp = []
    for i in grades:
        if i >= 38:
            remainder = i % 5
            next_multiple = i + (5 - remainder) if remainder != 0 else i
            if (next_multiple - i) < 3:
                resp.append(next_multiple)
            else:
                resp.append(i)
        else:
            resp.append(i)
    return resp    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
