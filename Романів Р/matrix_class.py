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
            raise ValueError("the length of the matrices must be equal")

        new_matrix = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                new_matrix[i][j] += other.matrix[i][j]

        return Matrix(new_matrix)


    # віднімання
    def sub(self, other):
        if not self._check_length_of_matrices(other):
            raise ValueError("the length of the matrices must be equal")

        new_matrix = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                new_matrix[i][j] -= other.matrix[i][j]

        return Matrix(new_matrix)


    # множення
    def mul(self, other):
        if not self._columns_equal_to_rows(other):
            raise ValueError("columns must be equal to rows")

        new_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                el = 0
                for k in range(len(self.matrix)):
                    el += self.matrix[i][k] * other.matrix[k][j]
                row.append(el)
            new_matrix.append(row)

        return Matrix(new_matrix)


    # ділення
    @staticmethod
    def _eliminate(r1, r2, col, target=0):
        fac = (r2[col] - target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    def _gauss(self, a):
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i + 1, len(a)):
                    if a[i][j] != 0:
                        a[i], a[j] = a[j], a[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            for j in range(i + 1, len(a)):
                self._eliminate(a[i], a[j], i)
        for i in range(len(a) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self._eliminate(a[i], a[j], i)
        for i in range(len(a)):
            self._eliminate(a[i], a[i], i, target=1)
        return a

    def inverse(self):
        tmp = [[] for _ in self.matrix]
        for i, row in enumerate(self.matrix):
            if len(row) != len(self.matrix):
                raise ValueError("lengths must be equal")
            tmp[i].extend(row + [0] * i + [1] + [0] * (len(self.matrix) - i - 1))
        self._gauss(tmp)
        return Matrix([tmp[i][len(tmp[i]) // 2:] for i in range(len(tmp))])

    def div(self, other):
        if not self._columns_equal_to_rows(other):
            raise ValueError("columns must be equal to rows")

        return self.mul(other.inverse())
