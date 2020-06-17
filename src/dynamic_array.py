from collections.abc import MutableSequence
import ctypes
from typing import TypeVar


class DynamicArray(MutableSequence):
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 1
        self.array = self._create_array()

    def insert(self, index: int, value: TypeVar) -> None:
        if index < -self.size or index > self.size:
            raise IndexError(f"{index} is out of bounds")
        if index < 0:
            index += self.size
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = value
        self.size += 1

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index: int) -> TypeVar:
        if index < -self.size or index >= self.size:
            raise IndexError(f"{index} is out of bounds")
        if index < 0:
            index += self.size
        return self.array[index]

    def __setitem__(self, index: int, value: TypeVar) -> None:
        if index < -self.size or index > self.size:
            raise IndexError(f"{index} is out of bounds")
        if index < 0:
            index += self.size
        if self.size == self.capacity:
            self._resize()
        self.array[index] = value

    def __delitem__(self, index: int) -> None:
        if self.size == 0:
            raise IndexError("Array is empty.")
        if index < -self.size or index >= self.size:
            raise IndexError(f"{index} is out of bounds")
        if index < 0:
            index += self.size
        if index == self.size - 1:
            self.array[index] = None
            self.size -= 1
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def __str__(self) -> str:
        return str([i for i in self.array[0:self.size]])

    def __repr__(self) -> str:
        return str(self)

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _create_array(self, capacity=None) -> ctypes.Array:
        capacity = capacity or self.capacity
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    ar = DynamicArray()
    lst = []
    for n in range(100):
        ar.append(n)
        lst.append(n)
    assert ar.pop() == lst.pop()
    assert ar.pop(0) == lst.pop(0)
    assert ar.pop(-3) == lst.pop(-3)
    ar.insert(10, 30)
    lst.insert(10, 30)
    ar[10] = 42
    lst[10] = 42
    ar[-50] = "test"
    lst[-50] = "test"
    assert ar.index(30) == lst.index(30)
    ar.reverse()
    lst.reverse()
    assert len(ar) == len(lst)
    assert str(ar) == str(lst)
    assert repr(ar) == repr(lst)



