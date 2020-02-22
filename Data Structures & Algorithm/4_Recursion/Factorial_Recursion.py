
## Recursion is used as a technique in which a function makes one or more calls to itself.
## Find the factorial of a number using Recursion

def rec_fact(n):

    # Base Case
    if n == 0:
        return 1

    else:
        return n * rec_fact(n-1)
