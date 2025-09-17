def fib_recursive_step(nums, a):
    if a==0:
        return nums
    else:
        nums.append(nums[-1]+nums[-2])
        a-=1
        return fib_recursive_step(nums, a)

def fib_recursive_limit(arr, l):
    if arr[-1]>l:
        return arr[:-1]
    else:
        arr.append(arr[-1]+arr[-2])
        return fib_recursive_limit(arr, l)

file_one=open("nums.txt")
nums=file_one.read()

nums = nums.split(',')
nums = [float(n) for n in nums]

file_two=open("step.txt")
a=file_two.read()
a=float(a)


result = fib_recursive_step(nums, a)
r = " ".join(str(item) for item in result)
print(r)

with open("result.txt", 'w') as file_three:
    file_three.write(r)



file_four=open('limit.txt')
l=file_four.read()
l=float(l)
arr=[0, 1]
result_two = fib_recursive_limit(arr, l)
result_two = [float(n) for n in result_two]
r2 = " ".join(str(item) for item in result_two)
print(r2)
with open("result.txt", 'a') as file_five:
    file_five.write('\n')
    file_five.write(r2)
