class MyMatrix:
    def __init__(self, data=None):
        self.data = data if data else []
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.data else 0

    def pretty(self):
        return "\n".join(" ".join(str(round(val, 2)) for val in row) for row in self.data)

    def add(self, other):
        try:
            if self.rows != other.rows or self.cols != other.cols:
                return None
            result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return MyMatrix(data=result)
        except:
            return None

    def subtract(self, other):
        try:
            if self.rows != other.rows or self.cols != other.cols:
                return None
            result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return MyMatrix(data=result)
        except:
            return None

    def multiply(self, other):
        try:
            if self.cols != other.rows:
                return None
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    val = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    row.append(val)
                result.append(row)
            return MyMatrix(data=result)
        except:
            return None

    def inverse(self):
        try:
            if self.rows != self.cols:
                return None
            size = self.rows
            identity = [[float(i == j) for j in range(size)] for i in range(size)]
            copy = [row[:] for row in self.data]
            for i in range(size):
                if copy[i][i] == 0:
                    for k in range(i + 1, size):
                        if copy[k][i] != 0:
                            copy[i], copy[k] = copy[k], copy[i]
                            identity[i], identity[k] = identity[k], identity[i]
                            break
                    else:
                        return None
                pivot = copy[i][i]
                for j in range(size):
                    copy[i][j] /= pivot
                    identity[i][j] /= pivot
                for k in range(size):
                    if k != i:
                        factor = copy[k][i]
                        for j in range(size):
                            copy[k][j] -= factor * copy[i][j]
                            identity[k][j] -= factor * identity[i][j]
            return MyMatrix(data=identity)
        except:
            return None

    def divide(self, other):
        try:
            inv = other.inverse()
            if inv is None:
                return None
            return self.multiply(inv)
        except:
            return None


class MatrixProcessor:
    def __init__(self, file1, file2, result_file):
        self.file1 = file1
        self.file2 = file2
        self.result_file = result_file

    def read_matrix_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
            matrix = []
            for line in lines:
                if line.strip():
                    matrix.append([float(x) for x in line.strip().split()])
            if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
                return None
            return matrix
        except:
            return None

    def write_matrix_to_file(self, matrix, label="Результат"):
        try:
            with open(self.result_file, "a") as f:
                f.write(label + ":\n")
                f.write(matrix.pretty() + "\n\n")
        except:
            pass

    def write_error(self, message):
        try:
            with open(self.result_file, "a") as f:
                f.write(message + "\n\n")
        except:
            pass

    def process(self):
        try:
            with open(self.result_file, "w") as f:
                f.write("Операції з матрицями\n\n")
        except:
            return

        data1 = self.read_matrix_from_file(self.file1)
        data2 = self.read_matrix_from_file(self.file2)

        if not data1 or not data2:
            self.write_error("Один з файлів порожній або має неправильний формат")
            return

        m1 = MyMatrix(data=data1)
        m2 = MyMatrix(data=data2)

        if m1.rows == 0 or m1.cols == 0 or m2.rows == 0 or m2.cols == 0:
            self.write_error("Одна з матриць порожня")
            return

        if any(len(row) != m1.cols for row in m1.data) or any(len(row) != m2.cols for row in m2.data):
            self.write_error("Матриці мають нерівномірні рядки")
            return

        results = [
            ("Додавання", m1.add(m2)),
            ("Віднімання", m1.subtract(m2)),
            ("Множення", m1.multiply(m2)),
            ("Ділення", m1.divide(m2))
        ]

        for label, result in results:
            if result:
                self.write_matrix_to_file(result, label)
            else:
                self.write_error(f"Не вдалося виконати операцію: {label}")


processor = MatrixProcessor("matrix1.txt", "matrix2.txt", "result.txt")
processor.process()
