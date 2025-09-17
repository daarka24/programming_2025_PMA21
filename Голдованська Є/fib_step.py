def fib(step,arr):
    if step < 1:
        return
    arr.append(arr[-2]+arr[-1])
    fib(step-1, arr)

with open("fib_in.txt", "r") as file:
    read = file.read()
    nums = read.split()
    nums = [float(ch) for ch in nums]
    step = nums.pop()

fib(step,nums)

with open("fib_out.txt", "w") as file:
    file.write(str(nums))
