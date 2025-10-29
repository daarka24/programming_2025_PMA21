file = open("data1.txt", "r")
nums = file.read().split()
nums = [int(x) for x in nums]

file.close()


steps = nums[-1]
nums = nums[:-1]



print("Список чисел з файлу:", nums)
print("Кількість кроків:", steps)


def generate(nums, steps):
    if steps == 0:
        return nums
    next_num = nums[-1] + nums[-2]
    nums.append(next_num)
    return generate(nums, steps - 1)

result = generate(nums, steps)

with open("../output.txt", "a") as f:
    f.write(" ".join(map(str, result)))


print("Результат записано у output.txt")
