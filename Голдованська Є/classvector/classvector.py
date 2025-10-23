class vector:

    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec}"

    def plus(self,other):
        new = []
        for i in range(len(self.vec)):
            try:
               new.append(self.vec[i] + other.vec[i])
            except IndexError:
                print("Різна довжина векторів")
                return []
        return vector(new)

    def minus(self, other):
        new = []
        for i in range(len(self.vec)):
            try:
                new.append(self.vec[i] - other.vec[i])
            except IndexError:
                print("Різна довжина векторів")
                return []
        return vector(new)

    def multiply(self, n):
        new = []
        for i in range(len(self.vec)):
            new.append(self.vec[i] * n.vec)
        return vector(new)

    def divide(self, n):
        new = []
        for i in range(len(self.vec)):
            try:
                new.append(self.vec[i] / n.vec)
            except ZeroDivisionError:
                print("Не можна ділити на нуль")
                return []
        return vector(new)

    def scalar(self, other):
        new = 0
        for i in range(len(self.vec)):
            try:
                new += (self.vec[i] * other.vec[i])
            except IndexError:
                print("Різна довжина векторів")
                return []
        return new

with open("in.txt", "r") as file:
    read = file.read()
    vecs = read.split("\n")
    vecs = vecs[0].split(), vecs[1].split(), vecs[2]
    first_vec = vector([float(num) for num in vecs[0]])
    second_vec = vector([float(num) for num in vecs[1]])
    numb = vector(float(vecs[2]))


result = [first_vec.plus(second_vec),
          first_vec.minus(second_vec),
          first_vec.scalar(second_vec),
          first_vec.multiply(numb),
          first_vec.divide(numb)]
operations = ["+", "-", "**","*", "/"]

with open("out.txt", "w") as file:
    for i in range(3):
        file.write(f"{first_vec} {operations[i]} {second_vec} = {result[i]}\n")
    for i in range(3,5):
        file.write(f"{first_vec} {operations[i]} {numb} = {result[i]}\n")