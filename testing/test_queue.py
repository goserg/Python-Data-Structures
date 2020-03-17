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
        self.assertIsNone(self.queue.pop())
        self.queue.push(1)
        self.assertEqual(self.queue.pop(), 1)
        self.assertIsNone(self.queue.pop())
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertIsNone(self.queue.pop())

    def test_peek(self):
        self.assertIsNone(self.queue.peek())
        self.queue.push(1)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 1)

    def test_search(self):
        self.assertIsNone(self.queue.search(1))
        self.queue.push(1)
        self.assertEqual(self.queue.search(1), 1)
        self.queue.push(2)
        self.assertEqual(self.queue.search(1), 1)
        self.assertEqual(self.queue.search(2), 2)
        self.assertIsNone(self.queue.search(-1))

    def test_is_empty_clear_len(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.clear()
        self.assertEqual(len(self.queue), 0)
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertEqual(len(self.queue), 1)
        self.assertFalse(self.queue.is_empty())
        self.queue.pop()
        self.assertEqual(len(self.queue), 0)
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.push(2)
        self.assertEqual(len(self.queue), 2)
        self.assertFalse(self.queue.is_empty())
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_big_test(self):
        test_case = 1_000_000
        for i in range(test_case):
            self.queue.push(i)
        for i in range(test_case):
            self.assertEqual(self.queue.pop(), i)
        self.assertIsNone(self.queue.pop())


if __name__ == "__main__":
    unittest.main()
