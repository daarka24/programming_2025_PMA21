import sys
import os
def load_data(filename):

    data = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('::', 1)
                        if len(parts) == 2:
                            key = parts[0].strip()
                            value = parts[1].strip()
                            data[key] = value
                        else:
                            print(f"Попередження: Некоректний формат рядка, ігнорується: {line}")
            print(f"Дані успішно завантажено з {filename}")
        except Exception as e:
            print(f"Помилка при читанні файлу {filename}: {e}. Створюємо новий словник.")
            return {}
    else:
        print(f"Файл {filename} не знайдено. Створюємо новий словник.")
    return data

def save_data(filename, data):

    with open(filename, 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}::{value}\n")
    print(f"\nДані успішно збережено у файл {filename}")

def display_dictionary(dictionary, title="Словник:"):
    print(f"\n{title}")
    if not dictionary:
        print("Словник порожній.")
        return
    max_key_len = max((len(key) for key in dictionary.keys()), default=0)

    for key, value in dictionary.items():
        print(f"{key:<{max_key_len}} : {value}")


def add_entry(dictionary, key, value):
    dictionary[key] = value
    print(f"\nДодано: {key} -> {value}")


def update_entry(dictionary, key, new_value):
    if key in dictionary:
        old_value = dictionary[key]
        dictionary[key] = new_value
        print(f"\nОновлено: {key}")
        print(f"   Старе значення: {old_value}")
        print(f"   Нове значення: {new_value}")
    else:
        print(f"\nКлюч '{key}' не знайдено для оновлення.")


def delete_entry(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        print(f"\nВидалено: {key} (Марка: {value})")
    else:
        print(f"\nКлюч '{key}' не знайдено для видалення.")


def search_entry(dictionary, key):
    if key in dictionary:
        print(f"\nЗнайдено: {key} -> {dictionary[key]}")
        return dictionary[key]
    else:
        print(f"\nКлюч '{key}' не знайдено у словнику.")
        return None

DATA_FILE = "car_database.txt"
LOG_FILE = "operation_log.txt"

original_stdout = sys.stdout

try:
    with open(LOG_FILE, 'w', encoding='utf-8') as f_log:
        sys.stdout = f_log

        cars = load_data(DATA_FILE)

        display_dictionary(cars, "Початковий автопарк:")

        add_entry(cars, "Mustang", "Ford")
        display_dictionary(cars, "Після додавання 'Mustang':")

        update_entry(cars, "X5", "BMW")
        update_entry(cars, "M5", "BMW (Competition)")
        display_dictionary(cars, "Після оновлення 'M5':")

        search_entry(cars, "Civic")
        search_entry(cars, "Lanos")

        delete_entry(cars, "911")
        display_dictionary(cars, "Фінальний автопарк:")

        save_data(DATA_FILE, cars)

finally:
    sys.stdout = original_stdout

print(f"Роботу завершено.")
print(f"Результат (дані) збережено у: {DATA_FILE}")
print(f"Повний звіт (лог) операцій дивіться у: {LOG_FILE}")
'''def display_dictionary(dictionary, title="Словник:"):
    print(f"\n{title}")
    if not dictionary:
        print("Словник порожній.")
        return
    max_key_len = max(len(key) for key in dictionary.keys())

    for key, value in dictionary.items():
        print(f"{key:<{max_key_len}} : {value}")


def add_entry(dictionary, key, value):
    dictionary[key] = value
    print(f"\nДодано: {key} -> {value}")


def update_entry(dictionary, key, new_value):
    if key in dictionary:
        old_value = dictionary[key]
        dictionary[key] = new_value
        print(f"\nОновлено: {key}")
        print(f"   Старе значення: {old_value}")
        print(f"   Нове значення: {new_value}")
    else:
        print(f"\nКлюч '{key}' не знайдено для оновлення.")


def delete_entry(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        print(f"\nВидалено: {key} (Марка: {value})")
    else:
        print(f"\nКлюч '{key}' не знайдено для видалення.")


def search_entry(dictionary, key):
    if key in dictionary:
        print(f"\nЗнайдено: {key} -> {dictionary[key]}")
        return dictionary[key]
    else:
        print(f"\nКлюч '{key}' не знайдено у словнику.")
        return None


cars = {"Model S": "Tesla", "Civic": "Honda", "911": "Porsche", "M5": "BMW"}
display_dictionary(cars, "Початковий автопарк:")

add_entry(cars, "Mustang", "Ford")
display_dictionary(cars, "Після додавання 'Mustang':")

update_entry(cars, "X5", "BMW")
update_entry(cars, "M5", "BMW (Competition)")
display_dictionary(cars, "Після оновлення 'M5':")

search_entry(cars, "Civic")
search_entry(cars, "Lanos")

delete_entry(cars, "911")
display_dictionary(cars, "Фінальний автопарк:")'''