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

    def append(self, data):
        """
        Places new 'data' at the end of the linked list.

        Arguments:
        data -- any data.
        """
        current = self.head
        while current.next:
            current = current.next
        current.next = _Node(data)

    def get(self, index):
        """
        Returns data with specified index.
        """
        if index >= self.__len__():
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

        :argument index - integer >= 0
        """
        if index < 0 or index >= self.__len__():
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
        return ret

    def clear(self):
        """
        Clear linked list.

        No arguments.
        """
        self.head.next = None

    def append_list(self, data):
        """
        Places new data from list at the end of the linked list.

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
        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count
