def str_to_float(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])

def plus(first,second):
    new_matrix = []
    for i in range(len(first)):
        new_row = []
        for j in range(len(first[i])):
           new_row.append(first[i][j] + second[i][j])
        new_matrix.append(new_row)
    return new_matrix


def minus(first,second):
    new_matrix = []
    for i in range(len(first)):
        new_row = []
        for j in range(len(first[i])):
           new_row.append(first[i][j] - second[i][j])
        new_matrix.append(new_row)
    return new_matrix

def multiply(first,second):
    length = len(first)
    result_matrix = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += first[i][k] * second[k][j]
    return result_matrix


def inverse_matrix(matrix):
    augmented_matrix = [
        [
            matrix[i][j] if j < len(matrix) else int(i == j - len(matrix))
            for j in range(2 * len(matrix))
        ]
        for i in range(len(matrix))
    ]
    for i in range(len(matrix)):
        pivot = augmented_matrix[i][i]
        if pivot == 0:
            raise ValueError("Matrix is not invertible")
        for j in range(2 * len(matrix)):
            augmented_matrix[i][j] /= pivot
        for j in range(len(matrix)):
            if i != j:
                scalar = augmented_matrix[j][i]
                for k in range(2 * len(matrix)):
                    augmented_matrix[j][k] -= scalar * augmented_matrix[i][k]
    inverse = [
        [augmented_matrix[i][j] for j in range(len(matrix), 2 * len(matrix))]
        for i in range(len(matrix))
    ]
    return inverse

def divide(first,second):
    return multiply(first,inverse_matrix(second))


with open("in.txt", "r") as file:
    read = file.read()

matrices = read.split("m")
matrices = [matrix.split("\n") for matrix in matrices]

first_matrix = [row.split() for row in matrices[0] if row != ""]
second_matrix = [row.split() for row in matrices[1] if row != ""]

str_to_float(first_matrix)
str_to_float(second_matrix)

result = [plus(first_matrix,second_matrix),
          minus(first_matrix,second_matrix),
          multiply(first_matrix,second_matrix),
          divide(first_matrix,second_matrix)]

operations = ["+", "-", "*", "/"]

with open("out.txt", "w") as file:
    for i in range(len(result)):
        file.write(f"{first_matrix} {operations[i]} {second_matrix} = {result[i]}\n")

