#
# Lilah has a string, s , of lowercase English letters that she repeated infinitely many times.
#
# Given an integer, n , find and print the number of letter a's in the first n letters of Lilah's infinite string.
# For example, if the string  s='abcac' and n = 10 , the substring we consider is abcacabcac , the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.
#
# Input Format
# The first line contains a single string, s . 
# The second line contains an integer, n .
#
# Output Format
# Print a single integer denoting the number of letter a's in the first n letters of the infinite string created by repeating s infinitely many times
#
# Sample Input 0
# aba
# 10
#
# Sample Output 0
# 7
#
# Explanation 0 
# The first n = 10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we print 7 on a new line.
#
# Sample Input 1
# a
# 1000000000000
#
# Sample Output 1
# 1000000000000
#
# Explanation 1 
# Because all of the first n = 1000000000000 letters of the infinite string are a, we print 1000000000000 on a new line.
#
#
############################################################################


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    var_a = s.count('a')
    count = var_a * (n / len(s)) 
    
    rem_num = n % len(s)
    for i in s[:rem_num]:
        if i == 'a':
            count += 1

    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

