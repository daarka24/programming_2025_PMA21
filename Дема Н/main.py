from matrix import Matrix as Matrix

def parse_m(lines):
    return Matrix([list(map(float, line.split())) for line in lines])

if __name__ == '__main__':
    try:
        with open('in.txt') as f:
            lines = [ln.strip() for ln in f if ln.strip()]
            if len(lines) < 7:
                raise ValueError('too many lines')
            m1 = parse_m(lines[0:3])
            m2 = parse_m(lines[3:6])
            scalar = float(lines[6])

            sum_m = m1 + m2
            sub = m1 - m2
            mul_m = m1 * m2
            div_mat = m1 / m2
            s_mul = m1 * scalar

            print("Matrix 1:\n", m1)
            print("Matrix 2:\n", m2)
            print("Scalar:\n", scalar)
            print("Sum:\n", sum_m)
            print("Sub:\n", sub)
            print("Mul:\n", mul_m)
            print("Div:\n", div_mat)
            print("Scalar Mul:\n", s_mul)

            with open('out.txt', 'w') as out:
                out.write("Matrix 1\n" + str(m1) + "\n")
                out.write("Matrix 2\n" + str(m2) + "\n")
                out.write("Scalar\n" + str(scalar) + "\n")
                out.write("Sum: " + str(sum_m) + "\n")
                out.write("Sub: " + str(sub) + "\n")
                out.write("Mul: " + str(mul_m) + "\n")
                out.write("Div: " + str(div_mat) + "\n")
                out.write("Scalar Mul: " + str(s_mul) + "\n")

            print("Saved to file")
    except FileNotFoundError:
         print("File not found")
    except ValueError:
         print("ValueError")
    except ZeroDivisionError:
         print("ZeroDivisionError")

