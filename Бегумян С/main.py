import numpy as np


def vec_to_str(vec):
    return "(" + ",".join([str(round(x, 2)) for x in vec]) + ")"

with open('numb.txt', 'r') as file:
    vectors = [np.array(list(map(float, line.strip().split()))) for line in file]
if len(vectors) < 2:
    print("should be two vectors in numb.txt file")
else:
    v1, v2 = vectors[0], vectors[1]

    results = [
        (v1 + v2, "+"),
        (v1 - v2, "-"),
        (v1 * v2, "*"),
        ([a/b if b != 0 else None for a, b in zip (v1, v2)], "/")
    ]
    with open('result.txt', 'w') as file:
        [file.write(vec_to_str(v1) + " " + op + " " + vec_to_str(v2) + " = " + vec_to_str(res) + "\n")
         for res, op in results]
