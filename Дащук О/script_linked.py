class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" ".join(map(str, elements)))

    def insert(self, position, data):
        if position < 0:
            print("Позиція поза межами списку")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        index = 0
        while current is not None and index < position - 1:
            current = current.next
            index += 1
        if current is None:
            print("Позиція поза межами списку")
            return
        new_node.next = current.next
        current.next = new_node

    def remove(self, position):
        if position < 0 or self.head is None:
            print("Позиція поза межами списку")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        index = 0
        while current is not None and index < position - 1:
            current = current.next
            index += 1
        if current is None or current.next is None:
            print("Позиція поза межами списку")
            return
        current.next = current.next.next

    def removeAll(self):
        self.head = None

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
            current = self.head
            while current:
                f.write(str(current.data) + " ")
                current = current.next


def menu_linkedlist_file(my_list: LinkedList, filename: str):
    my_list.load_from_file(filename)
    while True:
        print("""\n\t\t\t\t=== Menu ===
              1. Додати на позицію
              2. Видалити з позиції
              3. Видалити усі елементи
              4. Надрукувати LinkedList
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
            try:
                position = int(input("Enter index: "))
                data = int(input("Enter data: "))
            except ValueError:
                print("Індекс і дані мають бути цілими числами")
                continue
            my_list.insert(position, data)
            my_list.print_list()
            my_list.save_to_file(filename)
        elif choice == 2:
            try:
                position = int(input("Enter index: "))
            except ValueError:
                print("Індекс має бути цілим числом")
                continue
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
            try:
                data = int(input("Enter data: "))
            except ValueError:
                print("Дані мають бути цілим числом")
                continue
            my_list.append(data)
            my_list.print_list()
            my_list.save_to_file(filename)
        else:
            print("Choice out of range, try again")


filename = "linked_data.txt"
my_linked = LinkedList()
menu_linkedlist_file(my_linked, filename)
