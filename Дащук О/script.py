class ArrayList:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = int(self.capacity * 1.5) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, data):
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = data
        self.size += 1

    def insert(self, position, data):
        if position < 0 or position > self.size:
            print("Позиція поза межами списку")
            return
        if self.size >= self.capacity:
            self.resize()
        for i in range(self.size, position, -1):
            self.array[i] = self.array[i - 1]
        self.array[position] = data
        self.size += 1

    def remove(self, position):
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
        print(" ".join(str(self.array[i]) for i in range(self.size)),end="\n")
        print("Розмір:"+ f'{self.capacity}')

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                numbers = f.read().split()
                for num in numbers:
                    self.append(int(num))
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено. Створено порожній список.")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for i in range(self.size):
                f.write(str(self.array[i]) + " ")


def menu_arraylist_file(my_list, filename):
    my_list.load_from_file(filename)
    while True:
        print("""\n\t\t\t\t=== Menu ===
              1. Додати на позицію
              2. Видалити з позиції
              3. Видалити усі елементи
              4. Надрукувати ArrayList
              5. Додати в кінець
              0. Зупинити програму
              """)
        try:
            choice = int(input("Make a choice: "))
        except ValueError:
            print("Choice must be an integer, try again")
            continue

        if choice == 0:
            my_list.save_to_file(filename)
            print(f"Дані збережено у файл '{filename}'. Програма завершена.")
            break
        elif choice == 1:
            position = int(input("Enter index: "))
            data = int(input("Enter data: "))
            my_list.insert(position, data)
            my_list.print_list()
            my_list.save_to_file(filename)
        elif choice == 2:
            position = int(input("Enter index: "))
            my_list.remove(position)
            my_list.print_list()
            my_list.save_to_file(filename)
        elif choice == 3:
            my_list.removeAll()
            my_list.print_list()
            my_list.save_to_file(filename)
        elif choice == 4:
            my_list.print_list()
        elif choice == 5:
            data = int(input("Enter data: "))
            my_list.append(data)
            my_list.print_list()
            my_list.save_to_file(filename)
        else:
            print("Choice out of range, try again")


filename = "data.txt"
my_arraylist = ArrayList()
menu_arraylist_file(my_arraylist, filename)
