import unittest

from src.hash.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_from_keys(self) -> None:
        ht = HashTable.from_keys(['a', 'b'])
        self.assertIsNone(ht.pop("a"))
        self.assertIsNone(ht.pop("b"))
        ht = HashTable.from_keys(['a', 'b'], 100)
        self.assertEqual(ht.pop("a"), 100)
        self.assertEqual(ht.pop("b"), 100)

    def test_constructor(self) -> None:
        ht = HashTable(alpha=1, beta=0.9, gamma="ray")
        self.assertEqual(ht.pop("alpha"), 1)
        self.assertEqual(ht.pop("beta"), 0.9)
        self.assertEqual(ht.pop("gamma"), "ray")
        ht = HashTable([("delta", "force"), ("epsilon", 0), ("zeta", "Riemann")])
        self.assertEqual(ht.pop("delta"), "force")
        self.assertEqual(ht.pop("epsilon"), 0)
        self.assertEqual(ht.pop("zeta"), "Riemann")
        ht = HashTable([("delta", "force"), ("epsilon", 0), ("zeta", "Riemann")], alpha=1, beta=0.9, gamma="ray")
        self.assertEqual(ht.pop("alpha"), 1)
        self.assertEqual(ht.pop("beta"), 0.9)
        self.assertEqual(ht.pop("gamma"), "ray")
        self.assertEqual(ht.pop("delta"), "force")
        self.assertEqual(ht.pop("epsilon"), 0)
        self.assertEqual(ht.pop("zeta"), "Riemann")

    def test_insert_search_pop_len(self) -> None:
        ht = HashTable()
        test_case = 1_000
        for i in range(test_case):
            ht.insert(i, i*2)
        self.assertIsNone(ht.search("Uno"))
        for j in range(test_case):
            self.assertEqual(len(ht), test_case)
            self.assertEqual(ht.search(j), j * 2)
            self.assertEqual(ht.pop(j), j * 2)
            test_case -= 1
            self.assertEqual(len(ht), test_case)
            self.assertIsNone(ht.pop(j))

    def test_clear(self) -> None:
        ht = HashTable()
        self.assertEqual(len(ht), 0)
        ht[1] = 2
        ht[3] = 4
        self.assertEqual(len(ht), 2)
        ht.clear()
        self.assertEqual(len(ht), 0)

    def test_changing(self) -> None:
        ht = HashTable()
        ht[1] = 2
        self.assertEqual(ht[1], 2)
        self.assertEqual(len(ht), 1)
        ht[1] = 3
        self.assertEqual(ht[1], 3)
        self.assertEqual(len(ht), 1)

    def test_keys(self) -> None:
        ht = HashTable()
        ht["1"] = 2
        ht["2"] = 3
        self.assertEqual(ht.keys(), ["2", "1"])

    def test_values(self) -> None:
        ht = HashTable()
        ht["1"] = 2
        ht["2"] = 3
        self.assertEqual(ht.values(), [3, 2])


if __name__ == "__main__":
    unittest.main()
