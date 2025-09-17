with open("in.txt") as file1:
    lines = [line.strip() for line in file1 if line.strip()]
half = len(lines) // 2
matrix1 = [list(map(int, line.split())) for line in lines[:half]]
matrix2 = [list(map(int, line.split())) for line in lines[half:]]
print("Matrix 1:")
for row in matrix1:
    print(row)
print("Matrix 2:")
for row in matrix2:
    print(row)
if len(matrix1) != len(matrix2):
    raise ValueError("Matrix 1 and 2 have different length")

print("Sum: ")
return_s = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
for row in return_s:
    print(row)
print("Subtraction: ")
return_s2 = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
for row in return_s2:
    print(row)

row_1, cols_1 = len(matrix1), len(matrix1[0])
row_2, cols_2 = len(matrix2), len(matrix2[0])
print("Multiplication: ")
return_m = [[0 for _ in range(cols_2)] for _ in range(row_1)]
for i in range(row_1):
    for j in range(cols_2):
        for t in range(cols_1):
            return_m[i][j] += matrix1[i][t] * matrix2[t][j]
for row in return_m:
    print(row)

print("Division: ")
a, b, c = matrix2[0]
d, e, f = matrix2[1]
g, h, i = matrix2[2]
det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
if det == 0:
    raise ValueError("Division by zero")
else:
    inv_det = 1/det
    matrix2_inv = [[0] *3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != i]
            cols = [c for c in range(3) if c != j]
            m = matrix2[rows[0]][cols[0]]* matrix2[rows[1]][cols[1]] - matrix2[rows[0]][cols[1]]*matrix2[rows[1]][cols[0]]
            matrix2_inv[j][i] = inv_det * m * ((-1)**(i+j))
return_d = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        for t in range(3):
            return_d[i][j] += matrix1[i][t] * matrix2_inv[t][j]
for row in return_d:
    print(["{0:.2f}".format(x) for x in row])

    with open("out.txt", "w") as file:
        file.write("Sum: \n")
        for row in return_s:
            file.write(" ".join(map(str, row)) + "\n")
        file.write("Substraction: \n")
        for row in return_s2:
            file.write(" ".join(map(str, row)) + "\n")
        file.write("Multiplication: \n")
        for row in return_m:
            file.write(" ".join(map(str, row)) + "\n")
        file.write("Division: \n")
        for row in return_d:
            file.write(" ".join(map(str, row)) + "\n")
