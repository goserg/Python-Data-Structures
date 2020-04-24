import unittest
from src.circular_linked_list import CircularLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.cll = CircularLinkedList()

    def test_add_first(self) -> None:
        self.cll.add_first(1)
        self.assertEqual(self.cll.__repr__(), "[1]")
        self.cll.add_first(2)
        self.assertEqual(self.cll.__repr__(), "[2, 1]")
        self.cll.add_first(3)
        self.assertEqual(self.cll.__repr__(), "[3, 2, 1]")

    def test_append(self) -> None:
        self.cll.append(1)
        self.assertEqual(self.cll.__repr__(), "[1]")
        self.cll.append(2)
        self.assertEqual(self.cll.__repr__(), "[1, 2]")
        self.cll.append(3)
        self.assertEqual(self.cll.__repr__(), "[1, 2, 3]")

    def test_get(self) -> None:
        with self.assertRaises(IndexError) as context:
            self.cll.get(0)
            self.assertTrue("Index is out of range" in context.exception)
        self.cll.append(1)
        self.assertEqual(self.cll.get(0), 1)
        with self.assertRaises(IndexError) as context:
            self.cll.get(1)
            self.assertTrue("Index is out of range" in context.exception)
        self.cll.append(2)
        with self.assertRaises(IndexError) as context:
            self.cll.get(-1)
            self.assertTrue("Index is out of range" in context.exception)
        self.assertEqual(self.cll.get(0), 1)
        self.assertEqual(self.cll.get(1), 2)
        with self.assertRaises(IndexError) as context:
            self.cll.get(2)
            self.assertTrue("Index is out of range" in context.exception)
        self.cll.add_first(3)
        self.assertEqual(self.cll.get(0), 3)
        self.assertEqual(self.cll.get(1), 1)
        self.assertEqual(self.cll.get(2), 2)
        with self.assertRaises(IndexError) as context:
            self.cll.get(3)
            self.assertTrue("Index is out of range" in context.exception)

    def test_pop(self) -> None:
        with self.assertRaises(IndexError) as context:
            self.cll.pop(0)
            self.assertTrue("Index is out of range" in context.exception)
        self.cll.append(1)
        self.assertEqual(self.cll.pop(0), 1)
        with self.assertRaises(IndexError) as context:
            self.cll.pop(1)
            self.assertTrue("Index is out of range" in context.exception)
        self.cll.append(1)
        self.cll.append(2)
        self.assertEqual(self.cll.pop(0), 1)
        self.assertEqual(self.cll.pop(0), 2)
        self.cll.add_first(3)
        self.cll.add_first(2)
        self.cll.add_first(1)
        self.assertEqual(self.cll.pop(0), 1)
        self.assertEqual(self.cll.pop(1), 3)
        with self.assertRaises(IndexError) as context:
            self.cll.pop(2)
            self.assertTrue("Index is out of range" in context.exception)

    def test_clear(self) -> None:
        self.assertEqual(len(self.cll), 0)
        self.cll.append(1)
        self.assertEqual(len(self.cll), 1)
        self.cll.clear()
        self.assertEqual(len(self.cll), 0)
        self.cll.append(2)
        self.assertEqual(len(self.cll), 1)
        self.cll.clear()
        self.assertEqual(len(self.cll), 0)

    def test_big_test(self) -> None:
        test_case = 1_000_00
        for i in range(test_case):
            self.cll.add_first(i)
        for i in reversed(range(test_case)):
            self.assertEqual(self.cll.pop(0), i)

    def test_step(self) -> None:
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.step(2)
        self.assertEqual(self.cll.__repr__(), "[3, 1, 2]")


if __name__ == "__main__":
    unittest.main()
