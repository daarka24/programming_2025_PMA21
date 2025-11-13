from linked_list import LinkedList


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
