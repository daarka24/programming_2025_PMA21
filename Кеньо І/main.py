
from vectors import Vector

def readFromfile(filename):
    file_path = f'/Users/ilonakeno/PycharmProjects/vectorsClass/{filename}'
    with open(file_path, 'r') as file_one:
        line = file_one.readlines()
        vector = [float(v) for v in line[0].strip().split()]
    return vector
def readN(filename):
    file_path = f'/Users/ilonakeno/PycharmProjects/vectorsClass/{filename}'
    with open(file_path, 'r') as file_n:
        file_n = file_n.readlines()
        n = file_n[0]
        return n
def print_to_file(filename, a):
    file_path = f'/Users/ilonakeno/PycharmProjects/vectorsClass/{filename}'
    with open(file_path, 'a') as file_two:
        file_two.write('Results of action:\n')
        file_two.write(str(a))
        file_two.write('\n')

if __name__=="__main__":
    vector_one=Vector(readFromfile("vector_one.txt"))
    vector_two=Vector(readFromfile("vector_two.txt"))

    n=float(readN('n.txt'))

    s=vector_one.sum_of_vectors(vector_two)
    sb=vector_one.sub_of_vectors(vector_two)
    m=vector_one.multiply_vectors(vector_two)
    sc=vector_one.find_scalar(vector_two)
    msc=vector_one.mul_by_n(vector_two, n)
    dsc=vector_one.div_by_n(vector_two, n)

    print_to_file('output.txt', s)
    print_to_file('output.txt', sb)
    print_to_file('output.txt', m)
    print_to_file('output.txt', sc)
    print_to_file('output.txt', msc)
    print_to_file('output.txt', dsc)






