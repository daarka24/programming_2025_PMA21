def vec_to_str(vec):
    return "(" + ",".join([str(round(x, 2)) if isinstance(x, (int, float)) else str(x) for x in vec]) + ")"

with open('numb.txt', 'r') as file:
    vectors = [list(map(float, line.strip().split())) for line in file if line.strip()]

if len(vectors) < 2:
    print("should be two vectors in numb.txt file")
else:
    v1, v2 = vectors[0], vectors[1]

    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")

    n = len(v1)

    add = [v1[i] + v2[i] for i in range(n)]
    sub = [v1[i] - v2[i] for i in range(n)]
    mul = [v1[i] * v2[i] for i in range(n)]

    div = []
    for i in range(n):
        try:
            div.append(v1[i] / v2[i])
        except ZeroDivisionError:
            div.append("0")

    results = [
        (add, "+"),
        (sub, "-"),
        (mul, "*"),
        (div, "/")
    ]

    with open('result.txt', 'w') as file:
        [file.write(vec_to_str(v1) + " " + op + " " + vec_to_str(v2) + " = " + vec_to_str(res) + "\n")
         for res, op in results]