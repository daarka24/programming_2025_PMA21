def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def fun(limit, arr):
    new_value = arr[-2] + arr[-1]
    if new_value > limit:
        return
    arr.append(new_value)
    fun(limit, arr)
with open("numbers.txt", "r", encoding="utf-8") as file:
    data = file.read().split()
    numbers = list(map(float, filter(is_number, data)))
if len(numbers) < 2:
    raise ValueError("Файл має містити хоча б два числа")
limit = 50
fun(limit, numbers)
output_list = [int(x) if x.is_integer() else x for x in numbers]
with open("result.txt", "a", encoding="utf-8") as file:
    file.write("Результат з лімітом: ")
    file.write(" ".join(map(str, output_list)) + "\n")