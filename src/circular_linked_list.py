class _Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class CircularLinkedList:
    def __init__(self):
        """
        Constructor for a circular linked list.

        No arguments.
        """
        self.tail = None
        self.size = 0

    def add_first(self, data) -> None:
        """
        Places new 'data' at the beginning of the list.
        Time complexity = O(1).

        Arguments:
            data -- any data.
        """
        new_node = _Node(data)
        if self.size == 0:
            new_node.next = new_node
            self.tail = new_node
        else:  # list is not empty
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.size += 1

    def append(self, data) -> None:
        """
        Places new 'data' at the end of the list.
        Time complexity = O(1).

        Arguments:
            data -- any data.
        """
        new_node = _Node(data)
        if self.size == 0:
            new_node.next = new_node
        else:  # list is not empty
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def step(self, n=1) -> None:
        """
        Rotates the list by moving tail pointer forward for n steps.

        Arguments:
            n -- number of steps (default 1).
        """
        if self.size > 0:
            for _ in range(n):
                self.tail = self.tail.next

    def get(self, index: int):
        """
        Returns data with specified index.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index < 0 or index > self.size - 1:
            print("ERROR: 'get' index {} is out of range".format(index))
            return
        if self.size == 1:
            return self.tail.data
        count = 0
        current = self.tail.next
        while count < index:
            current = current.next
            count += 1
        return current.data

    def pop(self, index: int):
        """
        Returns data with specified index
        and erases this data from the list.
        Time complexity = O(n).

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index < 0 or index > self.size - 1:
            print("ERROR: 'get' index {} is out of range".format(index))
            return
        self.size -= 1
        if self.size == 0:
            ret = self.tail.data
            self.tail = None
            return ret
        count = 0
        current = self.tail.next
        last = None
        while count < index:
            last = current
            current = current.next
            count += 1
        ret = current.data
        if index == 0:  # first element
            self.tail.next = current.next
        elif index == self.size:  # last element
            last.next = current.next
            self.tail = last
        else:  # somewhere in the middle
            last.next = current.next
        return ret

    def clear(self) -> None:
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
        circular_list = []
        if self.size == 0:
            return "[]"
        current = self.tail
        while self.tail != current.next:
            circular_list.append(current.next.data)
            current = current.next
        circular_list.append(self.tail.data)
        return str(circular_list)

    def __len__(self) -> int:
        """
        Returns length of list.

        No arguments.
        """
        return self.size
