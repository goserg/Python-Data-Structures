from __future__ import annotations
from collections.abc import MutableSequence
import reprlib
from typing import Any, Optional, Tuple


class _Node:
    __slots__ = ("data", "next")

    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next: Optional[_Node] = None


class LinkedList(MutableSequence):
    __slots__ = ("head", "size")

    def __init__(self) -> None:
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

    def get(self, index: int) -> None:
        """
        Returns data with specified index.
        Time complexity = O(n).

        Raises: IndexError exception

        Arguments:
            index -- integer (0 <= index < len()).
        """
        return self._find(index)[0].data

    def _add_last(self, data: Any) -> None:
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

    def _find(self, index: int) -> Tuple[_Node, _Node]:
        """
        :returns: list[index], list[index-1] nodes
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
        return current, last

    def clear(self) -> None:
        """
        Clear linked list.
        """
        self.head.next = None
        self.size = 0

    def __getitem__(self, item: int) -> Any:
        return self._find(item)[0].data

    def __setitem__(self, index: int, data: Any) -> None:
        if index == self.size:
            self._add_last(data)
            return
        self._find(index)[0].data = data

    def __repr__(self) -> str:
        linked_list = []
        current = self.head
        while current.next:
            current = current.next
            linked_list.append(current.data)
        return f"{self.__class__.__name__} {reprlib.repr(linked_list)}"

    def __str__(self) -> str:
        linked_list = []
        current = self.head
        while current.next:
            current = current.next
            linked_list.append(current.data)
        return str(linked_list)

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, index: int) -> None:
        current, last = self._find(index)
        last.next = current.next
        self.size -= 1

    def insert(self, index: int, data: Any) -> None:
        if index == self.size:
            self._add_last(data)
            return
        new_node = _Node(data)
        current, last = self._find(index)
        new_node.next = current
        last.next = new_node
        self.size += 1
