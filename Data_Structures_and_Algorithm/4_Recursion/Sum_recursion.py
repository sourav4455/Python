
## Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer.
## if n =4 , return 4+3+2+1+0 = 10

def rec_sum(n):

    # Base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)