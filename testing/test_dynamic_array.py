import unittest

from src.dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def setUp(self) -> None:
        self.array = DynamicArray()

    def test_append(self) -> None:
        self.array.append(1)
        self.array.append(2)
        self.assertEqual(str(self.array), "[1, 2]")

    def test_extend(self) -> None:
        self.array.extend([1, 2, 3, 4])
        self.assertEqual(str(self.array), "[1, 2, 3, 4]")

    def test_big(self) -> None:
        for i in range(1000):
            self.array.append(i)
        for i in reversed(range(1000)):
            self.assertEqual(self.array.pop(), i)


if __name__ == "__main__":
    unittest.main()
