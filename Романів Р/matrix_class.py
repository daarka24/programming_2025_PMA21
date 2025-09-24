class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __repr__(self):
        return str(self.matrix)


    def __str__(self):
        return str(self.matrix)


    def __iter__(self):
        return iter(self.matrix)


    # провірка на правильні розміри матриці
    def _check_length_of_matrices(self, other):
        if len(self.matrix) != len(other.matrix):
            return False

        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return False
        return True


    def _columns_equal_to_rows(self, other):
        return len(self.matrix[0]) == len(other.matrix)


    # додавання
    def sum(self, other):
        if not self._check_length_of_matrices(other):
            print("the length of the matrices must be equal")
            return

        new_matrix = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                new_matrix[i][j] += other.matrix[i][j]

        return Matrix(new_matrix)


    # віднімання
    def sub(self, other):
        if not self._check_length_of_matrices(other):
            print("the length of the matrices must be equal")
            return

        new_matrix = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                new_matrix[i][j] -= other.matrix[i][j]

        return Matrix(new_matrix)


    # множення
    def mul(self, other):
        if not self._columns_equal_to_rows(other):
            print("columns must be equal to rows")
            return
        try:
            new_matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    el = 0
                    for k in range(len(self.matrix)):
                        el += self.matrix[i][k] * other.matrix[k][j]
                    row.append(el)
                new_matrix.append(row)
        except IndexError:
            print("Our list is not matrix")
            return


        return Matrix(new_matrix)


    # ділення
    @staticmethod
    def sub_matr(matrix, i, j):
        return [[matrix[p][k] for k in range(len(matrix[p])) if k != j] for p in range(len(matrix)) if p != i]

    @staticmethod
    def det(matrix):
        if len(matrix) == 1:
            return matrix[0][0]

        d = 0
        for j in range(len(matrix[0])):
            submatrix = Matrix.sub_matr(matrix, 0, j)
            d += matrix[0][j] * (-1) ** j * Matrix.det(submatrix)
        return d

    @staticmethod
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    @staticmethod
    def algebraic_addition(matrix, i, j):
        return ((-1) ** (i + j + 2)) * Matrix.det(Matrix.sub_matr(matrix, i, j))

    @staticmethod
    def inverse(matrix):
        determinant = Matrix.det(matrix)

        if determinant == 0:
            print("Матриця не має оберненої. Детермінант = 0.")
            return []

        almost_inverse = Matrix.transpose([[Matrix.algebraic_addition(matrix, i, j) / determinant for j in range(len(matrix[i]))] for i in range(len(matrix))])
        return Matrix([[almost_inverse[i][j] / determinant for j in range(len(almost_inverse[i]))] for i in range(len(almost_inverse))])

    def div(self, other):
        try:
            inversed = Matrix.inverse(other.matrix)
            return self.mul(inversed)
        except:
            print("неможливо поділити")
            return []

