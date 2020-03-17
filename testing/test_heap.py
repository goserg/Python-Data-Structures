import unittest
from heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = Heap()
        self.heap.heap = [1, 3, 2]

    def test_peek(self):
        self.assertEqual(self.heap.peek(), 1)

    def test_append(self):
        self.heap.append(2)
        self.assertEqual(self.heap.heap, [1, 2, 2, 3])
        self.heap.append(1)
        self.assertEqual(self.heap.heap, [1, 1, 2, 3, 2])
        self.heap.append(3)
        self.assertEqual(self.heap.heap, [1, 1, 2, 3, 2, 3])

    def test_pop(self):
        self.assertEqual(self.heap.pop(), 1)
        self.assertEqual(self.heap.heap, [2, 3])
        self.assertEqual(self.heap.pop(), 2)
        self.assertEqual(self.heap.heap, [3])
        self.assertEqual(self.heap.pop(), 3)
        self.assertEqual(self.heap.heap, [])

    def test_is_empty(self):
        self.assertFalse(self.heap.is_empty())
        self.heap.heap = []
        self.assertTrue(self.heap.is_empty())

    def test_clear(self):
        self.assertNotEqual(self.heap.heap, [])
        self.heap.clear()
        self.assertEqual(self.heap.heap, [])

    def test_big_test(self):
        self.heap.clear()
        test_case = 100_000
        for i in reversed(range(test_case)):
            self.heap.append(i)
        for i in range(test_case):
            self.assertEqual(self.heap.pop(), i)


if __name__ == "__main__":
    unittest.main()
