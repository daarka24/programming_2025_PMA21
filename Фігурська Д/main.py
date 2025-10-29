try:
    with open("matrix1.txt", "r") as f:
        lines1 = [line.strip() for line in f if line.strip() != ""]
    m1 = [[float(x) for x in line.split(",")] for line in lines1]
except FileNotFoundError:
    print("error? can`t find file")
    m1 = None
except ValueError:
    print("error, don`t have numbers")
    m1 = None

try:
    with open("matrix2.txt", "r") as f:
        lines2 = [line.strip() for line in f if line.strip() != ""]
    m2 = [[float(x) for x in line.split(",")] for line in lines2]
except FileNotFoundError:
    print("error? can`t find file")
    m2 = None
except ValueError:
    print("error, don`t have numbers")
    m2 = None


def addMatrix(x, y):
    return [[x[i][j] + y[i][j] for j in range(3)] for i in range(3)]

def subMatrix(x, y):
    return [[x[i][j] - y[i][j] for j in range(3)] for i in range(3)]


def mulMatrix(x, y):
    R = [[0.0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = 0.0
            for k in range(3):
                s += x[i][k] * y[k][j]
            R[i][j] = s
    return R

def inverse3x3(M):
    a = M[0][0]
    b = M[0][1]
    c = M[0][2]

    d = M[1][0]
    e = M[1][1]
    f = M[1][2]

    g = M[2][0]
    h = M[2][1]
    i = M[2][2]

    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    if det==0:
        print("det=0, something is wrong")
        return None
    transpose = [
        [(e*i - f*h)/det, (c*h - b*i)/det, (b*f - c*e)/det],
        [(f*g - d*i)/det, (a*i - c*g)/det, (c*d - a*f)/det],
        [(d*h - e*g)/det, (b*g - a*h)/det, (a*e - b*d)/det]
    ]
    return transpose


try:
    add = addMatrix(m1, m2)
except Exception:
    add = "error adding"

try:
    sub = subMatrix(m1, m2)
except Exception:
    sub = "error subtracting"

try:
    mul = mulMatrix(m1, m2)
except Exception:
    mul = "error while multiplying"

try:
    inv = inverse3x3(m2)
    if inv:
        div = mulMatrix(m1, inv)
    else:
        div = "can`t divide"
except Exception:
    div = "error while dividing"


try:
    with open("result.txt", "w") as f:
        f.write(f"add: {add}\n")
        f.write(f"sub: {sub}\n")
        f.write(f"mul: {mul}\n")
        f.write(f"div: {div}\n")
except Exception:
    print("could not write results")
