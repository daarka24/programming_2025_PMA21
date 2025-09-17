def fibbysteps(nums, steps):
    if len(nums) >= steps:
        return nums[:steps]
    return fibbysteps(nums + [nums[-1] + nums[-2]], steps)

def fibbylimit(nums, limit):
    if len(nums) < 2:
        return nums
    nextval = nums[-1] + nums[-2]
    if nextval > limit:
        return nums
    return fibbylimit(nums + [nextval], limit)

def readfile(filename):
    with open(filename, "r") as f:
        line = f.read().strip().split()
        return list(map(float, line))

def writefile(filename, nums):
    with open(filename, "w") as f:
        for num in nums:
            f.write(str(num) + "\n")

def step():
    data = readfile("text.txt")
    nums = data[:2]
    steps = int(data[2])
    fiblist = fibbysteps(nums, steps)
    writefile("result.txt", fiblist)

def limit():
    data = readfile("limit.txt")
    nums = data[:2]
    limit = data[2]
    fiblist = fibbylimit(nums, limit)
    writefile("limitresult.txt", fiblist)

step()
limit()
