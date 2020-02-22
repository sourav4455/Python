
## Create a function which return a sum of all the individual digits in that integer.
## For Example: if n=4326, return 4+3+2+6

def sum_func(n):

    # Base case
    if n == 0:
        return 0
    else:
        return n%10 + sum_func(n/10)