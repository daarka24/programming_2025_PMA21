
def read_file(file):
    with open(file, "r") as line:
        lines = line.readlines()
        first_vec = [float(x) for x in lines[0].strip().split()]
        second_vec = [float(x) for x in lines[1].strip().split()]

    if len(first_vec) != len(second_vec):
        raise ValueError("Vectors must be the same length.")
    return first_vec, second_vec

class VectorCalculator:
    def __init__(self, first_vec):
        self.first_vec = first_vec

    def add_vector(self, second_vec):
        new_vector = []
        n = len(self.first_vec)
        for i in range(n):
            new_vector.append(self.first_vec[i] + second_vec[i])

        return new_vector

    def subtract_vector(self, second_vec):
        new_vector = []
        n = len(self.first_vec)
        for i in range(n):
            new_vector.append(self.first_vec[i] - second_vec[i])

        return new_vector

    def scalar_vector(self, second_vec):
        result = 0
        n = len(self.first_vec)
        for i in range(n):
            result += self.first_vec[i] * second_vec[i]
        return result

    def multiply_vector(self, second_vec):
        new_vector = []
        n = len(self.first_vec)
        for i in range(n):
            new_vector.append(self.first_vec[i] * second_vec[i])
        return new_vector

    def divide_vector(self, second_vec, num):
        error_msg = "Can't divide by zero."
        if num == 0:
            return error_msg
        new_vector1 = []
        new_vector2 = []
        n = len(self.first_vec)
        for i in range(n):
            if self.first_vec[i] == 0:
                return error_msg
            elif second_vec[i] == 0:
                return error_msg
            new_vector1.append(self.first_vec[i] / num)
            new_vector2.append(second_vec[i] / num)
        return new_vector1, new_vector2


def user_input():
    while True:
        try:
            num = float(input("enter number to divide: "))
            if num != 0:
                return num
            else:
                print("enter number greater or lower than 0.")
        except ValueError:
            print("Enter <float, or int> type, try again.")

if __name__ == "__main__":
    try:
        first_vec, second_vec = read_file("vector_nums.txt")
    except ValueError as e:
        print(f"error : {e}")
        exit(1)
    except IndexError:
        print("file must contain two lines.")
        exit(1)
    #user = user_input()
    my_vector = VectorCalculator(first_vec)

    results = {
        "added_vector": my_vector.add_vector(second_vec),
        "subtracted_vector": my_vector.subtract_vector(second_vec),
        "scalar_vector": my_vector.scalar_vector(second_vec),
        "multiplied_vector": my_vector.multiply_vector(second_vec),
        "divided_vector": my_vector.divide_vector(second_vec, 3)
    }

    with open("vector_output.txt", "w") as w:
        for key, value in results.items():
            w.write(f"{key}: {value}\n")
