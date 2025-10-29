def limit():
    with open("input.txt", "r") as file_input:
        numbers = list(map(float, file_input.read().strip().split(",")))
    numbers.pop(-1)
    return int(max(numbers)*10)


def fibonacci(n, steps):
    if steps == 0:
        return n
    next_num = n[-1] + n[-2]
    if next_num >= limit():
        return n
    n.append(next_num)
    return fibonacci(n, steps - 1)

with open("input.txt", "r") as file_input:
    numbers = list(map(float, file_input.read().strip().split(",")))

steps = int(numbers[-1])
numbers.pop(-1)

output_list = fibonacci(numbers, steps)
with open("output.txt", "w") as file_output:
    file_output.write(", ".join(map(str, output_list)))