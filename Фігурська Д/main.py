class Vector:
    def __init__(self, values): 
        self.values = values

    def add(self, other):
        result = []
        max_len = max(len(self.values), len(other.values))
        for i in range(max_len):
            try:
                result.append(self.values[i] + other.values[i])
            except Exception:
                result.append("error")
        return Vector(result)

    def sub(self, other):
        result = []
        max_len = max(len(self.values), len(other.values))
        for i in range(max_len):
            try:
                result.append(self.values[i] - other.values[i])
            except Exception:
                result.append("error")
        return Vector(result)

    def mul(self, other):
        result = []
        max_len = max(len(self.values), len(other.values))
        for i in range(max_len):
            try:
                result.append(self.values[i] * other.values[i])
            except Exception:
             result.append("error")
        return Vector(result)

    def div(self, other):
        result = []
        max_len = max(len(self.values), len(other.values))
        for i in range(max_len):
            try:
                if other.values[i] == 0:
                    return Vector(["error"])
                result.append(self.values[i] / other.values[i])
            except Exception:
                return Vector(["error"])
        return Vector(result)



with open("starters.txt", "r") as f:
    lines = f.readlines()

try:
    v1 = Vector([float(x) for x in lines[0].strip().split(",") if x.strip() != ""])
    v2 = Vector([float(x) for x in lines[1].strip().split(",") if x.strip() != ""])
except ValueError as e:
    print(f"error {e}")
    exit()

if len(v1.values) != len(v2.values):
    print("error. vectors have different lengths")
else:
    add_res = v1.add(v2)
    sub_res = v1.sub(v2)
    mul_res = v1.mul(v2)
    div_res = v1.div(v2)
    try:
        with open("results.txt", "w") as f:
            f.write("add: " + str(add_res.values) + "\n")
            f.write("sub: " + str(sub_res.values) + "\n")
            f.write("mul: " + str(mul_res.values) + "\n")
            f.write("div: " + str(div_res.values) + "\n")
        print("results in 'results.txt'")
    except Exception:
        print("could not write results to file")