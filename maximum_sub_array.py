################################################################
#
# Find out the maximum sub-array of non negative numbers from an array.
# The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid# Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B)
#
# Example:
#
# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]
#
# NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
# NOTE 2: If there is still a tie, then return the segment with minimum starting index
#
#################################################################

#input = [1, 2, 5, -7, 2, 3]
input = [1, 2, 3, -7, 1, 4, 8, -1, 4, 7, 2]


def create_sub_array(input):
    count = 0
    out = []
    flag = True

    for i in input:
        if i > 0:
	    if flag:
	        out.append([i])
  	        flag = False
	    else:
   	        out[count].append(i)
        elif i < 0:
    	    count += 1
 	    flag = True
   
    return out

def largest_array():
    out = create_sub_array(input)
    print out
    max_arr = []
    for arr in out:
        if not max_arr:
	    max_arr = arr
	elif sum(max_arr) < sum(arr):
	    max_arr = arr
        elif sum(max_arr) == sum(arr):
	    if len(max_arr) < len(arr):
		max_arr = arr
    	    elif len(max_arr) == len(arr):
		if max_arr[0] > arr[0]:
		    max_arr = arr

    print max_arr
        
largest_array()

