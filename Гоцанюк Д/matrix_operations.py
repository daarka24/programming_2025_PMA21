class Matrix:
    def __init__(self, mat_values):
        if not mat_values or not all(len(row) == len(mat_values[0]) for row in mat_values):
            raise ValueError("Некоректна матриця — рядки різної довжини або порожня.")

        self.mat_values = mat_values
        self.row_count = len(mat_values)
        self.col_count = len(mat_values[0])

    def __add__(self, other_matrix):
        return self.perform_addition(other_matrix)

    def __sub__(self, other_matrix):
        return self.perform_subtraction(other_matrix)

    def __matmul__(self, other_matrix):
        return self.perform_multiplication(other_matrix)

    def perform_addition(self, other_matrix):
        try:
            if self.row_count != other_matrix.row_count or self.col_count != other_matrix.col_count:
                raise ValueError("Матриці різних розмірів — додавання неможливе.")

            new_data = [
                [self.mat_values[i][j] + other_matrix.mat_values[i][j]
                 for j in range(self.col_count)]
                for i in range(self.row_count)
            ]
            return Matrix(new_data)
        except Exception as e:
            return Matrix([[f"Помилка при додаванні: {e}"]])

    def perform_subtraction(self, other_matrix):
        try:
            if self.row_count != other_matrix.row_count or self.col_count != other_matrix.col_count:
                raise ValueError("Матриці різних розмірів — віднімання неможливе.")

            new_data = [
                [self.mat_values[i][j] - other_matrix.mat_values[i][j]
                 for j in range(self.col_count)]
                for i in range(self.row_count)
            ]
            return Matrix(new_data)
        except Exception as e:
            return Matrix([[f"Помилка при відніманні: {e}"]])

    def perform_multiplication(self, other_matrix):
        try:
            if self.col_count != other_matrix.row_count:
                raise ValueError("Множення неможливе — кількість стовпців першої ≠ кількості рядків другої.")

            result_vals = [[0] * other_matrix.col_count for _ in range(self.row_count)]

            for i in range(self.row_count):
                for j in range(other_matrix.col_count):
                    for k in range(self.col_count):
                        result_vals[i][j] += self.mat_values[i][k] * other_matrix.mat_values[k][j]

            return Matrix(result_vals)
        except Exception as e:
            return Matrix([[f"Помилка при множенні: {e}"]])

    def calculate_inverse(self):
        if self.row_count != self.col_count:
            raise ValueError("Матриця повинна бути квадратною для обернення.")

        size_n = self.row_count
        working_A = [row[:] for row in self.mat_values]
        inv_result_I = [[float(i == j) for j in range(size_n)] for i in range(size_n)]  # Одинична матриця

        for i in range(size_n):
            if working_A[i][i] == 0:
                raise ZeroDivisionError("Ділення на нуль при оберненні матриці (нульовий елемент на діагоналі).")

            pivot_val = working_A[i][i]
            for j in range(size_n):
                working_A[i][j] /= pivot_val
                inv_result_I[i][j] /= pivot_val

            for k in range(size_n):
                if k != i:
                    mult_factor = working_A[k][i]
                    for j in range(size_n):
                        working_A[k][j] -= mult_factor * working_A[i][j]
                        inv_result_I[k][j] -= mult_factor * inv_result_I[i][j]

        return Matrix(inv_result_I)

    def perform_division(self, other_matrix):
        try:
            inv_B = other_matrix.calculate_inverse()
            return self @ inv_B
        except ZeroDivisionError:
            return Matrix([["Помилка: ділення на нуль — оберненої матриці не існує (визначник B = 0)!"]])
        except ValueError as e:
            return Matrix([[f"Помилка при діленні: {e}"]])
        except Exception as e:
            return Matrix([[f"Непередбачена помилка при діленні: {e}"]])

    def to_file(self, output_file, header_text=""):
        output_file.write(header_text + "\n")
        for data_row in self.mat_values:
            formatted_row_str = []
            for item_value in data_row:
                if isinstance(item_value, (int, float)):
                    item_value = round(item_value, 2)
                    if isinstance(item_value, float) and item_value.is_integer():
                        formatted_row_str.append(str(int(item_value)))
                    else:
                        formatted_row_str.append(str(item_value))
                else:
                    formatted_row_str.append(str(item_value))
            output_file.write(" ".join(formatted_row_str) + "\n")
        output_file.write("\n")

    def __bool__(self):
        return bool(self.mat_values)


def read_matrix(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            input_lines = [line.strip() for line in file_handle if line.strip()]

            data_list = [[int(val) for val in line.split()] for line in input_lines]

            return Matrix(data_list)
    except FileNotFoundError:
        return Matrix([[f"Файл {file_path} не знайдено!"]])
    except ValueError as e:
        return Matrix(
            [[f"Помилка у файлі {file_path}: {e}. Переконайтеся, що всі елементи — цілі числа, розділені пробілами."]])
    except Exception as e:
        return Matrix([[f"Непередбачена помилка при читанні {file_path}: {e}"]])