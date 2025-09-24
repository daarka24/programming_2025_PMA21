

with open("file.txt", "r") as file:
 line_one=file.readline()
 line_two=file.readline()

line_one=line_one.split()
line_two=line_two.split()
vector_one=[]
vector_two=[]

for i in line_one:
    vector_one.append(float(i))
for i in line_two:
    vector_two.append(float(i))
print("Вхідні значення: ")
print(vector_one)
print(vector_two)
print("\n")
def addvector(vector_one, vector_two):
    return tuple([vector_one[i] + vector_two[i] for i in range(len(vector_one))])
def minusvector(vector_one, vector_two):
    return tuple([vector_one[i] - vector_two[i] for i in range(len(vector_one))])
def multiplyvector(vector_one, vector_two):
    return tuple([vector_one[i] * vector_two[i] for i in range(len(vector_one))])
def dividevector(vector_one, vector_two):
    return tuple([vector_one[i] / vector_two[i] for i in range(len(vector_one))])

print("Результат:")
print(addvector(vector_one, vector_two))
print(minusvector(vector_one, vector_two))
print(multiplyvector(vector_one, vector_two))
print(dividevector(vector_one, vector_two))
with open("result.txt", "w") as file:
    file.write("sum:" )
    file.write(str(addvector(vector_one, vector_two)))
    file.write("\n")
    file.write("subt:")
    file.write(str(minusvector(vector_one, vector_two)))
    file.write("\n")
    file.write("multiply:")
    file.write(str(multiplyvector(vector_one, vector_two)))
    file.write("\n")
    file.write("divide:")
    file.write(str(dividevector(vector_one, vector_two)))
