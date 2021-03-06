import unittest

from src.doubly_linked_list import DoublyLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = DoublyLinkedList()

    def test_add_first(self) -> None:
        self.ll.add_first(1)
        self.assertEqual(self.ll.__str__(), "[1]")
        self.ll.add_first(2)
        self.assertEqual(self.ll.__str__(), "[2, 1]")
        self.ll.add_first(3)
        self.assertEqual(self.ll.__str__(), "[3, 2, 1]")

    def test_append(self) -> None:
        self.ll.append(1)
        self.assertEqual(self.ll.__str__(), "[1]")
        self.ll.append(2)
        self.assertEqual(self.ll.__str__(), "[1, 2]")
        self.ll.append(3)
        self.assertEqual(self.ll.__str__(), "[1, 2, 3]")

    def test_get(self) -> None:
        with self.assertRaises(IndexError) as context:
            self.ll.get(0)
            self.assertTrue("Index is out of range" in context.exception)
        self.ll.append(1)
        self.assertEqual(self.ll.get(0), 1)
        with self.assertRaises(IndexError) as context:
            self.ll.get(1)
            self.assertTrue("Index is out of range" in context.exception)
        self.ll.append(2)
        with self.assertRaises(IndexError) as context:
            self.ll.get(-1)
            self.assertTrue("Index is out of range" in context.exception)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        with self.assertRaises(IndexError) as context:
            self.ll.get(2)
            self.assertTrue("Index is out of range" in context.exception)
        self.ll.add_first(3)
        self.assertEqual(self.ll.get(0), 3)
        self.assertEqual(self.ll.get(1), 1)
        self.assertEqual(self.ll.get(2), 2)
        with self.assertRaises(IndexError) as context:
            self.ll.get(3)
            self.assertTrue("Index is out of range" in context.exception)

    def test_pop(self) -> None:
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
        with self.assertRaises(IndexError) as context:
            self.ll.pop(2)
            self.assertTrue("Index is out of range" in context.exception)

    def test_clear(self) -> None:
        self.assertEqual(len(self.ll), 0)
        self.ll.append(1)
        self.assertEqual(len(self.ll), 1)
        self.ll.clear()
        self.assertEqual(len(self.ll), 0)
        self.ll.append(2)
        self.assertEqual(len(self.ll), 1)
        self.ll.clear()
        self.assertEqual(len(self.ll), 0)

    def test_big_test(self) -> None:
        test_case = 1_000_00
        for i in range(test_case):
            self.ll.add_first(i)
        for i in reversed(range(test_case)):
            self.assertEqual(self.ll.pop(0), i)

    def test_repr(self) -> None:
        for i in range(6):
            self.ll.append(i)
        self.assertEqual(self.ll.__repr__(), "DoublyLinkedList [0, 1, 2, 3, 4, 5]")
        self.ll.append(6)
        self.assertEqual(self.ll.__repr__(), "DoublyLinkedList [0, 1, 2, 3, 4, 5, ...]")


if __name__ == "__main__":
    unittest.main()
