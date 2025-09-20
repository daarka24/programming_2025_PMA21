class Matrix:
    def __init__(self, data=None, file_path=None):
        if file_path:
            self.data = self._read_from_file(file_path)
        elif data:
            self.data = data
        else:
            self.data = []
    def _read_from_file(self, file_path):
        matrix = []
        with open(file_path, "r") as file:
            for line in file:
                matrix_row = []
                numbers = line.strip().split()
                for number in numbers:
                    matrix_row.append(float(number))
                if matrix_row:
                    matrix.append(matrix_row)
        return matrix
    def rows(self):
        return len(self.data)
    def columns(self):
        return len(self.data[0]) if self.data else 0
    def __add__(self, other):
        if not self._can_sum_subtract(other):
            return None
        result_data = []
        for row_index in range(self.rows()):
            result_row = []
            for column_index in range(self.columns()):
                sum_element = self.data[row_index][column_index] + other.data[row_index][column_index]
                result_row.append(sum_element)
            result_data.append(result_row)
        return Matrix(data=result_data)
    def __sub__(self, other):
        if not self._can_sum_subtract(other):
            return None
        result_data = []
        for row_index in range(self.rows()):
            result_row = []
            for column_index in range(self.columns()):
                difference_element = self.data[row_index][column_index] - other.data[row_index][column_index]
                result_row.append(difference_element)
            result_data.append(result_row)
        return Matrix(data=result_data)
    def __mul__(self, other):
        if not self._can_multiply(other):
            return None
        first_matrix_rows = self.rows()
        first_matrix_columns = self.columns()
        second_matrix_columns = other.columns()
        result_data = []
        for row_index in range(first_matrix_rows):
            result_row = []
            for column_index in range(second_matrix_columns):
                element_sum = 0
                for inner_index in range(first_matrix_columns):
                    element_sum += self.data[row_index][inner_index] * other.data[inner_index][column_index]
                result_row.append(element_sum)
            result_data.append(result_row)
        return Matrix(data=result_data)
    def __truediv__(self, other):
        if not self._can_divide(other):
            return None
        try:
            if other.rows() != other.columns():
                return None
            inverse_other = other._invert()
            if not inverse_other:
                return None
            return self * inverse_other
        except:
            print("Error: Division by zero in matrix")
            return None
    def _can_sum_subtract(self, other):
        rows_match = self.rows() == other.rows()
        columns_match = self.columns() == other.columns()
        return rows_match and columns_match
    def _can_multiply(self, other):
        first_matrix_columns = self.columns()
        second_matrix_rows = other.rows()
        return first_matrix_columns == second_matrix_rows
    def _can_divide(self, other):
        is_square_matrix = other.rows() == other.columns()
        can_multiply_with_inverse = self.columns() == other.rows()
        return is_square_matrix and can_multiply_with_inverse
    def _invert(self):
        matrix_size = self.rows()
        augmented_matrix = [row[:] for row in self.data]
        identity_matrix = [[float(row_index == column_index) for row_index in range(matrix_size)] for column_index in
                           range(matrix_size)]
        for diagonal_index in range(matrix_size):
            diagonal_element = augmented_matrix[diagonal_index][diagonal_index]
            if diagonal_element == 0:
                return None
            try:
                for column_index in range(matrix_size):
                    augmented_matrix[diagonal_index][column_index] /= diagonal_element
                    identity_matrix[diagonal_index][column_index] /= diagonal_element
            except ZeroDivisionError:
                return None
            for row_index in range(matrix_size):
                if row_index != diagonal_index:
                    current_row_scalar = augmented_matrix[row_index][diagonal_index]
                    for column_index in range(matrix_size):
                        augmented_matrix[row_index][column_index] -= current_row_scalar * \
                                                                     augmented_matrix[diagonal_index][
                                                                         column_index]
                        identity_matrix[row_index][column_index] -= current_row_scalar * \
                                                                    identity_matrix[diagonal_index][
                                                                        column_index]
        return Matrix(data=identity_matrix)
    def __str__(self):
        return '\n'.join([str(row) for row in self.data])
class MatrixCalculator:
    def __init__(self, matrix1_file, matrix2_file):
        self.first_matrix = Matrix(file_path=matrix1_file)
        self.second_matrix = Matrix(file_path=matrix2_file)
    def save_results(self, output_filename="matrix_result.txt"):
        with open(output_filename, "w") as output_file:
            output_file.write("First Matrix:\n")
            for matrix_row in self.first_matrix.data:
                output_file.write(str(matrix_row) + "\n")
            output_file.write("\n")
            output_file.write("Second Matrix:\n")
            for matrix_row in self.second_matrix.data:
                output_file.write(str(matrix_row) + "\n")
            output_file.write("\n")
            if self.first_matrix._can_sum_subtract(self.second_matrix):
                output_file.write("Matrix Sum (A + B):\n")
                sum_result = self.first_matrix + self.second_matrix
                for result_row in sum_result.data:
                    output_file.write(str(result_row) + "\n")
                output_file.write("\n")
            if self.first_matrix._can_sum_subtract(self.second_matrix):
                output_file.write("Matrix Difference (A - B):\n")
                subtraction_result = self.first_matrix - self.second_matrix
                for result_row in subtraction_result.data:
                    output_file.write(str(result_row) + "\n")
                output_file.write("\n")
            if self.first_matrix._can_multiply(self.second_matrix):
                output_file.write("Matrix Product (A * B):\n")
                multiplication_result = self.first_matrix * self.second_matrix
                for result_row in multiplication_result.data:
                    output_file.write(str(result_row) + "\n")
                output_file.write("\n")
            if self.first_matrix._can_divide(self.second_matrix):
                output_file.write("Matrix Division (A / B):\n")
                division_result = self.first_matrix / self.second_matrix
                if division_result:
                    for result_row in division_result.data:
                        output_file.write(str(result_row) + "\n")
                else:
                    output_file.write("Error: Cannot divide - division by zero or matrix not invertible\n")
                output_file.write("\n")
        print(f"Results saved to {output_filename}")
calculator = MatrixCalculator("matrix1.txt", "matrix2.txt")
calculator.save_results()