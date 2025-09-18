def read(name):
    with open(name, "r", encoding="utf-8") as f:
        blocks = f.read().strip().split("\n\n")
        matrices = []
        for block in blocks:
            rows = block.strip().split("\n")
            matrix = [list(map(float, row.split())) for row in rows]
            matrices.append(matrix)
    return matrices[0], matrices[1]

def write(name, text):
    with open(name, "w", encoding="utf-8") as f:
        f.write(text)

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mul(A, B):
    res = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

def inverse(M):
    n = len(M)
    AM = [row[:] for row in M]
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
    return I

def determinant(M):
    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    det = 0
    for c in range(len(M)):
        minor = [row[:c] + row[c+1:] for row in (M[1:])]
        det += ((-1)**c) * M[0][c] * determinant(minor)
    return det

def div(A, B):
    if determinant(B) == 0:
        return None
    B_inv = inverse(B)
    return mul(A, B_inv)

def format_matrix(M):
    return "\n".join(" ".join(str(round(x, 2)) for x in row) for row in M)

A, B = read("numbers.txt")

result_text = "A + B:\n" + format_matrix(add(A, B)) + "\n\n"
result_text += "A - B:\n" + format_matrix(sub(A, B)) + "\n\n"
result_text += "A * B:\n" + format_matrix(mul(A, B)) + "\n\n"

result_div = div(A, B)
if result_div is None:
    result_text += "A / B:\nДілення неможливе (матриця B необернена)\n"
else:
    result_text += "A / B:\n" + format_matrix(result_div) + "\n"

write("result.txt", result_text)
