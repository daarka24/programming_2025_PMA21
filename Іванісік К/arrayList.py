class ArrayList:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.count = 0

    def __str__(self):
        return str(self.data[:self.count])

    def addItem(self, item):
        if self.count == self.size:
            self.size = int(self.size * 1.5 + 1)
            data_new = [None] * self.size
            for i in range(self.count):
                data_new[i] = self.data[i]
            self.data = data_new

        self.data[self.count] = item
        self.count += 1

    def deleteItem(self, index):
        if index < 0 or index >= self.count:
            print("Index out of range")
            return

        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.count - 1] = None
        self.count -= 1

    def insertItem(self, index, item):
        if index < 0 or index > self.count:
            print("Index out of range")
            return

        if self.count == self.size:
            self.size = int(self.size * 1.5 + 1)
            data_new = [None] * self.size
            for i in range(self.count):
                data_new[i] = self.data[i]
            self.data = data_new

        for i in range(self.count, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = item
        self.count += 1
    def clear(self):
        self.data = [None] * self.size
        self.count = 0

x = ArrayList(8)
print(f"Створили: {x} Лічильник: {x.count}, Ємність: {x.size}")
x.addItem(1)
x.addItem(2)
x.addItem(3)
x.addItem(4)
x.addItem(5)
x.addItem(6)
x.addItem(7)
x.addItem(8)
print(f"Додали 1-8: {x} Лічильник: {x.count}, Ємність: {x.size}")

x.deleteItem(3)
print(f"Видалили елемент [1]: {x} Лічильник: {x.count}, Ємність: {x.size}")

x.insertItem(0, 10)
print(f"Вставили 10 в [0]: {x} Лічильник: {x.count}, Ємність: {x.size}")

x.addItem(76)
print(f"Додали 5: {x} Лічильник: {x.count}, Ємність: {x.size}")

x.addItem(6)
print(f"Додали 6 (розширення): {x} Лічильник: {x.count}, Ємність: {x.size}")

x.insertItem(x.count, 56)
print(f"Вставили 56 в кінець: {x} Лічильник: {x.count}, Ємність: {x.size}")

x.clear()
print(f"Очистили: {x} Лічильник: {x.count}, Ємність: {x.size}")