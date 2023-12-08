#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Split the time string into hours, minutes, and AM/PM
    time_parts = s.split(':')
    hours = int(time_parts[0])
    minutes = time_parts[1]
    seconds = time_parts[2][:2]  # Extract seconds part
    am_pm = time_parts[2][-2:]  # Extract AM/PM part

    # Convert to 24-hour format
    if am_pm == 'AM' and hours == 12:
        hours = 0  # Special case: 12 AM becomes 00:00
    elif am_pm == 'PM' and hours != 12:
        hours += 12  # Add 12 hours for PM times (except 12 PM)

    # Format the time in 24-hour format
    military_time = '{:02d}:{:s}:{:s}'.format(hours, minutes, seconds)
    return military_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
