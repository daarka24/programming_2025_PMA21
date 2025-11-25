class ArrayList:
    def __init__(self, size =10):
        self.size = size
        self.count = 0
        self.array = [None] * size
    def __str__(self):
        return f"Elements{self.array}, Size{self.size}, Count{self.count}"
    def _resize(self):
        self.size = int(1.5 * self.size + 1)
        self.array += [None] * (self.size - self.count)
        print(f"Array Resized {self.size} elements")

    def add(self, value):
        if self.count >= self.size:
            self._resize()
        self.array[self.count] = value
        self.count += 1
    def remove(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        removed = self.array[index]
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.count -= 1
        self.array[self.count] = None
        return removed
    def insert(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        if self.count >= self.size:
            self._resize()
        for i in range(self.count, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.count += 1
    def clear(self):
        self.array = [None] * self.size
        self.count = 0

