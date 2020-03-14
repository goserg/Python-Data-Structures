class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        Add data to the stack.
        Time complexity = O(1).
        """
        self.stack.append(data)

    def pop(self):
        """
        Return data prom the top and remove it from the stack.
        Return None if stack is empty.
        Time complexity = O(1).
        """
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def peek(self):
        """
        Return data from top the stack.
        Return None if stack is empty.
        Time complexity = O(1).
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        return None

    def search(self, data):
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

    def is_empty(self):
        """
        Return False if the stack is empty else return True.
        """
        return True if len(self.stack) == 0 else False

    def clear(self):
        """
        Remove all data from the stack.
        """
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)
