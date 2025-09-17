from fileinput import fileno
from idlelib.macosx import fixb2context

n = input("Input a number: ")
n = int(n)
f1 = 1
f2 = 1
print(f1)
print(f2)

i = 0
while i < n - 2:
    sum = f1 + f2
    f1 = f2
    f2 = sum
    i += 1
    print(sum)

def fib_s(step, arr):
    if step == 0:
        return
    arr.append(arr[-2] + arr[-1])
    fib_s(step - 1, arr)

def fib_l(arr, limit):
    next = arr[-2] + arr[-1]
    if next > limit:
        return
    arr.append(next)
    fib_l(arr, limit)

with open("in.txt") as file1:
    read = file1.read().split()

num = list(map(int, read))
step = num[2]
limit = num[3]
f1, f2 = float(num[0]), float(num[1])

file_arr =[f1, f2]
if step > 2:
    fib_s(step - 2, file_arr)
print("Fibonacci(steps): ", file_arr)
file_arr_l = [f1, f2]
fib_l(file_arr_l, limit)
print("Fibonacci(limit): ", file_arr_l)

with open("out.txt", "w") as file2:
    file2.write("Fibonacci(step): \n\n")
    file2.write(" ".join(map(str, file_arr)) + "\n")

    file2.write("Fibonacci(limit): \n\n")
    file2.write(" ".join(map(str, file_arr_l)) + "\n")





