def fun(steps, arr):
    if steps == 0:
        return
    arr.append(arr[-1] + arr[-2])
    fun(steps - 1, arr)
with open("numbers.txt", "r", encoding="utf-8") as file:
    read = file.read()
    numbers = list(map(float, filter(lambda x: x.replace('.', '', 1).replace('-', '', 1).isdigit(), read.split())))
if len(numbers) < 2:
    raise ValueError("Файл має містити хоча б два числа")
with open("step.txt", "r", encoding="utf-8") as file:
    step = int(file.read().strip())
fun(step, numbers)
output_list = [int(x) if x % 1 == 0 else x for x in numbers]
with open("result.txt", "a", encoding="utf-8") as file:
    file.write("Результат зі step.txt: ")
    file.write(" ".join(map(str, output_list)) + "\n")

