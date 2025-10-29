from vector_math import Vector


def main_function():
    try:
        with open("vectors.txt", "r", encoding="utf-8") as read_file_handle:
            line1 = read_file_handle.readline().split()
            vector1_components = list(map(int, line1))

            line2 = read_file_handle.readline().split()
            vector2_components = list(map(int, line2))

    except FileNotFoundError:
        print("Помилка: Файл 'vectors.txt' не знайдено.")
        return
    except ValueError:
        print("Помилка: Переконайтеся, що 'vectors.txt' містить тільки цілі числа, розділені пробілами.")
        return
    except Exception as e:
        print(f"Непередбачена помилка при читанні файлу: {e}")
        return

    vector1 = Vector(vector1_components)
    vector2 = Vector(vector2_components)

    print("Перший вектор:", vector1.get_string_representation())
    print("Другий вектор:", vector2.get_string_representation())

    try:
        sum_result = vector1 + vector2
        difference_result = vector1 - vector2
        product_result = vector1 * vector2

        quotient_result = None
        division_error_message = None

        try:
            quotient_result = vector1 / vector2
        except ZeroDivisionError:
            division_error_message = "Неможливо (ділення на нуль)"

        with open("out.txt", "w", encoding="utf-8") as write_file_handle:
            write_file_handle.write(f"{vector1} + {vector2} = {sum_result}\n")
            write_file_handle.write(f"{vector1} - {vector2} = {difference_result}\n")
            write_file_handle.write(f"{vector1} * {vector2} = {product_result}\n")

            if division_error_message:
                write_file_handle.write(f"{vector1} / {vector2} = {division_error_message}\n")
            else:
                write_file_handle.write(f"{vector1} / {vector2} = {quotient_result}\n")

        print("Результати обчислень записані в out.txt")

    except ValueError as ve:
        print(f"Критична помилка обчислення: {ve}")
        with open("out.txt", "w", encoding="utf-8") as write_file_handle:
            write_file_handle.write(f"ПОМИЛКА: {ve}\n")
    except Exception as e:
        print(f"Непередбачена помилка під час обчислень: {e}")


if __name__ == "__main__":
    main_function()
