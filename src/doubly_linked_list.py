class _Node:
    """ Internal class. Not for public use. """

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        """
        Constructor for a doubly linked list.

        No arguments.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, data):
        """
        Places new 'data' at the beginning of the list.
        Time complexity = O(1).

        Arguments:
            data -- any data.
        """
        new_node = _Node(data)

        new_node.next = self.head  # link new_node to first
        if self.head:  # if not empty
            self.head.prev = new_node  # link first to new_node
        else:
            self.tail = new_node  # set tail to new_node
        self.head = new_node  # link heat fo new_node first
        self.size += 1

    def append(self, data):
        """
        Places new 'data' at the end of the list.
        Time complexity = O(1).

        Arguments:
            data -- any data.
        """
        if self.size == 0:
            self.add_first(data)
            return
        new_node = _Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def get(self, index):
        """
        Returns data with specified index.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index >= self.size or index < 0:
            print("ERROR: 'get' index {} is out of range".format(index))
            return
        current = self._find(index)
        return current.data

    def _find(self, index):
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node

    def pop(self, index):
        """
        Returns data with specified index
        and erases this data from the list.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if self.size == 0:
            return
        if index >= self.size or index < 0:
            print("ERROR: 'get' index {} is out of range".format(index))
            return
        current = self._find(index)
        data = current.data
        if self.size == 1:  # one element list
            self.head = None
            self.tail = None
        elif index == 0:  # if first
            self.head = current.next
            current.next.prev = None
        elif index == self.size - 1:  # if last
            current.prev.next = None
            self.tail = current.prev
        else:  # somewhere in the middle
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return data

    def clear(self):
        """
        Clear the list.

        No arguments.
        """
        self.__init__()

    def __repr__(self) -> str:
        """
        Returns string representation of the list.

        No arguments.
        """
        double_list = []
        current_node = self.head
        while current_node:
            double_list.append(current_node.data)
            current_node = current_node.next
        return str(double_list)

    def __len__(self):
        """
        Returns length of list.

        No arguments.
        """
        return self.size
