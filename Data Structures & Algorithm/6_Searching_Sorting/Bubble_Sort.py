
## The Bubble sort makes multiple passes through a list. It compares adjacent items and exchanges
## those that are out of order. Each item "bubbles" up to the location where it belongs.

def bubble_sort(arr):

    for n in range(len(arr)-1,0,-1):
        #print 'This is the n: ',n
        for k in range(n):
            #print 'This is the k index check: ',k
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
