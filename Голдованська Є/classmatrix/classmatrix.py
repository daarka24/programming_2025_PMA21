class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{self.matrix}"

    def plus(self, other):
        if len(self.matrix) != len(other.matrix):
            print("Різний розмір матриць")
            return []
        new_matrix = []
        for i in range(len(other.matrix)):
            new_row = []
            for j in range(len(self.matrix[i])):
                try:
                    new_row.append(self.matrix[i][j] + other.matrix[i][j])
                except IndexError:
                    print("Різний розмір матриць")
                    return[]
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def minus(self, other):
        if len(self.matrix) != len(other.matrix):
            print("Різний розмір матриць")
            return []
        new_matrix = []
        for i in range(len(other.matrix)):
            new_row = []
            for j in range(len(self.matrix[i])):
                try:
                    new_row.append(self.matrix[i][j] - other.matrix[i][j])
                except IndexError:
                    print("Різний розмір матриць")
                    return []
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def multiply(self, other):
        length = len(self.matrix)
        result_matrix = [[0 for _ in range(length)] for _ in range(length)]

        for i in range(length):
            for j in range(length):
                for k in range(length):
                    try:
                        result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    except IndexError:
                        print("Різний розмір матриць")
                        return []
        return Matrix(result_matrix)

    @staticmethod
    def minor(matrix, i, j):
        return [[matrix[p][k] for k in range(len(matrix[p])) if k != j] for p in range(len(matrix)) if p != i]

    @staticmethod
    def det(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        d = 0
        for j in range(len(matrix[0])):
            minormatrix = Matrix.minor(matrix, 0, j)
            d += matrix[0][j] * (-1) ** j * Matrix.det(minormatrix)
        return d

    @staticmethod
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    @staticmethod
    def algebraic_addition(matrix, i, j):
        return ((-1) ** (i + j + 2)) * Matrix.det(Matrix.minor(matrix, i, j))

    @staticmethod
    def inverse_matrix(matrix):
        determinant = Matrix.det(matrix)

        if determinant == 0:
            return []

        inverse_demo = Matrix.transpose(
            [[Matrix.algebraic_addition(matrix, i, j) / determinant for j in range(len(matrix[i]))] for i in
             range(len(matrix))])
        return Matrix([[inverse_demo[i][j] / determinant for j in range(len(inverse_demo[i]))] for i in
                       range(len(inverse_demo))])

    def divide(self, other):
        try:
            inverse = Matrix.inverse_matrix(other.matrix)
            if inverse:
                return self.multiply(inverse)
        except:
            print("Неможливо поділити")
            return []

def str_to_float(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])

with open("in.txt", "r") as file:
    read = file.read()

matrices = read.split("m")
matrices = [matrix.split("\n") for matrix in matrices]

first_matrix = [row.split() for row in matrices[0] if row != ""]
second_matrix = [row.split() for row in matrices[1] if row != ""]

str_to_float(first_matrix)
str_to_float(second_matrix)

first_matrix = Matrix(first_matrix)
second_matrix = Matrix(second_matrix)

result = [first_matrix.plus(second_matrix),
          first_matrix.minus(second_matrix),
          first_matrix.multiply(second_matrix)]

div = first_matrix.divide( second_matrix)
operations = ["+", "-", "*"]

if div:
    result.append(div)
    operations.append("/")


with open("out.txt", "w") as file:
    for i in range(len(result)):
        file.write(f"{first_matrix} {operations[i]} {second_matrix} = {result[i]}\n")
