with open("in.txt") as file1:
    lines = file1.readlines()
n1 = list(map(int, lines[0].split()))
m2 = list(map(int, lines[1].split()))
file1.close()

if len(n1) != len(m2):
    raise ValueError("n1 and m2 must have same length")
print("Vectors: ")
print(n1)
print(m2)

print("Suma: ")
result_s = [n1[i] + m2[i] for i in range(len(n1))]
print(result_s)

print("Minus: ")
result_m = [n1[i] - m2[i] for i in range(len(n1))]
print(result_m)

print("Dobutok: ")
result_d = [n1[i] * m2[i] for i in range(len(n1))]
print(result_d)

print("Dilena: ")
result_d2 = [n1[i] / m2[i] for i in range(len(n1))]
print(result_d2)

print("Skalyarnyi dobutok: ")
result_d3 = sum(n1[i] * m2[i] for i in range(len(n1)))
print(result_d3)

with open("out.txt", "w") as file:
    file.write("Suma: \n")
    file.write(" ".join(map(str, result_s)) + "\n")
    file.write("Minus: \n")
    file.write(" ".join(map(str, result_m)) + "\n")
    file.write("Dobutok: \n")
    file.write(" ".join(map(str, result_d)) + "\n")
    file.write("Dilenna: \n")
    file.write(" ".join(map(str, result_d2)) + "\n")
    file.write("Skalyarnyi dobutok: \n")
    file.write(str(result_d3) + "\n")