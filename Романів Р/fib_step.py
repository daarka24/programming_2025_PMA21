def is_number(ch):
    try:
        float(ch)
        return True
    except:
        return False


def is_int(n):
    return n % 1 == 0


def fib(step, arr):
    if step == 0:
        return

    arr.append(array[-2] + array[-1])

    fib(step - 1, arr)


with open("input_step.txt", "r") as file:
    readed = file.read()
    array, steps = readed.split("\n")

array = array.split()
array = [float(el) for el in array if is_number(el)]
steps = int(steps)

fib(steps, array)

output_list = []

for el in array:
    if is_int(el):
        output_list.append(int(el))
    else:
        output_list.append(el)

with open("output_step.txt", "w") as file:
    file.write(str(output_list))