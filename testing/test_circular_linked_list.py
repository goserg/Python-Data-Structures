import unittest
from src.circular_linked_list import CircularLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.cll = CircularLinkedList()

    def test_add_first(self):
        self.cll.add_first(1)
        self.assertEqual(self.cll.__repr__(), "[1]")
        self.cll.add_first(2)
        self.assertEqual(self.cll.__repr__(), "[2, 1]")
        self.cll.add_first(3)
        self.assertEqual(self.cll.__repr__(), "[3, 2, 1]")

    def test_append(self):
        self.cll.append(1)
        self.assertEqual(self.cll.__repr__(), "[1]")
        self.cll.append(2)
        self.assertEqual(self.cll.__repr__(), "[1, 2]")
        self.cll.append(3)
        self.assertEqual(self.cll.__repr__(), "[1, 2, 3]")

    def test_get(self):
        self.assertIsNone(self.cll.get(0))
        self.cll.append(1)
        self.assertEqual(self.cll.get(0), 1)
        self.assertIsNone(self.cll.get(1))
        self.cll.append(2)
        self.assertIsNone(self.cll.get(-1))
        self.assertEqual(self.cll.get(0), 1)
        self.assertEqual(self.cll.get(1), 2)
        self.assertIsNone(self.cll.get(2))
        self.cll.add_first(3)
        self.assertEqual(self.cll.get(0), 3)
        self.assertEqual(self.cll.get(1), 1)
        self.assertEqual(self.cll.get(2), 2)
        self.assertIsNone(self.cll.get(3))

    def test_pop(self):
        self.assertIsNone(self.cll.pop(0))
        self.cll.append(1)
        self.assertEqual(self.cll.pop(0), 1)
        self.assertIsNone(self.cll.pop(1))
        self.cll.append(1)
        self.cll.append(2)
        self.assertEqual(self.cll.pop(0), 1)
        self.assertEqual(self.cll.pop(0), 2)
        self.cll.add_first(3)
        self.cll.add_first(2)
        self.cll.add_first(1)
        self.assertEqual(self.cll.pop(0), 1)
        self.assertEqual(self.cll.pop(1), 3)
        self.assertIsNone(self.cll.pop(2))

    def test_clear(self):
        self.assertEqual(len(self.cll), 0)
        self.cll.append(1)
        self.assertEqual(len(self.cll), 1)
        self.cll.clear()
        self.assertEqual(len(self.cll), 0)
        self.cll.append(2)
        self.assertEqual(len(self.cll), 1)
        self.cll.clear()
        self.assertEqual(len(self.cll), 0)

    def test_big_test(self):
        test_case = 1_000_00
        for i in range(test_case):
            self.cll.add_first(i)
        for i in reversed(range(test_case)):
            self.assertEqual(self.cll.pop(0), i)

    def test_step(self):
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.step(2)
        self.assertEqual(self.cll.__repr__(), "[3, 1, 2]")


if __name__ == "__main__":
    unittest.main()
