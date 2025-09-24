class Vector:

    def __init__(self, file_one):
        self.vector_one, self.vector_two = self.readFromfile('vectors.txt')

    @staticmethod
    def readFromfile(file):
        with open(file, 'r') as file_one:
            lines = file_one.readlines()
            vector_one = [float(v) for v in lines[0].strip().split()]
            vector_two = [float(v) for v in lines[1].strip().split()]
        return vector_one, vector_two

    def sum_of_vectors(self):
        if len(self.vector_one) != len(self.vector_two):
            print("The length of the two vectors must be equal")
            return None
        return [self.vector_one[i] + self.vector_two[i] for i in range(len(self.vector_one))]

    def sub_of_vectors(self):
        if len(self.vector_one) != len(self.vector_two):
            print("The length of the two vectors must be equal")
            return None
        return [self.vector_one[i] - self.vector_two[i] for i in range(len(self.vector_one))]

    def multiply_vectors(self):
        if len(self.vector_one) != len(self.vector_two):
            print("The length of the two vectors must be equal")
            return None
        return [self.vector_one[i] * self.vector_two[i] for i in range(len(self.vector_one))]


    def find_scalar(self):
        if len(self.vector_one) != len(self.vector_two):
            print("The length of the two vectors must be equal")
            return None
        return sum([self.vector_one[i] * self.vector_two[i] for i in range(len(self.vector_one))])
    def mul_by_n(self, n):

        return f'{[self.vector_one[i]*n for i in range(len(self.vector_one))]}\n{[self.vector_two[i]*n for i in range(len(self.vector_two))]}'
    def div_by_n(self, n):

        return f'{[self.vector_one[i]/n for i in range(len(self.vector_one))]}\n{[self.vector_two[i]*n for i in range(len(self.vector_two))]}'




with open('n.txt', 'r') as file_n:
    file_n = file_n.readlines()
    n=float(file_n[0])



vector=Vector('vectors.txt')
s=str(vector.sum_of_vectors())
sb=str(vector.sub_of_vectors())
m=str(vector.multiply_vectors())
sc=str(vector.find_scalar())
msc=str(vector.mul_by_n(n))
dsc=str(vector.div_by_n(n))

with open("output.txt", 'a') as file_two:
    file_two.write('\n')
    file_two.write(s)
    file_two.write('\n')
    file_two.write(sb)
    file_two.write('\n')
    file_two.write(m)
    file_two.write('\n')
    file_two.write(sc)
    file_two.write('\n')
    file_two.write(msc)
    file_two.write('\n')
    file_two.write(dsc)
    file_two.write('\n')
