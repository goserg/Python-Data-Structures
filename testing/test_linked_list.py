import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_sdd_first(self):
        self.ll.add_first(1)
        self.assertEqual(self.ll.__str__(), "[1]")
        self.ll.add_first(2)
        self.assertEqual(self.ll.__str__(), "[2, 1]")
        self.ll.add_first(3)
        self.assertEqual(self.ll.__str__(), "[3, 2, 1]")

    def test_append(self):
        self.ll.append(1)
        self.assertEqual(self.ll.__str__(), "[1]")
        self.ll.append(2)
        self.assertEqual(self.ll.__str__(), "[1, 2]")
        self.ll.append(3)
        self.assertEqual(self.ll.__str__(), "[1, 2, 3]")

    def test_get(self):
        self.assertIsNone(self.ll.get(0))
        self.ll.append(1)
        self.assertEqual(self.ll.get(0), 1)
        self.assertIsNone(self.ll.get(1))
        self.ll.append(2)
        self.assertIsNone(self.ll.get(-1))
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertIsNone(self.ll.get(2))
        self.ll.add_first(3)
        self.assertEqual(self.ll.get(0), 3)
        self.assertEqual(self.ll.get(1), 1)
        self.assertEqual(self.ll.get(2), 2)
        self.assertIsNone(self.ll.get(3))

    def test_pop(self):
        self.assertIsNone(self.ll.pop(0))
        self.ll.append(1)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertIsNone(self.ll.pop(1))
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertEqual(self.ll.pop(0), 2)
        self.ll.add_first(3)
        self.ll.add_first(2)
        self.ll.add_first(1)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertEqual(self.ll.pop(1), 3)
        self.assertIsNone(self.ll.pop(2))

    def test_clear(self):
        self.assertEqual(len(self.ll), 0)
        self.ll.append(1)
        self.assertEqual(len(self.ll), 1)
        self.ll.clear()
        self.assertEqual(len(self.ll), 0)
        self.ll.append(2)
        self.assertEqual(len(self.ll), 1)
        self.ll.clear()
        self.assertEqual(len(self.ll), 0)

    def test_append_list(self):
        self.ll.append_list([])
        self.assertEqual(self.ll.__str__(), "[]")
        self.ll.append_list(123)
        self.assertEqual(self.ll.__str__(), "[]")
        self.ll.append_list([1, 2, 3])
        self.assertEqual(self.ll.__str__(), "[1, 2, 3]")
        self.ll.append_list([3, 2, 1])
        self.assertEqual(self.ll.__str__(), "[1, 2, 3, 3, 2, 1]")

    def test_big_test(self):
        test_case = 1_000_00
        for i in range(test_case):
            self.ll.add_first(i)
        for i in reversed(range(test_case)):
            self.assertEqual(self.ll.pop(0), i)


if __name__ == "__main__":
    unittest.main()
