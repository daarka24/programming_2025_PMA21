from vector import Vector

if __name__ == '__main__':
    result = []
try:
    with open("in.txt", "r") as file:
        lines = file.readlines()
        x1, y1, z1 = map(float, lines[0].split())
        x2, y2, z2 = map(float, lines[1].split())
        scalar = float(lines[2])

        v1 = Vector(x1, y1, z1)
        v2 = Vector(x2, y2, z2)
        sum_v = v1 + v2
        sub = v1 - v2
        mul = v1 * v2
        truediv = v1 / v2
        s_mul = v1 * scalar
        print("Vector 1:", v1)
        print("Vector 2:", v2)
        print("Scalar:", scalar)
        print("Sum:", sum_v)
        print("Subtraction:", sub)
        print("Multiplication:", mul)
        print("Division:", truediv)
        print("Scalar multiplication:", s_mul)

        with open("out.txt", "w") as out:
            out.write(f"Vector 1:{v1}\n")
            out.write(f"Vector 2:{v2}\n")
            out.write(f"Scalar:{scalar}\n")
            out.write(f"Sum:{sum_v}\n")
            out.write(f"Sub:{sub}\n")
            out.write(f"Multi:{mul}\n")
            out.write(f"Div:{truediv}\n")
            out.write(f"Scalar multiplication:{s_mul}\n")
        print("Saved to file")
except FileNotFoundError:
    print("File not found.")
except ValueError as error:
    print("error")
