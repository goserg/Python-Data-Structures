import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_pop(self) -> None:
        self.stack.stack = [1]
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.stack, [])
        self.stack.stack = []
        self.assertIsNone(self.stack.pop())
        self.assertEqual(self.stack.stack, [])
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.stack, [1, 2])

    def test_push(self) -> None:
        self.stack.push(1)
        self.assertEqual(self.stack.stack, [1])
        self.stack.push(2.0)
        self.assertEqual(self.stack.stack, [1, 2.0])
        self.stack.push("3")
        self.assertEqual(self.stack.stack, [1, 2.0, "3"])

    def test_peek(self) -> None:
        self.assertIsNone(self.stack.peek())
        self.stack.stack = [1]
        self.assertEqual(self.stack.peek(), 1)
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.stack, [1, 2, 3])

    def test_search(self) -> None:
        self.assertIsNone(self.stack.search(1))
        self.stack.stack = [1]
        self.assertEqual(self.stack.search(1), 1)
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.search(1), 3)
        self.assertEqual(self.stack.search(2), 2)
        self.assertEqual(self.stack.search(3), 1)

    def test_is_empty(self) -> None:
        self.assertTrue(self.stack.is_empty())
        self.stack.stack = [1]
        self.assertFalse(self.stack.is_empty())
        self.stack.stack = [1, 2, 3]
        self.assertFalse(self.stack.is_empty())

    def test_clear(self) -> None:
        self.stack.stack = [1, 2, 3]
        self.stack.clear()
        self.assertEqual(self.stack.stack, [])

    def test___str__(self) -> None:
        self.stack.stack = [1, 2, 3]
        self.assertEqual(self.stack.__str__(), "[1, 2, 3]")

    def test___len__(self) -> None:
        self.stack.stack = [1, 2, 3]
        self.assertEqual(len(self.stack), 3)

    def test_big_test(self) -> None:
        test_case = 100_000
        for i in range(test_case):
            self.stack.push(i)
        for i in reversed(range(test_case)):
            self.assertEqual(self.stack.pop(), i)
        self.assertIsNone(self.stack.pop())

    def test_repr(self) -> None:
        for i in range(6):
            self.stack.push(i)
        self.assertEqual(self.stack.__repr__(), "Stack [0, 1, 2, 3, 4, 5]")
        self.stack.push(6)
        self.assertEqual(self.stack.__repr__(), "Stack [0, 1, 2, 3, 4, 5, ...]")


if __name__ == "__main__":
    unittest.main()
