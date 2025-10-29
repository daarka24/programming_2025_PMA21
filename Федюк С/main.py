def fibonacci(step, arr):

    if step == 0:
        return arr

    arr.append(arr[-1] + arr[-2])
    return fibonacci(step - 1, arr)

with open('fib.txt', 'r') as file:
    numbers = [int(i) for i in file.read().split()]

with open('steps.txt', 'r') as file:
    steps = int(file.read().strip())

fibonacci_result = fibonacci(steps, numbers)


with open('result.txt', 'w') as file:
    file.write("Fibonacci:\n")
    for numbers in fibonacci_result:
     file.write(str(numbers) + " ")


