#!/bin/python3

import math
import os
import random
import re
import sys



def timeConversion(s):
    time_parts = s.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2]) 

    if "PM" in s and hours != 12:
        hours += 12

    elif "AM" in s and hours == 12:
        hours = 0

    result = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
