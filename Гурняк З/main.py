class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, element):
        if element is None:
            raise ValueError("Не можна додати None до списку")

        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self._size += 1

    def add_at_index(self, index, element):
        if element is None:
            raise ValueError("Не можна додати None до списку")

        if not isinstance(index, int):
            raise TypeError(f"Індекс повинен бути цілим числом, отримано {type(index).__name__}")

        if index < 0 or index > self._size:
            raise IndexError(f"Індекс {index} поза межами списку (розмір: {self._size})")

        if index == 0:
            new_node = Node(element)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self._size += 1
            return

        if index == self._size:
            self.add(element)
            return

        new_node = Node(element)
        current = self.head

        for i in range(index):
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self._size += 1

    def remove(self, element):
        if element is None:
            raise ValueError("Не можна видалити None зі списку")

        if self._size == 0:
            raise IndexError("Неможливо видалити елемент з порожнього списку")

        current = self.head

        while current is not None:
            if current.data == element:
                self._removeNode(current)
                return True
            current = current.next

        return False

    def remove_at_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Індекс повинен бути цілим числом, отримано {type(index).__name__}")

        if self._size == 0:
            raise IndexError("Неможливо видалити елемент з порожнього списку")

        if index < 0 or index >= self._size:
            raise IndexError(f"Індекс {index} поза межами списку (розмір: {self._size})")

        current = self.head

        for i in range(index):
            current = current.next

        removed_data = current.data
        self._removeNode(current)
        return removed_data

    def _removeNode(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self._size -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def __str__(self):
        if self.head is None:
            return "[]"

        result = []
        current = self.head

        while current is not None:
            result.append(str(current.data))
            current = current.next

        return "[" + ", ".join(result) + "]"

    def __len__(self):
        return self._size


def print_menu():
    print("\n=== МЕНЮ ===")
    print("1. Додати елемент в кінець")
    print("2. Додати елемент за індексом")
    print("3. Видалити елемент за значенням")
    print("4. Видалити елемент за індексом")
    print("5. Показати список")
    print("6. Показати розмір списку")
    print("7. Очистити список")
    print("0. Вихід")
    print("============")


def main():
    linked_list = LinkedList()

    while True:
        print_menu()
        choice = input("Виберіть опцію: ")

        try:
            if choice == "1":
                value = input("Введіть значення для додавання: ")
                try:
                    value = int(value)
                except ValueError:
                    pass
                linked_list.add(value)
                print(f"Елемент '{value}' додано!")

            elif choice == "2":
                index = int(input("Введіть індекс: "))
                value = input("Введіть значення: ")
                try:
                    value = int(value)
                except ValueError:
                    pass
                linked_list.add_at_index(index, value)
                print(f"Елемент '{value}' додано за індексом {index}!")

            elif choice == "3":
                value = input("Введіть значення для видалення: ")
                try:
                    value = int(value)
                except ValueError:
                    pass
                result = linked_list.remove(value)
                if result:
                    print(f"Елемент '{value}' видалено!")
                else:
                    print(f"Елемент '{value}' не знайдено!")

            elif choice == "4":
                index = int(input("Введіть індекс: "))
                removed = linked_list.remove_at_index(index)
                print(f"Елемент '{removed}' видалено за індексом {index}!")

            elif choice == "5":
                print(f"Список: {linked_list}")

            elif choice == "6":
                print(f"Розмір списку: {linked_list.size()}")

            elif choice == "7":
                linked_list.clear()
                print("Список очищено!")

            elif choice == "0":
                print("До побачення!")
                break

            else:
                print("Невірна опція! Спробуйте ще раз.")

        except (ValueError, TypeError, IndexError) as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
