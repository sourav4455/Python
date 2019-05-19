## Program to find factorial of a number.
## Use recursion to get the result

#!/bin/python

import math
import os
import random
import re
import sys

# Return the factorial of the number using Recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open('/tmp/out.txt', 'w')

    n = input()

    result = recur_factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

