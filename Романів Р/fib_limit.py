def is_number(ch):
    try:
        float(ch)
        return True
    except:
        return False


def is_int(n):
    return n % 1 == 0


def fib(lim, arr):
    next = arr[-2] + arr[-1]

    if lim < next:
        return

    arr.append(next)

    fib(lim, arr)


with open("input_limit.txt", "r") as file:
    readed = file.read()
    array, limit = readed.split("\n")

array = array.split()
array = [float(el) for el in array if is_number(el)]
limit = float(limit)

fib(limit, array)

output_list = []

for el in array:
    if is_int(el):
        output_list.append(int(el))
    else:
        output_list.append(el)

with open("output_limit.txt", "w") as file:
    file.write(str(output_list))