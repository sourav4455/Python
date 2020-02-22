
## A Deque, also known as double-ended queue, is an ordered collection of items
## similar to the queue. New items can be added/removed either from the front or rear.
## This hybrid linear structure provides all the capabilities of Stack and Queue in single
## data structure.

class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)