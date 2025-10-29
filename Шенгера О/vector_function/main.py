
def read_file(file):
    with open(file, "r") as line:
        lines = line.readlines()
        first_vec = [float(x) for x in lines[0].strip().split()]
        second_vec = [float(x) for x in lines[1].strip().split()]

    if len(first_vec) != len(second_vec):
        raise ValueError("Vectors must be the same length.")
    return first_vec, second_vec

def add_vector(first_vec, second_vec):
    new_vector = []
    n = len(first_vec)
    for i in range(n):
        new_vector.append(first_vec[i] + second_vec[i])

    return new_vector

def subtract_vector(first_vec, second_vec):
    new_vector = []
    n = len(first_vec)
    for i in range(n):
        new_vector.append(first_vec[i] - second_vec[i])

    return new_vector

def scalar_vector(first_vec, second_vec):
    result = 0
    n = len(first_vec)
    for i in range(n):
        result += first_vec[i] * second_vec[i]
    return result

def multiply_vector(first_vec, second_vec):
    new_vector = []
    n = len(first_vec)
    for i in range(n):
        new_vector.append(first_vec[i] * second_vec[i])

    return new_vector

def divide_vector(first_vec, second_vec, num):
    error_msg = "Can't divide by zero."
    if num == 0:
        return error_msg
    new_vector1 = []
    new_vector2 = []
    n = len(first_vec)
    for i in range(n):
        if first_vec[i] == 0:
            return error_msg
        elif second_vec[i] == 0:
            return error_msg
        new_vector1.append(first_vec[i] / num)
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

    results = {
        "added_vector": add_vector(first_vec, second_vec),
        "subtracted_vector": subtract_vector(first_vec, second_vec),
        "scalar_vector": scalar_vector(first_vec, second_vec),
        "multiplied_vector": multiply_vector(first_vec, second_vec),
        "divided_vector": divide_vector(first_vec, second_vec, 2)
    }

    with open("vector_output.txt", "w") as w:
        for key, value in results.items():
            w.write(f"{key}: {value}\n")
