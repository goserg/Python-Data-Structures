class _Node:
    """ Internal class. Not for public use. """

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    """
    Queue implemented on Double linked list base.
    Time complexity O(1) for push, peek and pop methods.
    Time complexity O(n) for search method.
    """
    def __init__(self):
        """
        Constructor for a queue.

        No arguments.
        """
        self.head = _Node()
        self.tail = _Node()
        self.tail.prev = self.head
        self.size = 0

    def push(self, data):
        """
        Add data to the queue.
        Time complexity = O(1).
        """
        new_node = _Node(data)
        if self.head.next:
            new_node.next = self.head.next
            new_node.next.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        if self.tail.prev == self.head:
            self.tail.prev = new_node
        self.size += 1

    def pop(self):
        """
        Return data prom the top and remove it from the queue.
        Return None if queue is empty.
        Time complexity = O(1).
        """
        if self.size > 0:
            ret = self.tail.prev.data
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = None
            self.size -= 1
            return ret
        return None

    def peek(self):
        """
        Return data from top the queue.
        Return None if queue is empty.
        Time complexity = O(1).
        """
        if self.size > 0:
            return self.tail.prev.data
        return None

    def search(self, data):
        """
        Search for a data in the queue and get its distance from the top.
        This method starts the count of the position from 1.
        Return None if data not in the queue.
        Time complexity = O(n).
        """
        if self.size == 0:
            return None
        current = self.tail.prev
        count = 1
        while current:
            if current.data == data:
                return count
            count += 1
            current = current.prev
        return None

    def is_empty(self):
        """
        Return False if the queue is empty else return True.
        """
        return True if self.size == 0 else False

    def clear(self):
        """
        Remove all data from the stack.
        """
        self.tail.prev = self.head
        self.head.next = None
        self.size = 0

    def __str__(self):
        """
        Returns string representation of queue.

        No arguments.
        """
        queue = []
        current = self.head
        while current.next:
            current = current.next
            queue.append(current.data)
        return str(queue)

    def __len__(self):
        """
        Returns length of queue.

        No arguments.
        """
        return self.size
