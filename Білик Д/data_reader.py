def read_one_float(filename):
    try:
        with open(filename, "r") as f:
            content = f.read().split()
            if content:
                return float(content[0])
            else:
                raise ValueError(f"Файл '{filename}' порожній або містить лише нечислові дані.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не знайдено.")
    except ValueError:
        raise ValueError(f"Перший елемент у файлі '{filename}' не є числом.")

def read_two_floats(filename):
    try:
        with open(filename, "r") as f:
            content = f.read().split()
            if len(content) >= 2:
                return float(content[0]), float(content[1])
            else:
                raise ValueError(f"Файл '{filename}' повинен містити щонайменше 2 числа.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не знайдено.")
    except ValueError:
        raise ValueError(f"Файл '{filename}' містить нечислові дані або недостатньо елементів для перетворення.")