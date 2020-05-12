from singly_linked_list import LinkedList
from singly_linked_list import Node

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert_end(value)
        self.size += 1
        print(self.size)

    def dequeue(self):
        if self.size == 0:
            return 'this should not show'
        self.size -= 1
        return self.storage.delete_head()
