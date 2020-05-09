from __future__ import annotations
import reprlib
from typing import Any, Optional


class _Node:
    __slots__ = ("data", "next", "prev")

    def __init__(self, data: Any = None):
        self.data = data
        self.next: Optional[_Node] = None
        self.prev: Optional[_Node] = None


class DoublyLinkedList:
    __slots__ = ("head", "tail", "size")

    def __init__(self):
        self.head: Optional[_Node] = None
        self.tail: Optional[_Node] = None
        self.size = 0

    def add_first(self, data: Any) -> None:
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

    def append(self, data: Any) -> None:
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

    def get(self, index: int) -> Any:
        """
        Returns data with specified index.
        Time complexity = O(n).

        Raises: IndexError exception

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range")
        current = self._find(index)
        return current.data

    def _find(self, index: int) -> _Node:
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node

    def pop(self, index: int) -> Any:
        """
        Returns data with specified index
        and erases this data from the list.
        Time complexity = O(n).

        Raises: IndexError exception

        Arguments:
            index -- integer (0 <= index < len()).
        """
        if self.size == 0:
            return
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range")
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

    def clear(self) -> None:
        """
        Clear the list.
        """
        self.__init__()

    def __repr__(self) -> str:
        double_list = []
        current_node = self.head
        while current_node:
            double_list.append(current_node.data)
            current_node = current_node.next
        return f"{self.__class__.__name__} {reprlib.repr(double_list)}"

    def __str__(self) -> str:
        double_list = []
        current_node = self.head
        while current_node:
            double_list.append(current_node.data)
            current_node = current_node.next
        return str(double_list)

    def __len__(self) -> int:
        return self.size
