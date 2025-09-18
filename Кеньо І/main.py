def sum_of_matrix(m_one, m_two):
        return [[m_one[i][j] + m_two[i][j] for j in range(len(m_one[0]))] for i in range(len(m_one))]


def sub_of_matrix(m_one, m_two):
    return [[m_one[i][j] - m_two[i][j] for j in range(len(m_one[0]))] for i in range(len(m_one))]

def transponation(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]



def multiply_matrix(m_one, m_two):
    if len(m_one[0]) != len(m_two):
        raise ValueError("invalid dimensions")

    result = [[0 for j in range(len(m_two[0]))] for i in range(len(m_one))]

    def multiply(m_one, m_two, result, i, j, k):
        if i >= len(m_one):
            return None
        if j >= len(m_two[0]):
            return multiply(m_one, m_two, result, i+1, 0, 0)
        if k >= len(m_two):
            return multiply(m_one, m_two, result, i, j+1, 0)
        result[i][j] += m_one[i][k] * m_two[k][j]
        multiply(m_one, m_two, result, i, j, k+1)

    multiply(m_one, m_two, result, 0, 0, 0)
    return result


def getMinor(m,i,j):
    return [r[:j] + r[j+1:] for r in (m[:i]+m[i+1:])]

def getDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for n in range(len(m)):
        determinant += ((-1)**n)*m[0][n]*getDeternminant(getMinor(m,0,n))
    return determinant

def matrixInverse(m):
    determinant = getDeternminant(m)
    if determinant==0:
        raise ValueError("determinant must not be 0")
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transponation(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def divide_matrix(m_one, m_two):
    m_two=matrixInverse(m_two)
    return multiply_matrix(m_one, m_two)


file_one=open('matrix_one.txt')

file_one=file_one.read()
matrix_one = file_one.strip().split('\n')
matrix_one = [i.split(' ') for i in matrix_one]
matrix_one=[[float(a) for a in i] for i in matrix_one]

file_two=open('matrix_two.txt')

file_two=file_two.read()
matrix_two=file_two.strip().split('\n')

matrix_two=[i.split(' ') for i in matrix_two]
matrix_two=[[float(a) for a in i] for i in matrix_two]


mul=multiply_matrix(matrix_one, matrix_two)
div=divide_matrix(matrix_one, matrix_two)
ad=sum_of_matrix(matrix_one, matrix_two)

iv=matrixInverse(matrix_two)
t=transponation(matrix_one)

print(matrix_two)


with open("output.txt", 'a') as file_two:
    file_two.write('Trnsponated:')
    file_two.write('\n')
    for a in t:
        for i in a:
            file_two.write(str(i))
            file_two.write(' ')
        file_two.write('\n')

    file_two.write('Sum:')
    file_two.write('\n')
    for a in ad:
        for i in a:
            file_two.write(str(i))
            file_two.write(' ')
        file_two.write('\n')

    file_two.write('Multiplied:')
    file_two.write('\n')
    for a in mul:
        for i in a:
            file_two.write(str(i))
            file_two.write(' ')
        file_two.write('\n')

    file_two.write('Inversed:')
    file_two.write('\n')
    for a in iv:
        for i in a:
            file_two.write(str(i))
            file_two.write(' ')
        file_two.write('\n')

    file_two.write('Divided:')
    file_two.write('\n')
    for a in div:
        for i in a:
            file_two.write(str(i))
            file_two.write(' ')
        file_two.write('\n')

