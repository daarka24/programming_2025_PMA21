with open("vectors.txt", "r") as f:
    line1 = f.readline().split()
    line2 = f.readline().split()
v1 = list(map(int, line1))
v2 = list(map(int, line2))
print("First vector:", v1)
print("Second vector:", v2)
sums = []
diff = []
prod = []
quots = []
for a, b in zip(v1, v2):
    sums.append(a + b)
    diff.append(a - b)
    prod.append(a * b)
    try:
        q = a / b
    except ZeroDivisionError:
        q = "Cannot divide by zero"
    quots.append(q)
print("Sum:", sums)
print("Subtraction:", diff)
print("Multiplication:", prod)
print("Division:", quots)
with open("out.txt", "w") as out:
    out.write("Sum: " + str(sums) + "\n")
    out.write("Subtraction: " + str(diff) + "\n")
    out.write("Multiplication: " + str(prod) + "\n")
    out.write("Division: " + str(quots) + "\n")
