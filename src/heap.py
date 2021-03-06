import reprlib
from typing import Optional, Union, List


class Heap:
    __slots__ = "heap"
    heap: List[Union[int, float]]

    def append(self, data: Union[int, float]) -> None:
        """
        Add data to heap.
        Time complexity = O(log n).

        Arguments:
            data -- number
        """
        self.heap.append(data)
        self._heap_up()

    def peek(self) -> Optional[Union[int, float]]:
        """
        Return data from top of heap.
        Return None if heap is empty.
        Time complexity = O(1).
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def pop(self) -> Optional[Union[int, float]]:
        """
        Return data prom the top and remove it from heap.
        Return None if heap is empty.
        Time complexity = O(log n).
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        ret = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heap_down()
        return ret

    def _heap_down(self) -> None:
        i = 0
        while (2 * i + 1) < len(self.heap):
            has_right = (2 * i + 2) < len(self.heap)
            smaller = 2 * i + 1
            if has_right and self.heap[2 * i + 2] < self.heap[2 * i + 1]:
                smaller = 2 * i + 2
            if self.heap[i] < self.heap[smaller]:
                return
            else:
                self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]
            i = smaller

    def _heap_up(self) -> None:
        i = len(self.heap) - 1
        parent_i = (i - 1) // 2
        while parent_i >= 0 and self.heap[parent_i] > self.heap[i]:
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            i, parent_i = parent_i, (parent_i - 1) // 2

    def is_empty(self) -> bool:
        """
        Return False if heap is empty else return True.
        """
        return True if len(self.heap) == 0 else False

    def clear(self) -> None:
        """
        Remove all data from heap.
        """
        self.heap = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {reprlib.repr(self.heap)}"

    def __str__(self) -> str:
        return str(self.heap)

    def __len__(self) -> int:
        return len(self.heap)
