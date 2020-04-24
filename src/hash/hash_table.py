from __future__ import annotations
from typing import Any, List, Final


import hashlib

MAX_LOAD_FACTOR: Final = 0.5
INITIAL_SIZE: Final = 1


class _Data:
    __slots__ = ("key", "value")

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:
    __slots__ = ("table", "size")

    @staticmethod
    def from_keys(*args) -> HashTable:
        """
        Returns Hash Table filled with data from args

        Time complexity = O(n).

        Arguments:
            list of keys, value (value default: None)

        Example:
            hash_table = HashTable.from_keys(["Bob", "Mary"], 20)
            returns hash table {'Bob': 20, 'Mary': 20}
        """
        ht = HashTable()
        value = None
        if len(args) > 1:
            value = args[1]
        for i in args[0]:
            ht[i] = value
        return ht

    def __init__(self, *args, **kwargs) -> None:
        """
        Default constructor

        Time complexity = O(n).

        Arguments:
            list of tuples (key, value), keyword arguments (key=value)

        Example:
            hash_table = HashTable([("Bob", 20), ("Mary", 10)])
            or
            hash_table = HashTable(Bob=20, Mary=10)
            returns hash table {'Bob': 20, 'Mary': 10}
        """
        self.table = [[] for _ in range(INITIAL_SIZE)]
        self.size = 0

        for i in args:
            for j in i:
                self.insert(j[0], j[1])

        for key, value in kwargs.items():
            self.insert(key, value)

    def insert(self, key: Any, value: Any = None) -> None:
        """
        Insert key with a value. If key is in the hash table updates the value of that key.

        Time complexity = O(1).
        """
        index = self._get_index_and_hash(key)
        for i, data in enumerate(self.table[index]):
            if data.key == key:
                self.table[index][i].value = value
                break
        else:
            self.table[index].append(_Data(key, value))
            self.size += 1
        self._resize()

    def __setitem__(self, key, value) -> None:
        self.insert(key, value)

    def search(self, key: Any) -> Any:
        """
        Return the value for key if key is in the hash table, else None.

        Time complexity = O(1).
        """
        index = self._get_index_and_hash(key)
        for data in self.table[index]:
            if data.key == key:
                return data.value

    def __getitem__(self, key: Any) -> Any:
        return self.search(key)

    def pop(self, key: Any) -> Any:
        """
        Return the value for key if key is in the hash table, else None.
        Removes key from the hash table.

        Time complexity = O(1).
        """
        index = self._get_index_and_hash(key)
        for i, data in enumerate(self.table[index]):
            if data.key == key:
                value = self.table[index].pop(i).value
                self.size -= 1
                return value

    def keys(self) -> List[Any]:
        """
        Return a copy of the hash table’s list of keys.
        Time complexity = O(n).
        """
        keys = []
        for i in self.table:
            for j in i:
                keys.append(j.key)
        return keys

    def values(self) -> List[Any]:
        """
        Return a copy of the hash table’s list of values.

        Time complexity = O(n).
        """
        values = []
        for i in self.table:
            for j in i:
                values.append(j.value)
        return values

    def clear(self) -> None:
        """
        Clears hash table's data.

        Time complexity = O(1).
        """
        self.__init__()

    def _get_index_and_hash(self, key: Any) -> int:
        encode = hashlib.md5()
        encode.update(str(key).encode())
        hashed = encode.hexdigest()
        s = 0
        for i, letter in enumerate(str(hashed)):
            s += ord(letter) ** i
        index = s % len(self.table)
        return index

    def _resize(self) -> None:
        if self._load_factor() > MAX_LOAD_FACTOR:
            temp = list(self.table)
            self.table = [[] for _ in range(len(self.table) * 2)]
            for lst in temp:
                if lst:
                    for data in lst:
                        index = self._get_index_and_hash(data.key)
                        self.table[index].append(data)

    def _load_factor(self) -> float:
        return self.size / len(self.table)

    def __repr__(self) -> str:
        data = []
        for i in self.table:
            for j in i:
                a = j.key
                a = "".join(["'", a, "'"]) if isinstance(a, str) else str(a)
                b = j.value
                b = "".join(["'", b, "'"]) if isinstance(b, str) else str(b)
                data.append(": ".join([a, b]))
        return "{" + ", ".join(data) + "}"

    def __len__(self) -> int:
        return self.size
