def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i + 1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(a) - i - 1))
    gauss(tmp)
    return [tmp[i][len(tmp[i]) // 2:] for i in range(len(tmp))]

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def div(A, B):
    return mul(A, inverse(B))

def read_matrix(filename):
    with open(filename, "r") as f:
        return [[float(x) for x in line.strip().split()] for line in f if line.strip()]

try:
    A = read_matrix("matrix1.txt")
    B = read_matrix("matrix2.txt")
except Exception as e:
    print("error reading", e)
    exit()

try:
    add_res = add(A, B)
    sub_res = sub(A, B)
    mul_res = mul(A, B)
    div_res = div(A, B)
except Exception as e:
    print("error calculating", e)
    exit()

# --- запис ---
with open("result.txt", "w") as file:
    file.write("Add:\n")
    for row in add_res:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("\nSub:\n")
    for row in sub_res:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("\nMul:\n")
    for row in mul_res:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")

    file.write("\nDiv:\n")
    for row in div_res:
        file.write(" ".join(str(round(x, 2)) for x in row) + "\n")