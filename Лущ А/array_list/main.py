from array_list import ArrayList

INPUT_FILE = "input_data.txt"
OUTPUT_FILE = "output_data.txt"


def print_menu():
    print("\n=== ArrayList Menu ===")
    print("1. Завантажити дані з input_data.txt")
    print("2. Додати елемент")
    print("3. Вставити елемент по індексу")
    print("4. Видалити елемент по індексу")
    print("5. Очистити масив")
    print("6. Показати поточний масив")
    print("7. Зберегти масив у output_data.txt")
    print("0. Вийти")
    print("=====================")


def main():
    arr = ArrayList()
    while True:
        print_menu()
        choice = input("Оберіть дію: ")

        if choice == "1":
            try:
                arr.load_from_file(INPUT_FILE)
                print(f"Дані завантажені з {INPUT_FILE}.")
            except FileNotFoundError:
                print(f"Файл {INPUT_FILE} не знайдено!")

        elif choice == "2":
            value = input("Введіть елемент для додавання: ")
            arr.add(value)
            print("Елемент додано.")

        elif choice == "3":
            index = int(input("Введіть індекс для вставки: "))
            value = input("Введіть елемент для вставки: ")
            try:
                arr.insert(index, value)
                print("Елемент вставлено.")
            except IndexError as e:
                print(e)

        elif choice == "4":
            index = int(input("Введіть індекс елемента для видалення: "))
            try:
                arr.remove(index)
                print("Елемент видалено.")
            except IndexError as e:
                print(e)

        elif choice == "5":
            arr.clear()
            print("Масив очищено.")

        elif choice == "6":
            print("Поточний масив:")
            print(arr.to_list())

        elif choice == "7":
            arr.save_to_file(OUTPUT_FILE)
            print(f"Масив збережено у {OUTPUT_FILE}.")

        elif choice == "0":
            print("Вихід з програми...")
            break

        else:
            print("Невірна команда! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
