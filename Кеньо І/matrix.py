class Matrix:
    def __init__(self, matrix):

        self.matrix = matrix

    def __repr__(self):
        return str(self.matrix)

    def __str__(self):
        return str(self.matrix)

    def __iter__(self):
        return iter(self.matrix)

    def check_length(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return False
        return True

    def columns_to_rows(self, other):
        return len(self.matrix[0]) == len(other.matrix)

    def sum_of_matrix(self, other):
        if not self.check_length(other):
            print("The matrices must have equal dimensions.")
            return None
        try:
            new_matrix = self.matrix.copy()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new_matrix[i][j] += other.matrix[i][j]
            return Matrix(new_matrix)
        except IndexError:
            print("Error: Incompatible matrices.")
            return None

    def sub_of_matrix(self, other):
        if not self.check_length(other):
            print("The matrices must have equal dimensions.")
            return None
        try:
            new_matrix = self.matrix.copy()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new_matrix[i][j] -= other.matrix[i][j]
            return Matrix(new_matrix)
        except IndexError:
            print("Error: Incompatible matrices.")
            return None

    def mul(self, other):
        if not self.columns_to_rows(other):
            print("The number of columns in the first matrix must equal the number of rows in the second.")
            return None
        try:
            new_matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    el = 0
                    for k in range(len(self.matrix[0])):
                        el += self.matrix[i][k] * other.matrix[k][j]
                    row.append(el)
                new_matrix.append(row)
            return Matrix(new_matrix)
        except IndexError:
            print("Error: Incompatible matrices.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @staticmethod
    def sub_matrix(matrix, i, j):
        return [[matrix[p][k] for k in range(len(matrix[p])) if k != j] for p in range(len(matrix)) if p != i]

    @staticmethod
    def det(matrix):
        try:
            if len(matrix) == 1:
                return matrix[0][0]

            d = 0
            for j in range(len(matrix[0])):
                submatrix = Matrix.sub_matrix(matrix, 0, j)
                d += matrix[0][j] * (-1) ** j * Matrix.det(submatrix)
            return d
        except IndexError:
            print("Matrix is not well-formed.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while calculating the determinant: {e}")
            return None

    @staticmethod
    def get_minor(matrix, i, j):
        try:
            return ((-1) ** (i + j + 2)) * Matrix.det(Matrix.sub_matrix(matrix, i, j))
        except Exception as e:
            print(f"Error while calculating minor: {e}")
            return None

    @staticmethod
    def transpose(matrix):
        try:
            return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        except IndexError:
            print("Error: Matrix is not properly structured.")
            return None

    @staticmethod
    def inverse(matrix):
        try:
            determinant = Matrix.det(matrix)
            if determinant == 0:
                print("Matrix has no inverse (determinant is zero).")
                return None

            almost_inverse = Matrix.transpose([[Matrix.get_minor(matrix, i, j) / determinant for j in range(len(matrix[i]))] for i in range(len(matrix))])
            return Matrix([[almost_inverse[i][j] / determinant for j in range(len(almost_inverse[i]))] for i in range(len(almost_inverse))])
        except Exception as e:
            print(f"Error while calculating inverse: {e}")
            return None

    def div(self, other):
        try:
            inversed = Matrix.inverse(other.matrix)
            if inversed:
                return self.mul(inversed)
            else:
                print("Matrix division not possible.")
                return None
        except Exception as e:
            print(f"Error while dividing matrices: {e}")
            return None

