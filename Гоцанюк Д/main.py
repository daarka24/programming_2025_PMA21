from matrix_operations import Matrix, read_matrix

def main():

    matrix_a = read_matrix("matrixA.txt")
    matrix_b = read_matrix("matrixB.txt")

    if not isinstance(matrix_a.mat_values[0][0], str) and not isinstance(matrix_b.mat_values[0][0], str):
        try:
            with open("result.txt", "w", encoding="utf-8") as output_file:
                (matrix_a + matrix_b).to_file(output_file, "A + B (Додавання):")
                (matrix_a - matrix_b).to_file(output_file, "A - B (Віднімання):")
                (matrix_a @ matrix_b).to_file(output_file, "A * B (Множення):")
                (matrix_a.perform_division(matrix_b)).to_file(output_file, "A / B (Ділення):")

            print(" Результати обчислень збережено у файл result.txt")

        except Exception as e:
            error_message = f" Критична помилка виконання програми: {e}"
            with open("result.txt", "w", encoding="utf-8") as output_file:
                output_file.write(error_message + "\n")
            print(error_message)
    else:
        error_message = "Критична помилка: Не вдалося зчитати одну або обидві матриці."
        if isinstance(matrix_a.mat_values[0][0], str):
            error_message += f"\nПомилка A: {matrix_a.mat_values[0][0]}"
        if isinstance(matrix_b.mat_values[0][0], str):
            error_message += f"\nПомилка B: {matrix_b.mat_values[0][0]}"

        with open("result.txt", "w", encoding="utf-8") as output_file:
            output_file.write(error_message + "\n")
        print(error_message)


if __name__ == "__main__":
    main()