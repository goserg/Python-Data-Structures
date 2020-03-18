import hashlib

MAX_LOAD_FACTOR = 0.5
INITIAL_SIZE = 1


class _Data:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:
    @staticmethod
    def from_keys(*args):
        ht = HashTable()
        for i in args[0]:
            ht[i] = args[1]
        return ht

    def __init__(self, *args, **kwargs) -> None:
        self.table = [[] for _ in range(INITIAL_SIZE)]
        self.size = 0

        for i in args:
            for j in i:
                self.insert(j[0], j[1])

        for key, value in kwargs.items():
            self.insert(key, value)

    def insert(self, key, value=None) -> None:
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

    def search(self, key):
        index = self._get_index_and_hash(key)
        for data in self.table[index]:
            if data.key == key:
                return data.value

    def __getitem__(self, key):
        return self.search(key)

    def pop(self, key) -> None:
        index = self._get_index_and_hash(key)
        for i, data in enumerate(self.table[index]):
            if data.key == key:
                value = self.table[index].pop(i).value
                self.size -= 1
                return value

    def clear(self) -> None:
        self.__init__()

    def _get_index_and_hash(self, key) -> int:
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
                a = ''.join(["'", a, "'"]) if isinstance(a, str) else str(a)
                b = j.value
                b = ''.join(["'", b, "'"]) if isinstance(b, str) else str(b)
                data.append(': '.join([a, b]))
        return '{' + ', '.join(data) + '}'
