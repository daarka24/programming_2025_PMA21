def fibonacci_steps(amount, arr):
    if amount < 0:
        return ["Steps shoul be bigger than 0"]
    if amount == 0:
        return arr
    arr.append(arr[-1] + arr[-2])
    return fibonacci_steps(amount - 1, arr)

def fibonacci_range(start, end, arr):
    if start > end:
        return ["Beginning of the range bigger than end"]

    def build(a, b):
        next_value = a + b
        if next_value > end:
            return []
        return [next_value] + build(b, next_value)

    def filter(lst, i=0):
        if i == len(lst):
            return []
        if lst[i] >= start:
            return [lst[i]] + filter(lst, i + 1)
        return filter(lst, i + 1)

    full = arr + build(arr[-2], arr[-1])
    return filter(full)

errors = []

with open('input.txt', 'r') as file:
    numbers = [float(i) for i in file.readlines()]
    if len(numbers) < 2:
        errors.append("Should be at least 2 numbers in input.txt")

with open('steps.txt', 'r') as file:
    steps = int(file.readline())
    if steps < 0:
        errors.append("Steps should be greater than 0")

with open('limit.txt', 'r') as file:
    start_limit, end_limit = [float(x) for x in file.readline().split()]
    if start_limit > end_limit:
        errors.append("Range error: beginning bigger than end")

with open('output.txt', 'w') as file:
    if errors:
        for err in errors:
            file.write(err + "\n")
    else:
        fib_steps = fibonacci_steps(steps, numbers.copy())
        fib_range = fibonacci_range(start_limit, end_limit, numbers.copy())

        file.write("Fibonacci with " + str(steps) + " steps:\n")
        for i in fib_steps:
            file.write(str(i) + " ")
        file.write("\nFibonacci in range " + str(start_limit) + " to " + str(end_limit) + ":\n")
        for i in fib_range:
            file.write(str(i) + " ")
