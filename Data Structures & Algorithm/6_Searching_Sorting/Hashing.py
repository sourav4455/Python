
## A hash table is a collection of items which are stored in such a way as to make it easy to find them later.
## Each position of the hash table, slots, can hold an item and is named by an integer value starting at 0.
## The mapping between an item and the slot where that item belongs in the hash table is called the hash function.
##

class HashTable(object):

    def __init__(self,size):

        self.size = size
        self.slots = [None] * self.size
        self. data = [None] * self.size