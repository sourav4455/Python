
## The Selection sort improves on the bubble sort by making only one exchange for every pass
## throughout the list. A selection sort looks for the largest value as it makes a pass, places
## it in proper location.

def selection_sort(arr):

    for fillslot in range(len(arr)-1,0,-1):

        positionOfMax = 0

        for location in range(1,fillslot+1):

            