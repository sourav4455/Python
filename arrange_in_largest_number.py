############################################################################################

## Given a list of non negative integers, arrange them such that they form the largest number.
#
#  For example:
#
## Given [3, 30, 34, 5, 9], the largest formed number is 9534330

############################################################################################

input = [3, 30, 34, 5, 9]

def arrange_largest(input):
    str_num = "".join(map(str,input))             ## output = '3303459'
    list_num = map(int,str(str_num))              ## output = [3,3,0,3,4,5,9]
    list_num.sort(reverse = 1)                    ## output = [9,5,4,3,3,3,0]
    final_out = int("".join(map(str,list_num)))   ## output = 9543330
    print final_out

arrange_largest(input)
