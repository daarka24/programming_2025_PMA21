class ArrayList:
    def __init__(self, initial_data=None):
        if initial_data is None:
            self.array = [None] * 10
            self.size = 0
        else:
            self.array = list(initial_data)
            self.size = len(initial_data)

    def _resize(self):
        new_capacity = int(1.5 * len(self.array)) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, value):
        if self.size >= len(self.array):
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size >= len(self.array):
            self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def clear(self):
        for i in range(self.size):
            self.array[i] = None
        self.size = 0

    def to_list(self):
        return [self.array[i] for i in range(self.size)]

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for i in range(self.size):
                file.write(str(self.array[i]) + "\n")

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        self.array = [line.strip() for line in lines]
        self.size = len(self.array)
        if len(self.array) == 0:
            self.array = [None] * 10
