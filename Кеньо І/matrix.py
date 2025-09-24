
class Matrix:
    def __init__(self, file_one, file_two):
        self.matrix_one = self.readFromfile(file_one)
        self.matrix_two = self.readFromfile(file_two)

    @staticmethod
    def readFromfile(file):
        with open(file, 'r') as file:
            file = file.read()
            matrix = file.strip().split('\n')
            matrix = [i.split(' ') for i in matrix]
            matrix = [[float(a) for a in i] for i in matrix]
        return matrix

    def sum_of_matrix(self):
        if len(self.matrix_one)!=len(self.matrix_two):
            return None
        return [[self.matrix_one[i][j] + self.matrix_two[i][j] for j in range(len(self.matrix_one[0]))] for i in range(len(self.matrix_one))]

    def sub_of_matrix(self):
        if len(self.matrix_one)!=len(self.matrix_two):
            return None
        return [[self.matrix_one[i][j] - self.matrix_two[i][j] for j in range(len(self.matrix_one[0]))] for i in range(len(self.matrix_one))]

    def transponation(self, m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

    def multiply_matrix(self):
        if len(self.matrix_one[0]) != len(self.matrix_two):
            return None
        else:
            result = [[0 for j in range(len(self.matrix_two[0]))] for i in range(len(self.matrix_one))]

            def multiply(result, i, j, k):
                if i >= len(self.matrix_one):
                    return None
                if j >= len(self.matrix_two[0]):
                    return multiply(result, i + 1, 0, 0)
                if k >= len(self.matrix_two):
                    return multiply(result, i, j + 1, 0)
                result[i][j] += self.matrix_one[i][k] * self.matrix_two[k][j]
                multiply(result, i, j, k + 1)

            multiply(result, 0, 0, 0)
            return result


    def getMinor(self, m, i, j):
        return [r[:j] + r[j + 1:] for r in (m[:i] + m[i + 1:])]

    def getDeternminant(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for n in range(len(m)):
            determinant += ((-1) ** n) * m[0][n] * self.getDeternminant(self.getMinor(m, 0, n))
        return determinant

    def matrixInverse(self, m):
        determinant = self.getDeternminant(m)
        if determinant is None or determinant == 0:
            print("Matrix is not invertible.")
            return None
            

        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.getDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.transponation(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def divide_matrix(self):
        self.matrix_two = self.matrixInverse(self.matrix_two)
        if self.matrix_two is None:
            print("matrix has no inverse")
            return None

        return self.multiply_matrix()


matrix=Matrix('matrix_one.txt', 'matrix_two.txt')


mul=matrix.multiply_matrix()
s=matrix.sum_of_matrix()
sb=matrix.sub_of_matrix()
inv=matrix.matrixInverse(matrix.matrix_one)
t=matrix.transponation(matrix.matrix_one)
d=matrix.divide_matrix()


print(d)

with open("output.txt", 'a') as file_two:
    file_two.write('Multiplied:\n')
    if mul:
        for e in mul:
            file_two.write(' '.join(map(str, e)) + '\n')
    else:
        file_two.write('None\n')

    file_two.write('Sum:\n')
    if s:
        for e in s:
            file_two.write(' '.join(map(str, e)) + '\n')
    else:
        file_two.write('None\n')

    file_two.write('Sub:\n')
    if sb:
        for e in sb:
            file_two.write(' '.join(map(str, e)) + '\n')
    else:
        file_two.write('None\n')

    file_two.write('Inversed:\n')
    if inv:
        for e in inv:
            file_two.write(' '.join(map(str, e)) + '\n')
    else:
        file_two.write('None\n')

    file_two.write('Transposed:\n')
    for e in t:
        file_two.write(' '.join(map(str, e)) + '\n')

    file_two.write('Divided:\n')
    if d:
        for e in d:
            file_two.write(' '.join(map(str, e)) + '\n')
    else:
        file_two.write('None\n')
