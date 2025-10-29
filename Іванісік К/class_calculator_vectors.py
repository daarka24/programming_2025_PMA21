class Vector:
    def __init__(self, coords=None):
        if coords is None:
            self.coords = []
        else:
            self.coords = coords

    def add(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Вектори різної довжини")
        res = []
        for a, b in zip(self.coords, other.coords):
            res.append(a + b)
        return Vector(res)

    def sub(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Вектори різної довжини")
        res = []
        for a, b in zip(self.coords, other.coords):
            res.append(a - b)
        return Vector(res)

    def mul(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Вектори різної довжини")
        res = []
        for a, b in zip(self.coords, other.coords):
            res.append(a * b)
        return Vector(res)

    def div(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Вектори різної довжини")
        res = []
        for a, b in zip(self.coords, other.coords):
            if b == 0:
                res.append("error")
            else:
                res.append(a / b)
        return Vector(res)

    def show(self):
        return str(self.coords)

with open("vectors.txt", "r") as f:
    firstVector = list(map(int, f.readline().split()))
    secondVector = list(map(int, f.readline().split()))

firstVector = Vector(firstVector)
secondVector = Vector(secondVector)

print("Перший вектор:", firstVector.show())
print("Другий вектор:", secondVector.show())
with open("out.txt", "w") as out:
    out.write(firstVector.show() + " + " + secondVector.show() + " = " + firstVector.add(secondVector).show() + "\n")
    out.write(firstVector.show() + " - " + secondVector.show() + " = " + firstVector.sub(secondVector).show() + "\n")
    out.write(firstVector.show() + " * " + secondVector.show() + " = " + firstVector.mul(secondVector).show() + "\n")
    out.write(firstVector.show() + " / " + secondVector.show() + " = " + firstVector.div(secondVector).show() + "\n")
print("Результати записані в out.txt")
