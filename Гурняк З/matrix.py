class Matrix:
    def __init__(self, data):
        if not data or not data[0]:
            raise ValueError("Matrix must be non-empty and rectangular.")
        w = len(data[0])
        for row in data:
            if len(row) != w:
                raise ValueError("Matrix rows must have equal length.")
        self.data = [list(map(float, row)) for row in data]

    @staticmethod
    def from_file(path):
        rows = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                rows.append([float(x) for x in line.split()])
        return Matrix(rows)

    def shape(self):
        return len(self.data), len(self.data[0])

    def add(self, other):
        r1, c1 = self.shape()
        r2, c2 = other.shape()
        if r1 != r2 or c1 != c2:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(c1)] for i in range(r1)])

    def subtract(self, other):
        r1, c1 = self.shape()
        r2, c2 = other.shape()
        if r1 != r2 or c1 != c2:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(c1)] for i in range(r1)])

    def multiply(self, other):
        r1, c1 = self.shape()
        r2, c2 = other.shape()
        if c1 != r2:
            raise ValueError("Number of columns in A must equal number of rows in B.")
        return Matrix([[sum(self.data[i][k] * other.data[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)])

    def inverse(self):
        n, m = self.shape()
        if n != m:
            raise ValueError("Matrix must be square to invert.")
        aug = [[float(self.data[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        for i in range(n):
            pivot_row = max(range(i, n), key=lambda r: abs(aug[r][i]))
            if abs(aug[pivot_row][i]) == 0.0:
                raise ValueError("Matrix is singular and cannot be inverted.")
            if pivot_row != i:
                aug[i], aug[pivot_row] = aug[pivot_row], aug[i]
            diag = aug[i][i]
            for j in range(2 * n):
                aug[i][j] /= diag
            for r in range(n):
                if r == i:
                    continue
                factor = aug[r][i]
                if factor != 0.0:
                    for j in range(2 * n):
                        aug[r][j] -= factor * aug[i][j]
        inv = [row[n:] for row in aug]
        return Matrix(inv)

    def divide(self, other):
        return self.multiply(other.inverse())
