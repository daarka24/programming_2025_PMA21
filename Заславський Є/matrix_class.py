class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j]
                        for j in range(self.cols)]
                        for i in range(self.rows)])

    def __sub__(self, other):
        return Matrix([[self.data[i][j] - other.data[i][j]
                        for j in range(self.cols)]
                        for i in range(self.rows)])

    def __mul__(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_val = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(sum_val)
            result.append(row)
        return Matrix(result)

    def inverse(self):
        n = self.rows
        aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(self.data)]

        for i in range(n):
            pivot = aug[i][i]
            if abs(pivot) < 1e-12:
                raise ValueError("Матриця необернена")

            aug[i] = [x / pivot for x in aug[i]]

            for k in range(n):
                if k != i:
                    factor = aug[k][i]
                    aug[k] = [aug[k][j] - factor * aug[i][j] for j in range(2 * n)]

        inv_data = [row[n:] for row in aug]
        return Matrix(inv_data)

    def __truediv__(self, other):
        return self * other.inverse()

    def __str__(self):
        return "\n".join(" ".join(f"{x:g}" for x in row) for row in self.data)
