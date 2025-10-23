class Matrix:
    def __init__(self, values):
        self.values = values

    def size(self):
        return len(self.values), len(self.values[0]) if self.values else 0

    def add(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()
        if r1 != r2 or c1 != c2:
            return "Error matrix must have the same size"
        result = [[self.values[i][j] + other.values[i][j] for j in range(c1)] for i in range(r1)]
        return Matrix(result)

    def sub(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()
        if r1 != r2 or c1 != c2:
            return "Error matrix must have the same size"
        result = [[self.values[i][j] - other.values[i][j] for j in range(c1)] for i in range(r1)]
        return Matrix(result)

    def mul(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()
        if c1 != r2:
            return "Error number of columns in A should be equal number of rows in B"
        result = []
        for i in range(r1):
            row = []
            for j in range(c2):
                s = sum(self.values[i][k] * other.values[k][j] for k in range(c1))
                row.append(s)
            result.append(row)
        return Matrix(result)

    def eliminate(self, r1, r2, col, target=0):
        fac = (r2[col] - target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    def gauss(self, a):
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i + 1, len(a)):
                    if a[j][i] != 0:
                        a[i], a[j] = a[j], a[i]
                        break
                else:
                    return "error matrix is not invertible"
            for j in range(i + 1, len(a)):
                self.eliminate(a[i], a[j], i)
        for i in range(len(a) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.eliminate(a[i], a[j], i)
        for i in range(len(a)):
            self.eliminate(a[i], a[i], i, target=1)
        return a

    def inverse(self):
        n = len(self.values)
        tmp = [[] for _ in self.values]
        for i, row in enumerate(self.values):
            tmp[i].extend(row + [0]*i + [1] + [0]*(n-i-1))
        self.gauss(tmp)
        inv = [tmp[i][n:] for i in range(n)]
        return Matrix(inv)

    def div(self, other):
        invB = other.inverse()
        if isinstance(invB, str):
            return "Cannot divide matrix"
        return self.mul(invB)

    def writeToFile(self, file, title):
        file.write(title + "\n")
        for row in self.values:
            file.write(" ".join(str(round(x, 2)) for x in row) + "\n")
        file.write("\n")


def read_matrix(filename):
    matrix = []
    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        row = [float(x) for x in line.strip().split()]
                    except:
                        print("Invalid number")
                        return []
                    if len(matrix) > 0 and len(row) != len(matrix[0]):
                        print("Missing number")
                        return []

                    matrix.append(row)
    except:
        print("Cannot open file")
        return []

    return matrix



A_val = read_matrix("matrix1.txt")
B_val = read_matrix("matrix2.txt")
if not A_val or not B_val:
    print ("no matrix")
    exit(0)
A = Matrix(A_val)
B = Matrix(B_val)

add_res = A.add(B)
sub_res = A.sub(B)
mul_res = A.mul(B)
div_res = A.div(B)

with open("result.txt", "w") as file:
    file.write("Add:\n")
    for row in add_res.values:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("Sub:\n")
    for row in sub_res.values:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("Mul:\n")
    for row in mul_res.values:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("Div:\n")
    for row in div_res.values:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")