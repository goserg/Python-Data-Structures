import reprlib
from typing import Any, List, Optional


class Stack:
    __slots__ = "stack"

    def __init__(self) -> None:
        self.stack: List[Any] = []

    def push(self, data: Any) -> None:
        """
        Add data to the stack.
        Time complexity = O(1).
        """
        self.stack.append(data)

    def pop(self) -> Any:
        """
        Return data prom the top and remove it from the stack.
        Return None if stack is empty.
        Time complexity = O(1).
        """
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def peek(self) -> Any:
        """
        Return data from top of the stack.
        Return None if stack is empty.
        Time complexity = O(1).
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None

    def search(self, data: Any) -> Optional[int]:
        """
        Search for a data in the stack and get its distance from the top.
        This method starts the count of the position from 1.
        Return None if data not in the stack.
        Time complexity = O(n).
        """
        for i, d in enumerate(reversed(self.stack)):
            if d == data:
                return i + 1
        return None

    def is_empty(self) -> bool:
        """
        Return False if the stack is empty else return True.
        """
        return True if len(self.stack) == 0 else False

    def clear(self) -> None:
        """
        Remove all data from the stack.
        """
        self.stack = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {reprlib.repr(self.stack)}"

    def __str__(self) -> str:
        return str(self.stack)

    def __len__(self) -> int:
        return len(self.stack)
