from __future__ import annotations
from typing import Any, Optional


class _Node:
    __slots__ = ("data", "next")

    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next: Optional[_Node] = None


class LinkedList:
    __slots__ = ("head", "size")

    def __init__(self) -> None:
        """
        Constructor for a linked list.
        """
        self.head = _Node()
        self.size = 0

    def add_first(self, data: Any) -> None:
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

    def append(self, data: Any) -> None:
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

    def get(self, index: int) -> None:
        """
        Returns data with specified index.
        Time complexity = O(n).

        Raises: IndexError exception

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index >= self.size:
            raise IndexError("Index is out of range")
        current_index = 0
        current = self.head
        while current_index <= index:
            current_index += 1
            current = current.next
        return current.data

    def pop(self, index: int) -> None:
        """
        Returns data with specified index
        and erases this data from linked list.
        Time complexity = O(n).

        Raises: IndexError exception

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        current_index = 0
        current = self.head
        last = current
        while current_index <= index:
            current_index += 1
            last = current
            current = current.next
        ret = last.next.data
        last.next = current.next
        self.size -= 1
        return ret

    def clear(self) -> None:
        """
        Clear linked list.
        """
        self.head.next = None
        self.size = 0

    def __repr__(self) -> str:
        linked_list = []
        current = self.head
        while current.next:
            current = current.next
            linked_list.append(current.data)
        return str(linked_list)

    def __len__(self) -> int:
        return self.size
