class _Node:
    """ Internal class. Not for public use. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        """
        Constructor for a linked list.

        No arguments.
        """
        self.head = _Node()
        self.size = 0

    def add_first(self, data):
        """
        Places new 'data' at the beginning of the linked list.
        Time complexity = O(1).

        Arguments:
            data -- any data.
        """
        new_node = _Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def append(self, data):
        """
        Places new 'data' at the end of the linked list.
        Time complexity = O(n).

        Arguments:
            data -- any data.
        """
        current = self.head
        while current.next:
            current = current.next
        current.next = _Node(data)
        self.size += 1

    def get(self, index):
        """
        Returns data with specified index.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index >= self.size:
            print("ERROR: 'get' index {} is out of range".format(index))
            return
        current_index = 0
        current = self.head
        while current_index <= index:
            current_index += 1
            current = current.next
        return current.data

    def pop(self, index):
        """
        Returns data with specified index
        and erases this data from linked list.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index < 0 or index >= self.size:
            print("ERROR: 'pop' index {} is out of range".format(index))
            return
        current_index = 0
        current = self.head
        while current_index <= index:
            current_index += 1
            last = current
            current = current.next
        ret = last.next.data
        last.next = current.next
        self.size -= 1
        return ret

    def clear(self):
        """
        Clear linked list.

        No arguments.
        """
        self.head.next = None
        self.size = 0

    def append_list(self, data):
        """
        Places new data from list at the end of the linked list.
        Time complexity = O(n).

        Arguments:
            data -- any list.
        """
        try:
            _ = iter(data)
        except TypeError:
            print("ERROR: list is not iterable")
            return
        if len(data) == 0:
            print("ERROR: empty list")
            return
        current = self.head
        while current.next:
            current = current.next
        for i in data:
            current.next = _Node(i)
            current = current.next
            self.size += 1

    def __str__(self):
        """
        Returns string representation of linked list.
        
        No arguments.
        """
        linked_list = []
        current = self.head
        while current.next:
            current = current.next
            linked_list.append(current.data)
        return str(linked_list)

    def __len__(self):
        """
        Returns length of linked list.

        No arguments.
        """
        return self.size
