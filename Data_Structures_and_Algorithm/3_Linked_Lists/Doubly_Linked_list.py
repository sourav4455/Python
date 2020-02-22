
## Doubly Linked List

class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.prev_node = None
        self.next_node = None

## Run the code like below
# a = DoublyLinkedListNode(1)
# b = DoublyLinkedListNode(2)
# c = DoublyLinkedListNode(3)

# a.next_node = b
# b.prev_node = a
# b.next_node = c
# c.prev_node = b