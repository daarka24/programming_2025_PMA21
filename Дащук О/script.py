class Vector:
    def __init__(self, values):
        self.values = values

    def length(self):
        return len(self.values)

    def __getitem__(self, i):
        return self.values[i]

    def addvector(self, other):
        if self.length() != other.length():
            return "Error: vectors have different length"
        return tuple([self[i] + other[i] for i in range(self.length())])

    def minusvector(self, other):
        if self.length() != other.length():
            return "Error: vectors have different length"
        return tuple([self[i] - other[i] for i in range(self.length())])

    def multiplyvector(self, other):
        if self.length() != other.length():
            return "Error: vectors have different length"
        return tuple([self[i] * other[i] for i in range(self.length())])

    def dividevector(self, other):
        if self.length() != other.length():
            return "Error: vectors have different length"
        return tuple([self[i] / other[i] if other[i] != 0 else float('inf') for i in range(self.length())])

try:
    with open("file.txt", "r") as file:
        lines = file.readlines()
        vector_one = Vector([float(a) for a in lines[0].strip().split()])
        vector_two = Vector([float(a) for a in lines[1].strip().split()])
except:
    print("File not found.")

sum_result = vector_one.addvector(vector_two)
min_result = vector_one.minusvector(vector_two)
mult_result=vector_one.multiplyvector(vector_two)
div_result=vector_one.dividevector(vector_two)
with open("result.txt", "w") as file:
    file.write("sum:" )
    file.write(str(sum_result))
    file.write("\n")
    file.write("subt:")
    file.write(str(min_result))
    file.write("\n")
    file.write("multiply:")
    file.write(str(mult_result))
    file.write("\n")
    file.write("division:")
    file.write(str(div_result))
