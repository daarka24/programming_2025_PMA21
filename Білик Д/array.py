def read(filename="data.txt"):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    data.append(number)
                except ValueError:
                    pass
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None
    return data

def write(data_structure, filename="result.txt"):
    active_elements = data_structure.elements[:len(data_structure)]
    output_data = map(str, active_elements)
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(output_data))
    except Exception as e:
        print(f"Помилка запису у файл: {e}")

class ArrayList:
    def __init__(self, capacity=10):
        self.elements = [None] * capacity
        self.size = 0
        self.capacity = capacity
        self.resize_history = [(0, capacity)]  # (розмір, місткість)
    def __len__(self):
        return self.size
    def __str__(self):
        active_elements = self.elements[:self.size]
        return f"ArrayList (Size: {self.size}, Capacity: {self.capacity}): {active_elements}"
    def __getitem__(self, index):
        if not (0 <= index < self.size):
            raise IndexError("list index out of range")
        return self.elements[index]
    def display(self):
        print(self)
    def resize(self):
        old_capacity = self.capacity
        new_capacity = int(1.5 * self.capacity) + 1
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity
        self.resize_history.append((self.size, new_capacity))
        print(f"Місткість збільшена: з {old_capacity} до {self.capacity}")
    def add(self, x, silent=False):
        if self.size == self.capacity:
            self.resize()
        self.elements[self.size] = x
        self.size += 1
        if not silent:
            print(f"Додано {x}. Розмір: {self.size}, Місткість: {self.capacity}")
    def remove_at_index(self, index):
        if not (0 <= index < self.size):
            raise IndexError(f"Індекс {index} поза межами (0-{self.size - 1})")
        removed_element = self.elements[index]
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.size - 1] = None
        self.size -= 1
        print(f"Видалено {removed_element} з індексу {index}.")
        return removed_element
    def insert_at_index(self, x, index):
        if index < 0 or index > self.size:
            raise IndexError(f"Індекс {index} поза межами (0-{self.size})")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = x
        self.size += 1
        print(f"Вставлено {x} на індекс {index}.")
    def clear(self):
        self.elements = [None] * self.capacity
        self.size = 0
        print("Список очищено.")

if __name__ == "__main__":
    data = read("data.txt")
    if data:
        print(f"Завантажено {len(data)} елементів з файлу: {data}")
        array_list = ArrayList(capacity=10)
        elements_to_add = data[:11] if len(data) >= 11 else data
        for num in elements_to_add:
            if array_list.size == array_list.capacity:
                array_list.resize()
            array_list.elements[array_list.size] = num
            array_list.size += 1
        array_list.insert_at_index(99, 1)
        array_list.display()
        if len(array_list) >= 6:
            array_list.remove_at_index(5)
        else:
            print("Список занадто малий для видалення за індексом 5.")
        array_list.display()
        write(array_list, "result.txt")
        array_list.clear()
        array_list.display()
    else:
        print("Дані відсутні")
