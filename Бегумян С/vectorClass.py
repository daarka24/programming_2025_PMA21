class Vector:
    def __init__(self, values):
        self.values = values

    def length(self):
        return len(self.values)

    def add(self, other):
        if self.length() != other.length():
            return "Error vectors have different lengths "
        return Vector([self.values[i] + other.values[i] for i in range(self.length())])

    def sub(self, other):
        if self.length() != other.length():
            return "Error vectors have different lengths"
        return Vector([self.values[i] - other.values[i] for i in range(self.length())])

    def mul(self, other):
        if self.length() != other.length():
            return "Error vectors have different lengths"
        return Vector([self.values[i] * other.values[i] for i in range(self.length())])

    def div(self, other):
        if self.length() != other.length():
            return "Error vectors have different lengths"
        result = []
        for i in range(self.length()):
            try:
                result.append(self.values[i] / other.values[i])
            except ZeroDivisionError:
                result.append("-")
        return Vector(result)

    def vec_to_str(self):
        return "(" + ",".join([str(x) for x in self.values]) + ")"

try:
    with open("vectors.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]
except:
    print("Error can`t read file")
    lines = []

vectors = []
if len(lines) >= 2:
    for line in lines[:2]:
        try:
            values = [float(x) for x in line.split()]
            vectors.append(Vector(values))
        except:
            print("Error invalid vector format")
else:
    print("Error not enough vectors in file")

if len(vectors) == 2:
    v1, v2 = vectors[0], vectors[1]
    results = [
        (v1.add(v2), "+"),
        (v1.sub(v2), "-"),
        (v1.mul(v2), "*"),
        (v1.div(v2), "/")
    ]
    try:
        with open("result.txt", "w") as file:
            for res, op in results:
                if isinstance(res, Vector):
                    file.write(v1.vec_to_str() + " " + op + " " + v2.vec_to_str() + " = " + res.vec_to_str() + "\n")
                else:
                    file.write(v1.vec_to_str() + " " + op + " " + v2.vec_to_str() + " = " + str(res) + "\n")
    except:
        print("Error cannot write to file")