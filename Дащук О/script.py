class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __getitem__(self, i):
        return self.matrix[i]
    def __len__(self):
        return len(self.matrix)

    def check_length_of_matrices(self, matrix_two):
        if len(self) != len(matrix_two):
            return False

        for i in range(len(self)):
            if len(self[i]) != len(matrix_two[i]):
                return False
        return True
    def mat_plus_mat(self, matrix_two):
        if not self.check_length_of_matrices(matrix_two):
            print("the length of the matrices must be equal")
            return
        result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(self))]
        for i in range(len(self)):
            for j in range(len(matrix_two[0])):
                result[i][j] = self[i][j] + matrix_two[i][j]
        return result

    def mat_minus_mat(self, matrix_two):
        if not self.check_length_of_matrices(matrix_two):
            print("the length of the matrices must be equal")
            return
        result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(self))]
        for i in range(len(self)):
            for j in range(len(matrix_two[0])):
                result[i][j] = self[i][j] - matrix_two[i][j]
        return result

    def mat_multi_mat(self, matrix_two):
        if not self.check_length_of_matrices(matrix_two):
            print("the length of the matrices must be equal")
            return
        result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(self))]
        for i in range(len(self)):
            for j in range(len(matrix_two[0])):
                for k in range(len(matrix_two)):
                    result[i][j] += self[i][k] * matrix_two[k][j]
        return result

    def inverse_matrix(self):
        n = len(self)
        augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(self)]

        for i in range(n):
            diag_element = augmented[i][i]
            if diag_element == 0:
                print("Error: Matrix is singular and cannot be inverted")
                return None

            for j in range(2 * n):
                augmented[i][j] /= diag_element

            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]

        return Matrix([row[n:] for row in augmented])

    def divide_matrices(self, matrix_two):
        if not self.check_length_of_matrices(matrix_two):
            print("the length of the matrices must be equal")
            return
        inv = matrix_two.inverse_matrix()
        if inv is None:
            return None
        return self.mat_multi_mat(inv)
matrix_one_list=[]
matrix_two_list=[]
try:
    with open("file.txt") as f:
        for line in f:
            matrix_one_list.append([float(x) for x in line.split()])
except FileNotFoundError:
    print("file.txt is not found")

try:
    with open("file_2.txt") as f:
        for line in f:
            matrix_two_list.append([float(x) for x in line.split()])
except FileNotFoundError:
    print("file_2.txt is not found")
matrix_one = Matrix(matrix_one_list)
matrix_two = Matrix(matrix_two_list)
try:
        with open("result.txt", "w") as file:
            file.write("Matrix One:\n")
            for row in matrix_one:
                file.write(str(row) + "\n")

            file.write("\nMatrix Two:\n")
            for row in matrix_two:
                file.write(str(row) + "\n")

            file.write("\nAddition:\n")
            sum_result = matrix_one.mat_plus_mat(matrix_two)
            if sum_result:
                for row in sum_result:
                    file.write(str(row) + "\n")
            else:
                file.write("Cannot Add Matrices\n")

            file.write("\nSubtraction:\n")
            subtraction_result = matrix_one.mat_minus_mat(matrix_two)
            if subtraction_result:
                for row in subtraction_result:
                    file.write(str(row) + "\n")
            else:
                file.write("Cannot subtract matrices\n")

            file.write("\nMultiplication:\n")
            multiplication_result = matrix_one.mat_multi_mat(matrix_two)
            if multiplication_result:
                for row in multiplication_result:
                    file.write(str(row) + "\n")
            else:
                file.write("Cannot multiply matrices\n")

            file.write("\nDivision:\n")
            division_result = matrix_one.divide_matrices(matrix_two)
            if division_result:
                for row in division_result:
                    file.write(str(row) + "\n")
            else:
                file.write("Cannot divide matrices\n")
except Exception as e:
        print(f"Error writing to file: {e}")