def process_vectors(input_filename="vectors.txt", output_filename="out.txt"):
    try:
        with open(input_filename, "r", encoding="utf-8") as file_in:
            first_line_data = file_in.readline().split()
            second_line_data = file_in.readline().split()

        vec1_components = list(map(int, first_line_data))
        vec2_components = list(map(int, second_line_data))

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{input_filename}' не знайдено.")
        return
    except ValueError:
        print("Помилка: Переконайтеся, що файл містить лише цілі числа, розділені пробілами.")
        return
    except Exception as e:
        print(f"Критична помилка при читанні файлу: {e}")
        return

    print("Перший вектор:", vec1_components)
    print("Другий вектор:", vec2_components)

    sum_results = []
    difference_results = []
    product_results = []
    quotient_results = []

    zero_division_occurred = False

    for comp_a, comp_b in zip(vec1_components, vec2_components):
        sum_results.append(comp_a + comp_b)
        difference_results.append(comp_a - comp_b)
        product_results.append(comp_a * comp_b)

        if comp_b == 0:
            zero_division_occurred = True

        try:
            quotient_comp = comp_a / comp_b
        except ZeroDivisionError:
            quotient_comp = None

        quotient_results.append(quotient_comp)

    if zero_division_occurred:
        message = "Ділення на нуль неможливе"
        quotient_results_output = message
    else:
        quotient_results_output = quotient_results

    print("Сума:", sum_results)
    print("Різниця:", difference_results)
    print("Множення:", product_results)
    print("Ділення:", quotient_results_output)

    try:
        with open(output_filename, "w", encoding="utf-8") as output_handle:
            output_handle.write("Сума: " + str(sum_results) + "\n")
            output_handle.write("Різниця: " + str(difference_results) + "\n")
            output_handle.write("Множення: " + str(product_results) + "\n")
            output_handle.write("Ділення: " + str(quotient_results_output) + "\n")

        print(f"\nРезультати записані у файл '{output_filename}'.")

    except Exception as e:
        print(f"Критична помилка при записі у файл: {e}")


if __name__ == "__main__":
    process_vectors()