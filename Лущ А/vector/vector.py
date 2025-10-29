def parse_vector(vector_str):
    vector_str = vector_str.strip().replace('(', '').replace(')', '')
    try:
        return [float(x.strip()) for x in vector_str.split(',')]
    except ValueError:
        print(f"Не вдалось розпізнати вектор '{vector_str}'.")
        return []


def vector_to_string(vector):
    return f"({', '.join(map(str, vector))})"


def add_vectors(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]


def subtract_vectors(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]


def multiply_vectors(v1, v2):
    return [v1[i] * v2[i] for i in range(len(v1))]


def divide_vectors(v1, v2):
    return [v1[i] / v2[i] for i in range(len(v1))]


try:
    with open("vectors.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Файл 'vectors.txt' не знайдено.")
    exit()

vectors = []
for line in lines:
    line = line.strip()
    if line:
        vector = parse_vector(line)
        if vector:
            vectors.append(vector)

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Результати обчислень векторів\n")

if len(vectors) >= 2:
    v1 = vectors[0]
    v2 = vectors[1]

    try:
        if len(v1) != len(v2):
            raise ValueError(f"Вектори мають різну кількість елементів ({len(v1)} і {len(v2)}).")

        result_add = add_vectors(v1, v2)
        result_sub = subtract_vectors(v1, v2)
        result_mult = multiply_vectors(v1, v2)
        result_div = divide_vectors(v1, v2)

        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{vector_to_string(v1)} + {vector_to_string(v2)} = {vector_to_string(result_add)}\n")
            f.write(f"{vector_to_string(v1)} - {vector_to_string(v2)} = {vector_to_string(result_sub)}\n")
            f.write(f"{vector_to_string(v1)} * {vector_to_string(v2)} = {vector_to_string(result_mult)}\n")
            f.write(f"{vector_to_string(v1)} / {vector_to_string(v2)} = {vector_to_string(result_div)}\n")

    except ZeroDivisionError:
        print("Помилка: ділення на нуль у другому векторі.")
    except ValueError as e:
        print("Помилка:", e)
else:
    print("У файлі має бути хоча б два вектори.")
