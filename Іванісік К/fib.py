def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fibonacci(amount, arr):
    if amount == 0:
        return arr
    arr.append(arr[-1] + arr[-2])
    return fibonacci(amount - 1, arr)

def fibonacci_until(limit, arr, index=0):
    next_val = arr[-1] + arr[-2]
    if next_val >= limit:
        return arr
    arr.append(next_val)
    return fibonacci_until(limit, arr, index + 1)
with open('input.txt', 'r') as f1:
    bounds = list(map(int, f1.read().split()))
    print("Межі:", bounds)

with open('input2.txt', 'r') as f2:
    steps = int(f2.read())
    print("Кількість:", steps)

start, end = bounds
fib_numbers = fibonacci(end - start, [fib(start), fib(start + 1)])
res = ' '.join(map(str, fib_numbers))
print("Fibonacci (діапазон):", res)

with open('output.txt', 'w') as f3:
    f3.write("Fibonacci (range):\n")
    f3.write(res + "\n")

with open('input4.txt', 'r') as f4:
    limit = int(f4.read())
    print("Ліміт:", limit)

fib_numbers2 = fibonacci_until(limit, [0, 1])
res2 = ' '.join(map(str, fib_numbers2))
print("Fibonacci (limit):", res2)

with open('output.txt', 'a') as f5:
    f5.write("Fibonacci (limit):\n")
    f5.write(res2)

