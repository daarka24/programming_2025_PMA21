def add(results):
    steps = [f"{v1} + {v2} = {v1 + v2}" for v1, v2 in zip(results[0], results[1])]
    results.append(f"Addition Steps: {steps}\n")
    results.append(f"Addition: {[v1 + v2 for v1, v2 in zip(results[0], results[1])]}\n")

def subtract(results):
    steps = [f"{v1} - {v2} = {v1 - v2}" for v1, v2 in zip(results[0], results[1])]
    results.append(f"Subtraction Steps: {steps}\n")
    results.append(f"Subtraction: {[v1 - v2 for v1, v2 in zip(results[0], results[1])]}\n")

def divide(results):
    steps = [f"{v1} / {v2} = {v1 / v2 if v2 != 0 else 'Division by zero'}" for v1, v2 in zip(results[0], results[1])]
    results.append(f"Division Steps: {steps}\n")
    results.append(f"Division: {[v1 / v2 if v2 != 0 else 'Division by zero' for v1, v2 in zip(results[0], results[1])]}\n")

def dot_product(results):
    steps = [f"{v1} * {v2} = {v1 * v2}" for v1, v2 in zip(results[0], results[1])]
    product_sum = sum(v1 * v2 for v1, v2 in zip(results[0], results[1]))
    steps.append(f"{' + '.join(str(v1 * v2) for v1, v2 in zip(results[0], results[1]))} = {product_sum}")
    results.append(f"Dot Product Steps: {steps}\n")
    results.append(f"Dot Product: {product_sum}\n")

def read_vectors(input_file):
    with open(input_file, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

def write_results(output_file, results):
    with open(output_file, 'w') as file:
        file.writelines(results[2:])

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    results = read_vectors(input_file)

    add(results)
    subtract(results)
    divide(results)
    dot_product(results)

    write_results(output_file, results)