
######################################################################
#
# Largest perfect square number in an Array
# Given an array of n integers. The task is to find the largest number which is a perfect square.
# Print -1 if there is no number that is perfect square.
#
# Examples:
#
# Input : arr[] = {16, 20, 25, 2, 3, 10}
# Output : 25
# Explanation: 25 is the largest number that is a perfect square.
#
# Input : arr[] = {36, 64, 10, 16, 29, 25|
# Output : 64
#
#
######################################################################

#!/bin/python

import math

arr = [16, 20, 25, 2, 3, 10]
arr1 = [36, 64, 10, 16, 29, 25]

def largest_perfect_square(arr):
    out = 0
    for num in arr:
        d = math.sqrt(num)
        if d * d == num:
            if num > out:
                out = num
    print out

largest_perfect_square(arr1)

