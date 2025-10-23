class ArrayList:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self):
        new_capacity = int(self.capacity * 1.5) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Масив розширено до {new_capacity} елементів")

    def append(self, data):
        if self.size >= self.capacity:
            self._resize()
        self.array[self.size] = data
        self.size += 1

    def insert(self, position, data):
        if position < 0 or position > self.size:
            print("Позиція поза межами списку")
            return
        if self.size >= self.capacity:
            self._resize()
        for i in range(self.size, position, -1):
            self.array[i] = self.array[i - 1]
        self.array[position] = data
        self.size += 1

    def pop(self, position):
        if position < 0 or position >= self.size:
            print("Позиція поза межами списку")
            return
        for i in range(position, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def removeAll(self):
        self.array = [None] * self.capacity
        self.size = 0

    def print_list(self):
        if self.size == 0:
            print("Список порожній")
        else:
            print(" ".join(str(self.array[i]) for i in range(self.size)),end=", ")
            print("capacity = " + str(self.capacity))