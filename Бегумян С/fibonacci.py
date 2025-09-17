def fibonacci(n, nums):
    if n == 0:
        return nums
    else:
        nums.append(nums[-1] + nums[-2])
        return fibonacci(n - 1, nums)


def fibonacci_range(max_val, nums):
    next_val = nums[-1] + nums[-2]
    if next_val > max_val:
        return [x for x in nums if x <= max_val]
    nums.append(next_val)
    return fibonacci_range(max_val, nums)

with open('start_numbers.txt', 'r') as file:
    start_nums = [float(file.readline().strip()) for _ in range(2)]

with open('step.txt', 'r') as file:
    steps, max_val = [float(file.readline().strip()) for _ in range(2)]

if steps <= 0:
    raise ValueError("Number of steps should be bigger than 0")
if max_val <= 0:
    raise ValueError("Number of maximum should be bigger than 0")


with open('result.txt', 'w') as file:
    file.write(' '.join([str(num) for num in fibonacci(int(steps), start_nums[:])]))

with open('range.txt', 'w') as file:
    file.write(' '.join([str(num) for num in fibonacci_range(max_val, start_nums[:])]))





