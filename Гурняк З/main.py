def display_dictionary(dictionary, title="Словник:"):
    print(f"\n{title}")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_entry(dictionary, key, value):
    dictionary[key] = value
    print(f"\nДодано: {key} -> {value}")

def update_entry(dictionary, key, new_value):
    if key in dictionary:
        old_value = dictionary[key]
        dictionary[key] = new_value
        print(f"\nОновлено: {key}")
        print(f"Старе значення: {old_value}")
        print(f"Нове значення: {new_value}")
    else:
        print(f"\nКлюч '{key}' не знайдено у словнику")

def delete_entry(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        print(f"\nВидалено: {key} -> {value}")
    else:
        print(f"\nКлюч '{key}' не знайдено у словнику")

def search_entry(dictionary, key):
    if key in dictionary:
        print(f"\nЗнайдено: {key} -> {dictionary[key]}")
        return dictionary[key]
    else:
        print(f"\nКлюч '{key}' не знайдено у словнику")
        return None

capital_city = {"Nepal": "Kathmandu", "Ukraine": "Kyiv", "Italy": "Rome"}

display_dictionary(capital_city, "Початковий словник:")

add_entry(capital_city, "Japan", "Tokyo")
display_dictionary(capital_city, "Після додавання:")

update_entry(capital_city, "Ukraine", "Kyiv (столиця)")
display_dictionary(capital_city, "Після оновлення:")

search_entry(capital_city, "Italy")

delete_entry(capital_city, "Nepal")
display_dictionary(capital_city, "Фінальний словник:")
