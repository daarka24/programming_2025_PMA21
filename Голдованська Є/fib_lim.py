def fib(lim,arr):
    if (arr[-2]+arr[-1])>lim:
        return
    arr.append(arr[-2]+arr[-1])
    fib(lim, arr)

with open("fib_in.txt", "r") as file:
    read = file.read()
    nums = read.split()
    nums = [float(ch) for ch in nums]
    lim = nums.pop()

fib(lim,nums)

with open("fib_out.txt", "w") as file:
    file.write(str(nums))