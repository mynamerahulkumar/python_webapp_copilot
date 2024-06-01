from collections import deque

from collections import deque

class Queue:
    """
    A class representing a queue data structure.

    Attributes:
        items (deque): A deque object to store the items in the queue.

    Methods:
        is_empty: Check if the queue is empty.
        enqueue: Add an item to the end of the queue.
        dequeue: Remove and return the item at the front of the queue.
        size: Get the number of items in the queue.
    """

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Returns:
            item: The item at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items.popleft()

    @property
    def size(self):
        """
        Get the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)