import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test___str__(self):
        self.assertEqual(self.queue.__str__(), "[]")
        self.queue.push(1)
        self.assertEqual(self.queue.__str__(), "[1]")
        self.queue.push(2)
        self.assertEqual(self.queue.__str__(), "[2, 1]")
        self.queue.push(3)
        self.assertEqual(self.queue.__str__(), "[3, 2, 1]")

    def test_push(self):
        self.queue.push(1)
        self.assertEqual(self.queue.__str__(), "[1]")
        self.queue.push(2)
        self.assertEqual(self.queue.__str__(), "[2, 1]")

    def test_pop(self):
        self.assertEqual(self.queue.pop(), None)
        self.queue.push(1)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), None)
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), None)

    def test_peek(self):
        self.assertEqual(self.queue.peek(), None)
        self.queue.push(1)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 1)

    def test_search(self):
        self.assertEqual(self.queue.search(1), None)
        self.queue.push(1)
        self.assertEqual(self.queue.search(1), 1)
        self.queue.push(2)
        self.assertEqual(self.queue.search(1), 1)
        self.assertEqual(self.queue.search(2), 2)
        self.assertEqual(self.queue.search(-1), None)

    def test_is_empty_clear_len(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.clear()
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.push(1)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.is_empty(), False)
        self.queue.pop()
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.push(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.push(2)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.is_empty(), False)
        self.queue.clear()
        self.assertEqual(self.queue.is_empty(), True)
        self.assertEqual(len(self.queue), 0)


if __name__ == "__main__":
    unittest.main()
