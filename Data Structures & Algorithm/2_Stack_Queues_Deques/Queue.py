
## A Queue is an ordered collection of items where the addition of new items happens at one
## end, called the "rear" and removal of existing items occurs at the other end, commonly
## called the "front". (FIFO)

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)