def read_matrix_from_file(file_path):
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
def can_sum_subtract(first_matrix, second_matrix):
    rows_match = len(first_matrix) == len(second_matrix)
    columns_match = len(first_matrix[0]) == len(second_matrix[0])
    return rows_match and columns_match
def can_multiply(first_matrix, second_matrix):
    first_matrix_columns = len(first_matrix[0])
    second_matrix_rows = len(second_matrix)
    return first_matrix_columns == second_matrix_rows
def can_divide(first_matrix, second_matrix):
    is_square_matrix = len(second_matrix) == len(second_matrix[0])
    can_multiply_with_inverse = len(first_matrix[0]) == len(second_matrix)
    return is_square_matrix and can_multiply_with_inverse
def sum_matrices(first_matrix, second_matrix):
    result_matrix = []
    for row_index in range(len(first_matrix)):
        result_row = []
        for column_index in range(len(first_matrix[0])):
            sum_element = first_matrix[row_index][column_index] + second_matrix[row_index][column_index]
            result_row.append(sum_element)
        result_matrix.append(result_row)
    return result_matrix
def subtract_matrices(first_matrix, second_matrix):
    result_matrix = []
    for row_index in range(len(first_matrix)):
        result_row = []
        for column_index in range(len(first_matrix[0])):
            difference_element = first_matrix[row_index][column_index] - second_matrix[row_index][column_index]
            result_row.append(difference_element)
        result_matrix.append(result_row)
    return result_matrix
def multiply_matrices(first_matrix, second_matrix):
    first_matrix_rows = len(first_matrix)
    first_matrix_columns = len(first_matrix[0])
    second_matrix_columns = len(second_matrix[0])
    result_matrix = []
    for row_index in range(first_matrix_rows):
        result_row = []
        for column_index in range(second_matrix_columns):
            element_sum = 0
            for inner_index in range(first_matrix_columns):
                element_sum += first_matrix[row_index][inner_index] * second_matrix[inner_index][column_index]
            result_row.append(element_sum)
        result_matrix.append(result_row)
    return result_matrix
def invert_matrix(input_matrix):
    matrix_size = len(input_matrix)
    augmented_matrix = [row[:] for row in input_matrix]
    identity_matrix = [[float(row_index == column_index) for row_index in range(matrix_size)] for column_index in
                       range(matrix_size)]
    for diagonal_index in range(matrix_size):
        diagonal_element = augmented_matrix[diagonal_index][diagonal_index]
        if diagonal_element == 0:
            return []
        for column_index in range(matrix_size):
            augmented_matrix[diagonal_index][column_index] /= diagonal_element
            identity_matrix[diagonal_index][column_index] /= diagonal_element
        for row_index in range(matrix_size):
            if row_index != diagonal_index:
                current_row_scalar = augmented_matrix[row_index][diagonal_index]
                for column_index in range(matrix_size):
                    augmented_matrix[row_index][column_index] -= current_row_scalar * augmented_matrix[diagonal_index][
                        column_index]
                    identity_matrix[row_index][column_index] -= current_row_scalar * identity_matrix[diagonal_index][
                        column_index]
    return identity_matrix
def divide_matrices(dividend_matrix, divisor_matrix):
    if len(divisor_matrix) != len(divisor_matrix[0]):
        return []
    inverse_divisor_matrix = invert_matrix(divisor_matrix)
    if len(inverse_divisor_matrix) == 0:
        return []
    return multiply_matrices(dividend_matrix, inverse_divisor_matrix)
def save_results_to_file(first_matrix, second_matrix):
    output_filename = "matrix_result.txt"
    with open(output_filename, "w") as output_file:
        output_file.write("First Matrix:\n")
        for matrix_row in first_matrix:
            output_file.write(str(matrix_row) + "\n")
        output_file.write("\n")
        output_file.write("Second Matrix:\n")
        for matrix_row in second_matrix:
            output_file.write(str(matrix_row) + "\n")
        output_file.write("\n")
        if can_sum_subtract(first_matrix, second_matrix):
            output_file.write("Matrix Sum (A + B):\n")
            sum_result = sum_matrices(first_matrix, second_matrix)
            for result_row in sum_result:
                output_file.write(str(result_row) + "\n")
            output_file.write("\n")
        if can_sum_subtract(first_matrix, second_matrix):
            output_file.write("Matrix Difference (A - B):\n")
            subtraction_result = subtract_matrices(first_matrix, second_matrix)
            for result_row in subtraction_result:
                output_file.write(str(result_row) + "\n")
            output_file.write("\n")
        if can_divide(first_matrix, second_matrix):
            output_file.write("Matrix Division (A / B):\n")
            division_result = divide_matrices(first_matrix, second_matrix)
            if len(division_result) > 0:
                for result_row in division_result:
                    output_file.write(str(result_row) + "\n")
            output_file.write("\n")
        if can_multiply(first_matrix, second_matrix):
            output_file.write("Matrix Product (A * B):\n")
            multiplication_result = multiply_matrices(first_matrix, second_matrix)
            for result_row in multiplication_result:
                output_file.write(str(result_row) + "\n")
            output_file.write("\n")
first_matrix = read_matrix_from_file("matrix1.txt")
second_matrix = read_matrix_from_file("matrix2.txt")
save_results_to_file(first_matrix, second_matrix)