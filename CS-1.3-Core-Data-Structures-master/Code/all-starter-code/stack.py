#!python

from collections import deque
from linkedlist import LinkedList

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):
    ''' LAST IN FIRST OUT '''

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.head == None

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Runtime: O(1) bc we add to the top and we know where that is at all times [TODO]"""
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        
        if self.list.head != None:
            return self.list.get_at_index(0)
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) Because we know where the top of the stack is always [TODO]"""
        # TODO: Remove and return top item, if any
        node = self.list.get_at_index(0)
        self.list.delete(self.list.get_at_index(0))
        return node
        

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):
    ''' LAST IN FIRST OUT '''

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = deque([])
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) Because we always know where the top of the stack is [TODO]"""
        # TODO: Insert given item
        self.list.appendleft(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if len(self.list) == 0:
            return None
        else:
            return self.list[0]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – We know where the top of the stack is [TODO]"""
        # TODO: Remove and return top item, if any
        if len(self.list) == 0:
            raise ValueError('List index out of range.')
        else:
            return self.list.popleft()
    
    def dequeue(self):
        if len(self.list) == 0:
            raise ValueError('List index out of range.')
        else:
            return self.list.pop()


    def enqueue(self, item):
        self.list.append(item)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
