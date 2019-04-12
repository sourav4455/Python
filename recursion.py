## Question :
## --------

## Write a recursion function which counts number of time a number "4" appeared in an numerical input by user. 
## Do not us count funciton or for loop. 
## Use recursion to complete this.


res = []
def rec(num):
  aa = num % 10
  bb = num / 10

  if aa == 4:
       res.append(aa)

  if bb != 0:
       return rec(num/10)

  print len(res)


rec(124343546747)
