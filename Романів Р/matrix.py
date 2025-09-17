#допоміжні функції
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def check_operation(rows):
    undefined_operation = True
    for i in range(len(rows)):
        if rows[i] in "+-*/":
            undefined_operation = False

    if undefined_operation:
        raise ValueError("Undefined operation")


def from_str_to_list(row):
    return [float(el) for el in row.strip().split() if is_number(el)]


#провірка на правильні розміри матриці
def check_length_of_matrices(A, B):
    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return False
    return True


def columns_equal_to_rows(A, B):
    return len(A[0]) == len(B)


#додавання
def sum(A, B):
    if not check_length_of_matrices(A, B):
        raise ValueError("the length of the matrices must be equal")

    new_matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            row.append((A[i][j] + B[i][j]))

        new_matrix.append((row))
    return new_matrix


#віднімання
def sub(A, B):
    if not check_length_of_matrices(A, B):
        raise ValueError("the length of the matrices must be equal")

    new_matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            row.append((A[i][j] - B[i][j]))

        new_matrix.append((row))
    return new_matrix


#множення
def mul(A, B):
    if not columns_equal_to_rows(A, B):
        raise ValueError("columns must be equal to rows")

    new_matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            el = 0
            for k in range(len(A)):
                el += A[i][k] * B[k][j]
            row.append(el)
        new_matrix.append(row)

    return new_matrix


#ділення
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    return [tmp[i][len(tmp[i])//2:] for i in range(len(tmp))]


def div(A, B):
    if not columns_equal_to_rows(A, B):
        raise ValueError("columns must be equal to rows")

    return mul(A, inverse(B))

if __name__ == "__main__":
    with open("input_matrix.txt", "r") as file:
        readed = file.readlines()

    rows = [row.removesuffix("\n").strip() for row in readed]

    check_operation(rows)

    first, second, separated, operator = [], [], False, None
    for i in range(len(rows)):
        if rows[i] not in "+-*/":
            if not separated:
                first.append(rows[i])
            else:
                second.append(rows[i])
        else:
            operator = rows[i]
            separated = True

    first = [from_str_to_list(row) for row in first]
    second = [from_str_to_list(row) for row in second]

    result = []
    if operator == "+":
        result = sum(first, second)

    elif operator == "-":
        result = sub(first, second)

    elif operator == "*":
        result = mul(first, second)

    elif operator == "/":
        result = div(first, second)

    with open("output_matrix.txt", "w") as file:
        for row in result:
            file.write(str(row) + "\n")

    print("Результат записано: " + str(result))
