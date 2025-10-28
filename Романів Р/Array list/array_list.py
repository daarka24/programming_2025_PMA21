class ArrayList:
    def __init__(self, array=None):
        if not isinstance(array, list):
            array = None

        if array is None:
            self.size = 0
            self.capacity = 10
            self.data = [None] * 10
        else:
            self.size = len(array)
            self.capacity = int(1.5 * self.size + 1)
            self.data = array + ([None] * (self.capacity - self.size))

    def __str__(self):
        return str([el for el in self.data if el])

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        idx = self.size + index if index < 0 else index
        if idx >= self.size or idx < 0:
            raise IndexError("Index out of range")

        return self.data[idx]

    def __setitem__(self, index, value):
        idx = self.size + index if index < 0 else index
        if idx >= self.size or idx < 0:
            raise IndexError("Index out of range")

        self.data[idx] = value

    def _resize(self):
        self.capacity = int(1.5 * self.capacity + 1)
        self.data += [None] * (self.capacity - self.size)

    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def pop(self, index=-1):
        idx = self.size + index if index < 0 else index

        if idx >= self.size or idx < 0:
            raise IndexError("Index out of range")

        value = self.data[idx]

        for i in range(idx, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

        return value

    def remove(self, value):
        if value is None:
            raise ValueError("Can't remove nothing")

        for index, el in enumerate(self.data):
            if el == value:
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i + 1]
                self.data[self.size - 1] = None
                self.size -= 1
                return
        raise ValueError("Can't find an element")

    def insert(self, index, value):
        idx = self.size + 1 + index if index < 0 else index

        if idx > self.size:
            idx = self.size

        if self.size >= self.capacity:
            self._resize()

        for i in range(self.size, idx, -1):
            self.data[i] = self.data[i - 1]
        self.data[idx] = value
        self.size += 1

    def clear(self):
        self.data = [None] * self.capacity
        self.size = 0