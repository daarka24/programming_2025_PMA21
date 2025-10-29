
with open("data2.txt", "r") as file:
    nums = file.read().split()
    nums = [int(x) for x in nums]


limit = nums[-1]
nums = nums[:-1]


print("Список чисел з файлу:", nums)
print("Ліміт:", limit)



def recursive_fibonacci(arr, limit):

    def recursive(arr, limit):
        next_val = arr[-2] + arr[-1]
        if next_val > limit:
            return arr
        arr.append(next_val)
        return recursive(arr, limit)

    return recursive(arr, limit)

result = recursive_fibonacci(nums, limit)




with open("../output2.txt", "a") as f:
    f.write(" ".join(map(str, result)))


print("Результат записано у output2.txt:", result)
