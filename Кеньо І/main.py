


def sum_of_vectors(vector_one, vector_two):
    return list([vector_one[i] + vector_two[i] for i in range(len(vector_one))])
def sub_of_vectors(vector_one, vector_two):
    return list([vector_one[i] - vector_two[i] for i in range(len(vector_one))])

def multiply_vectors(vector_one, vector_two):
    return list([vector_one[i]*vector_two[i] for i in range(len(vector_one))])
def divide_vectors(vector_one, vector_two):
    return list([vector_one[i]/vector_two[i] for i in range(len(vector_one))])

file_one=open('vector_one.txt')
vector_one=file_one.read()


file_two=open('vector_two.txt')
vector_two=file_two.read()



vector_one = vector_one.split(' ')
vector_one = [float(v) for v in vector_one]

vector_two = vector_two.split(' ')
vector_two = [float(v) for v in vector_two]

print(vector_one)
print(vector_two)




s=str(sum_of_vectors(vector_one, vector_two))
sb=str(sub_of_vectors(vector_one, vector_two))
m=str(multiply_vectors(vector_one, vector_two))
d=str(divide_vectors(vector_one, vector_two))

with open("output.txt", 'a') as file_three:
    file_three.write(s)
    file_three.write('\n')
    file_three.write(sb)
    file_three.write('\n')
    file_three.write(m)
    file_three.write('\n')
    file_three.write(d)

