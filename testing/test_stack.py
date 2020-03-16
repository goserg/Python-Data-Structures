import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_pop(self):
        self.stack.stack = [1]
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.stack, [])
        self.stack.stack = []
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.stack, [])
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.stack, [1, 2])

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.stack, [1])
        self.stack.push(2.0)
        self.assertEqual(self.stack.stack, [1, 2.0])
        self.stack.push("3")
        self.assertEqual(self.stack.stack, [1, 2.0, "3"])

    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)
        self.stack.stack = [1]
        self.assertEqual(self.stack.peek(), 1)
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.stack, [1, 2, 3])

    def test_search(self):
        self.assertEqual(self.stack.search(1), None)
        self.stack.stack = [1]
        self.assertEqual(self.stack.search(1), 1)
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.search(1), 3)
        self.assertEqual(self.stack.search(2), 2)
        self.assertEqual(self.stack.search(3), 1)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.stack = [1]
        self.assertEqual(self.stack.is_empty(), False)
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.is_empty(), False)

    def test_clear(self):
        self.stack.stack = [1, 2, 3]
        self.stack.clear()
        self.assertEqual(self.stack.stack, [])

    def test___repr__(self):
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.__repr__(), "[1, 2, 3]")

    def test___len__(self):
        self.stack.stack = [1, 2, 3]
        self.assertEqual(len(self.stack), 3)


if __name__ == "__main__":
    unittest.main()
