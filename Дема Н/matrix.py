class Matrix:
    def __init__(self, rows):
        if len(rows) != 3 or any(len(r) != 3 for r in rows):
            raise ValueError('rows must have 3 elements')
        self.rows = [[float(v) for v in r] for r in rows]
    def __str__(self):
        return '\n'.join(['[' + ' '.join(f"{v:.1f}" for v in r) + ']' for r in self.rows])
    def __add__(self, other):
        return Matrix([[self.rows[i][j] + other.rows[i][j] for j in range(3)] for i in range(3)])
    def __sub__(self, other):
        return Matrix([[self.rows[i][j] - other.rows[i][j] for j in range(3)] for i in range(3)])
    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = []
            for i in range(3):
                row = []
                for j in range(3):
                    s = sum([self.rows[i][j] * other.rows[j][i] for j in range(3)])
                    row.append(s)
                result.append(row)
            return Matrix(result)
        else:
            return Matrix([[self.rows[i][j] * other for j in range(3)] for i in range(3)])
    def determinant(self):
        m = self.rows
        return (
            m[0][0] * m[1][1] * m[2][2] +
            m[0][1] * m[1][2] * m[2][0] +
            m[0][2] * m[1][0] * m[2][1] -
            m[0][2] * m[1][1] * m[2][0] -
            m[0][0] * m[1][2] * m[2][1] -
            m[0][1] * m[1][0] * m[2][2]
        )
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ZeroDivisionError("Determinant cannot be 0")
        m = self.rows
        cof = [
            [
                m[(j+1)%3][(k+1)%3]*m[(j+2)%3][(k+2)%3]- m[(j+1)%3][(k+2)%3]*m[(j+2)%3][(k+1)%3]
                for k in range(3)
            ]
            for j in range(3)
        ]
        adj = [[cof[j][i] for j in range(3)] for i in range(3)]
        inv = [[adj[i][j]/det for j in range(3)] for i in range(3)]
        return Matrix(inv)
    def __truediv__(self, other):
        if isinstance(other, Matrix):
            return self * other.inverse()
        else:
            return Matrix([[self.rows[i][j] / other for j in range(3)] for i in range(3)])
    def scalar_m(self, scalar):
        return self * scalar
