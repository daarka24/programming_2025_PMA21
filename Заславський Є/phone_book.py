FILENAME = "data.txt"
OUTPUT_FILE = "output.txt"


def save_data(book):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for email, info in book.items():
            line = f"{email} {info['Name']} {info['Surname']} {info['Phone']}\n"
            file.write(line)
    print(f"Дані збережено у {OUTPUT_FILE}")


def load_data():
    book = {}
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 4:
                    email, name, surname, phone = parts
                    book[email] = {"Name": name, "Surname": surname, "Phone": phone}
    except FileNotFoundError:
        pass
    return book


def show_all_contacts(book):
    if not book:
        print("Телефонна книга порожня.")
        return
    print("\nВсі контакти")
    for email, info in book.items():
        print(f"{info['Name']} {info['Surname']} ({email}) — {info['Phone']}")


def add_contact(book):
    email = input("Введіть email: ")
    if email in book:
        print("Контакт з таким email вже існує!")
        return
    name = input("Ім'я: ")
    surname = input("Прізвище: ")
    phone = input("Телефон: ")
    book[email] = {"Name": name, "Surname": surname, "Phone": phone}
    print("Контакт додано.")


def search_by_name(book):
    query = input("Введіть ім'я або прізвище для пошуку: ").lower()
    results = [(email, info) for email, info in book.items()
               if query in info['Name'].lower() or query in info['Surname'].lower()]
    if not results:
        print("Контактів не знайдено.")
        return
    print(f"\nЗнайдено {len(results)} контакт(и):")
    for email, info in results:
        print(f"{info['Name']} {info['Surname']} ({email}) — {info['Phone']}")


def update_contact(book):
    email = input("Введіть email контакту для зміни: ")
    if email not in book:
        print("Контакт не знайдено.")
        return
    info = book[email]
    name = input(f"Ім'я ({info['Name']}): ")
    surname = input(f"Прізвище ({info['Surname']}): ")
    phone = input(f"Телефон ({info['Phone']}): ")
    book[email] = {"Name": name, "Surname": surname, "Phone": phone}
    print("Контакт оновлено.")


def delete_contact(book):
    email = input("Введіть email контакту для видалення: ")
    if email in book:
        removed = book.pop(email)
        print(f"Контакт {removed['Name']} {removed['Surname']} видалено.")
    else:
        print("Контакт не знайдено.")


def main():
    book = load_data()
    while True:
        print("\nМеню:")
        print("1. Показати всі контакти")
        print("2. Додати контакт")
        print("3. Пошук контакту")
        print("4. Змінити контакт")
        print("5. Видалити контакт")
        print("6. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            show_all_contacts(book)
        elif choice == "2":
            add_contact(book)
        elif choice == "3":
            search_by_name(book)
        elif choice == "4":
            update_contact(book)
        elif choice == "5":
            delete_contact(book)
        elif choice == "6":
            save_data(book)
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
