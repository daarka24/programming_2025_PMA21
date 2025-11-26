from Linked_class import LinkedList


def load_from_file(lst, filename):
    try:
        with open(filename, "r") as f:
            numbers = f.read().split()
            for num in numbers:
                lst.append(int(num))
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено. Створено новий.")


def save_to_file(lst, filename):
    with open(filename, "w") as f:
        current = lst.head
        while current is not None:
            f.write(str(current.data) + " ")
            current = current.next


def menu(lst, filename):
    load_from_file(lst, filename)

    while True:
        print("""
        1. Вставити по індексу
        2. Видалити по індексу
        3. Очистити список
        4. Вивести список
        5. Додати в кінець
        0. Вийти (зберегти)
        """)

        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print("Введіть число!")
            continue

        if choice == 0:
            save_to_file(lst, filename)
            print("Збережено. Вихід.")
            break

        elif choice == 1:
            index = int(input("Індекс: "))
            value = int(input("Значення: "))
            lst.insert(index, value)
            print(lst)
            save_to_file(lst, filename)

        elif choice == 2:
            index = int(input("Індекс: "))
            lst.remove_at(index)
            print(lst)
            save_to_file(lst, filename)

        elif choice == 3:
            lst.clear()
            print("Список очищено:", lst)
            save_to_file(lst, filename)

        elif choice == 4:
            print("Список:", lst)

        elif choice == 5:
            value = int(input("Значення: "))
            lst.append(value)
            print(lst)
            save_to_file(lst, filename)

        else:
            print("Невірний вибір!")


filename = "data.txt"
lst = LinkedList()
menu(lst, filename)
