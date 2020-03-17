import unittest
from linked_list import LinkedList


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
        self.assertEqual(self.ll.get(0), None)
        self.ll.append(1)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), None)
        self.ll.append(2)
        self.assertEqual(self.ll.get(-1), None)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), None)
        self.ll.add_first(3)
        self.assertEqual(self.ll.get(0), 3)
        self.assertEqual(self.ll.get(1), 1)
        self.assertEqual(self.ll.get(2), 2)
        self.assertEqual(self.ll.get(3), None)

    def test_pop(self):
        self.assertEqual(self.ll.pop(0), None)
        self.ll.append(1)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertEqual(self.ll.pop(1), None)
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertEqual(self.ll.pop(0), 2)
        self.ll.add_first(3)
        self.ll.add_first(2)
        self.ll.add_first(1)
        self.assertEqual(self.ll.pop(0), 1)
        self.assertEqual(self.ll.pop(1), 3)
        self.assertEqual(self.ll.pop(2), None)

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


if __name__ == "__main__":
    unittest.main()
