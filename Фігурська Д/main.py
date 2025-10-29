class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        result = []
        try:
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
        except Exception:
                return Matrix([["error"]])
        return Matrix(result)

    def sub(self, other):
        result = []
        try:
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] - other.matrix[i][j])
                result.append(row)
        except Exception:
                return Matrix([["error"]])
        return Matrix(result)

    def mul(self, other):
        try:
            rowA = len(self.matrix)
            colA = len(self.matrix[0])
            rowB = len(other.matrix)
            colB = len(other.matrix[0])

            if colA != rowB:
                print("Impossible to multiply matrices!")
                return Matrix([["error"]])

            result = []
            for i in range(rowA):
                row = []
                for j in range(colB):
                    s = 0
                    for k in range(colA):
                        s += self.matrix[i][k] * other.matrix[k][j]
                    row.append(s)
                result.append(row)
            return Matrix(result)
        except Exception:
            return Matrix([["error"]])

    def reverse(self):
        try:
            n = len(self.matrix)
            A = [row[:] for row in self.matrix]
            E = [[float(i == j) for j in range(n)] for i in range(n)]

            for i in range(n):
                if A[i][i] == 0:
                    for j in range(i + 1, n):
                        if A[j][i] != 0:
                            A[i], A[j] = A[j], A[i]
                            E[i], E[j] = E[j], E[i]
                            break

                div = A[i][i]
                if div == 0:
                    return Matrix([["error"]])
                for j in range(n):
                    A[i][j] /= div
                    E[i][j] /= div

                for k in range(n):
                    if k != i:
                        factor = A[k][i]
                        for j in range(n):
                            A[k][j] -= factor * A[i][j]
                            E[k][j] -= factor * E[i][j]
            return Matrix(E)
        except Exception:
            return Matrix([["error"]])

    def div(self, other):
        try:
            return self.mul(other.reverse())
        except Exception:
            return Matrix([["error"]])



try:
    with open("matrix1.txt", "r") as f:
        lines1 = [line.strip() for line in f if line.strip() != ""]
    A = Matrix([[float(x) for x in line.split(",")] for line in lines1])
except FileNotFoundError:
    print("error? can`t find file")
    A = None
except ValueError:
    print("error, don`t have numbers")
    A = None

try:
    with open("matrix2.txt", "r") as f:
        lines2 = [line.strip() for line in f if line.strip() != ""]
    B = Matrix([[float(x) for x in line.split(",")] for line in lines2])
except FileNotFoundError:
    print("error? can`t find file")
    B = None
except ValueError:
    print("error, don`t have numbers")
    B = None

if A is not None and B is not None:
    resultsum = A.add(B)
    resultsub = A.sub(B)
    resultmul = A.mul(B)
    resultdiv = A.div(B)

    with open("result.txt", "w") as f:
        f.write("ADD: \n" + str(resultsum.matrix) + "\n")
        f.write("SUB: \n" + str(resultsub.matrix) + "\n")
        f.write("MUL: \n" + str(resultmul.matrix) + "\n")
        f.write("DIV: \n" + str(resultdiv.matrix) + "\n")
else:
    print("something went wrong")