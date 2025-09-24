class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    @staticmethod
    def read(name):
        with open(name, "r", encoding="utf-8") as f:
            blocks = f.read().strip().split("\n\n")
            matrices = []
            for block in blocks:
                rows = block.strip().split("\n")
                matrix = [list(map(float, row.split())) for row in rows]
                matrices.append(Matrix(matrix))
        return matrices

    def write(self, name, text):
        with open(name, "w", encoding="utf-8") as f:
            f.write(text)

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __matmul__(self, other):
        res = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(res)

    def determinant(self):
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for c in range(self.cols):
            minor = [row[:c] + row[c+1:] for row in (self.data[1:])]
            det += ((-1) ** c) * self.data[0][c] * Matrix(minor).determinant()
        return det

    def inverse(self):
        n = self.rows
        AM = [row[:] for row in self.data]
        I = [[float(i == j) for j in range(n)] for i in range(n)]
        for fd in range(n):
            if AM[fd][fd] == 0:
                raise ZeroDivisionError("Матриця має нульовий елемент на головній діагоналі")
            fd_scaler = 1.0 / AM[fd][fd]
            for j in range(n):
                AM[fd][j] *= fd_scaler
                I[fd][j] *= fd_scaler
            for i in range(n):
                if i != fd:
                    cr_scaler = AM[i][fd]
                    for j in range(n):
                        AM[i][j] -= cr_scaler * AM[fd][j]
                        I[i][j] -= cr_scaler * I[fd][j]
        return Matrix(I)

    def __truediv__(self, other):
        if other.determinant() == 0:
            raise ZeroDivisionError("Ділення неможливе: матриця необернена")
        return self @ other.inverse()

    def __str__(self):
        return "\n".join(" ".join(str(round(x, 2)) for x in row) for row in self.data)

A, B = Matrix.read("numbers.txt")

result_text = "A + B:\n" + str(A + B) + "\n\n"
result_text += "A - B:\n" + str(A - B) + "\n\n"
result_text += "A * B:\n" + str(A @ B) + "\n\n"

try:
    result_text += "A / B:\n" + str(A / B) + "\n"
except ZeroDivisionError:
    result_text += "A / B:\nДілення неможливе (матриця B необернена)\n"

A.write("result.txt", result_text)
