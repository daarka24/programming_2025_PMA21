def read_matrix(text):
    text = text.strip().replace('],[', ']~[').replace('[', '').replace(']', '')
    rows = text.split('~')
    matrix = []
    for row in rows:
        matrix.append([float(x) for x in row.split(',')])
    return matrix

def matrix_text(m):
    return "[" + ", ".join("[" + ", ".join(str(int(x)) if x == int(x) else str(round(x, 2)) for x in row) + "]" for row in m) + "]"

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mul(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            value = 0
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
            row.append(value)
        result.append(row)
    return result

def div(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            if b[i][j] != 0:
                row.append(a[i][j] / b[i][j])
            else:
                row.append('inf')
        result.append(row)
    return result

input_file = open('matrixes.txt', 'r')
lines = input_file.readlines()
input_file.close()

output_file = open('results.txt', 'w')

for line in lines:
    line = line.strip()

    if '+' in line:
        parts = line.split('+')
        op = '+'
    elif '-' in line:
        parts = line.split('-')
        op = '-'
    elif '*' in line:
        parts = line.split('*')
        op = '*'
    elif '/' in line:
        parts = line.split('/')
        op = '/'
    else:
        continue

    a = read_matrix(parts[0])
    b = read_matrix(parts[1])

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)

    output = matrix_text(a) + f' {op} ' + matrix_text(b) + ' = ' + matrix_text(result)
    print(output)
    output_file.write(output + '\n')

output_file.close()
