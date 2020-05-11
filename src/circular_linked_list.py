from __future__ import annotations
import reprlib
from collections.abc import MutableSequence
from typing import Any, Optional


class _Node:
    __slots__ = ("next", "data")

    def __init__(self, data: Any = None) -> None:
        self.next: Optional[_Node] = None
        self.data = data


class CircularLinkedList(MutableSequence):
    __slots__ = ("tail", "size")

    def __init__(self) -> None:
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
        if self.size == 0:
            new_node.next = new_node
            self.tail = new_node
        else:  # list is not empty
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.size += 1

    def rotate(self, n: int = 1) -> None:
        """
        Rotates the list by moving tail pointer forward for n steps.

        Arguments:
            n -- number of steps (default 1).
        """
        if self.size > 0:
            for _ in range(n):
                self.tail = self.tail.next

    def get(self, index: int) -> None:
        return self.__getitem__(index)

    def clear(self) -> None:
        """Clear the list."""
        self.__init__()

    def __repr__(self) -> str:
        circular_list = []
        if self.size == 0:
            return f"{self.__class__.__name__} []"
        current = self.tail
        while self.tail != current.next:
            circular_list.append(current.next.data)
            current = current.next
        circular_list.append(self.tail.data)
        return f"{self.__class__.__name__} {reprlib.repr(circular_list)}"

    def __str__(self) -> str:
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
        return self.size

    def insert(self, index: int, data: Any) -> None:
        if index == 0:
            self.add_first(data)
            return
        if index == self.size or index == -1:
            new_node = _Node(data)
            if self.size == 0:
                new_node.next = new_node
            else:  # list is not empty
                new_node.next = self.tail.next
                self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return
        if index < 0 or index > self.size - 1:
            raise IndexError("Index is out of range")
        new_node = _Node(data)
        count = 1
        current = self.tail.next
        while count < index:
            current = current.next
            count += 1
        temp = current.next
        current.next = new_node
        new_node.next = temp
        self.size += 1

    def __getitem__(self, index: int) -> Any:
        if index == -1:
            index = self.size - 1
        if index < 0 or index > self.size - 1:
            raise IndexError("Index is out of range")
        count = 0
        current = self.tail.next
        while count < index:
            current = current.next
            count += 1
        return current.data

    def __setitem__(self, index: int, data: Any) -> None:
        if index == -1:
            index = self.size - 1
        if index < 0 or index > self.size - 1:
            raise IndexError("Index is out of range")
        count = 0
        current = self.tail.next
        while count < index:
            current = current.next
            count += 1
        current.data = data

    def __delitem__(self, index: int) -> None:
        if index == -1:
            index = self.size - 1
        if index < 0 or index > self.size - 1:
            raise IndexError("Index is out of range")
        count = 0
        current = self.tail.next
        last = None
        while count < index:
            last = current
            current = current.next
            count += 1
        if index == 0:  # first element
            self.tail.next = current.next
        elif index == self.size or index == -1:  # last element
            last.next = current.next
            self.tail = last
        else:  # somewhere in the middle
            last.next = current.next
        self.size -= 1
