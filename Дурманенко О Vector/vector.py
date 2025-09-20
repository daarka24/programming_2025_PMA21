try:
    with open("vectors.txt", "r") as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()
    with open("scalars.txt", "r") as file:
        multiply_line = file.readline().strip()
        divide_line = file.readline().strip()
except:
    print("Error: Cannot read files")
    exit()
try:
    first_vector = [float(x) for x in first_line.split()]
    second_vector = [float(x) for x in second_line.split()]
    multiply = float(multiply_line)
    divide = float(divide_line)
except:
    print("Error: Invalid data format")
    exit()
if len(first_vector) != len(second_vector):
    print("Error: Vectors must have same length")
    exit()
def sum_vector(first_vector, second_vector):
    result = []
    for i in range(len(first_vector)):
        result.append(first_vector[i] + second_vector[i])
    return result
def subtract_vector(first_vector, second_vector):
    result = []
    for i in range(len(first_vector)):
        result.append(first_vector[i] - second_vector[i])
    return result
def multiply_vector(first_vector, second_vector):
    result = []
    for i in range(len(first_vector)):
        result.append(first_vector[i] * second_vector[i])
    return result
def divide_vector(first_vector, second_vector):
    result = []
    for i in range(len(first_vector)):
        if second_vector[i] == 0:
            raise ValueError("Division by zero")
        result.append(first_vector[i] / second_vector[i])
    return result
def multiply_by_number(vector, number):
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * number)
    return result
def divide_by_number(vector, number):
    if number == 0:
        raise ValueError("Division by zero")
    result = []
    for i in range(len(vector)):
        result.append(vector[i] / number)
    return result
def vector_to_str(vector):
    return "(" + ", ".join(str(x) for x in vector) + ")"
def save_results_to_file(first_vector, second_vector, multiply, divide, filename="result.txt"):
    try:
        with open(filename, "w") as file:
            file.write("First vector: ")
            file.write(vector_to_str(first_vector))
            file.write("\n")
            file.write("Second vector: ")
            file.write(vector_to_str(second_vector))
            file.write("\n")
            file.write("Sum: ")
            file.write(vector_to_str(sum_vector(first_vector, second_vector)))
            file.write("\n")
            file.write("Subtract: ")
            file.write(vector_to_str(subtract_vector(first_vector, second_vector)))
            file.write("\n")
            file.write("Multiply: ")
            file.write(vector_to_str(multiply_vector(first_vector, second_vector)))
            file.write("\n")
            try:
                file.write("Divide: ")
                file.write(vector_to_str(divide_vector(first_vector, second_vector)))
                file.write("\n")
            except:
                file.write("Error - division by zero\n")
            file.write(f"First vector * by ({multiply}): ")
            file.write(vector_to_str(multiply_by_number(first_vector, multiply)))
            file.write("\n")
            try:
                file.write(f"First vector / by ({divide}): ")
                file.write(vector_to_str(divide_by_number(first_vector, divide)))
                file.write("\n")
            except:
                file.write(f"First vector / by ({divide}): Error - division by zero\n")
            file.write(f"Second vector * by ({multiply}): ")
            file.write(vector_to_str(multiply_by_number(second_vector, multiply)))
            file.write("\n")
            try:
                file.write(f"Second vector / by ({divide}): ")
                file.write(vector_to_str(divide_by_number(second_vector, divide)))
                file.write("\n")
            except:
                file.write(f"Second vector / by ({divide}): Error - division by zero\n")
        print("Results saved")
    except:
        print("Error: Cannot write to file")
save_results_to_file(first_vector, second_vector, multiply, divide)