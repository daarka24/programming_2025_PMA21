def plus(one,two):
    new = []
    for i in range(len(one)):
       new.append(one[i]+two[i])
    return new

def minus(one, two):
    new=[]
    for i in range(len(one)):
        new.append(one[i]-two[i])
    return new

def multiply(one,n):
    new = []
    for i in range(len(one)):
        new.append(one[i] * n)
    return new

def divide(one,n):
    new = []
    for i in range(len(one)):
        new.append(one[i] / n)
    return new

def scalar(one,two):
    new = 0
    for i in range(len(one)):
        new += (one[i]*two[i])
    return new

with open("in.txt", "r") as file:
    read = file.read()
    vecs = read.split("\n")
    vecs = vecs[0].split(), vecs[1].split(), vecs[2]
    first_vec = [float(num) for num in vecs[0]]
    second_vec = [float(num) for num in vecs[1]]
    numb = float(vecs[2])

result = [plus(first_vec,second_vec),
          minus(first_vec,second_vec),
          scalar(first_vec,second_vec),
          multiply(first_vec, numb),
          divide(first_vec, numb) ]

operations = ["+", "-", "**","*", "/"]

with open("out.txt", "w") as file:
    for i in range(3):
        file.write(f"{first_vec} {operations[i]} {second_vec} = {result[i]}\n")
    for i in range(3,5):
        file.write(f"{first_vec} {operations[i]} {numb} = {result[i]}\n")

