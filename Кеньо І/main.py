from array import Arraylist
from linked import Linkedlist, Node


def to_str(data):
    return " ".join(str(item) for item in data)

def write_to_file(filename, data):
    with open(filename, 'a') as file_two:
        file_two.write(to_str(data))
        file_two.write('\n')

def write_message(filename, data):
    with open(filename, 'a') as file_two:
        file_two.write(data)
        file_two.write('\n')

with open("input.txt", 'r') as file_one:
    data=[]

    for line in file_one:
        elements = line.strip().split(' ')
        nums = [int(e) for e in elements if e.strip()]
        data.extend(nums)


arr = Arraylist(data)
link = Linkedlist(data)


write_message("output.txt", "Array way:")
write_message("output.txt", "From file")
write_to_file('output.txt', arr)
print(arr.cap)
write_message("output.txt", "Append 7")
arr.append(7)
print(arr.cap)
write_to_file('output.txt', arr)
write_message("output.txt", "Remove 2")
arr.remove(2)
write_to_file('output.txt', arr)
write_message("output.txt", "insert 5 to 1")
arr.insert(1, 5)
write_to_file('output.txt', arr)
write_message("output.txt", "Remove a nu, at index 3")
arr.rem_index(3)
write_to_file('output.txt', arr)
write_message("output.txt", "Clear")
arr.clear()
write_to_file('output.txt', arr)
print(arr.cap)


write_message("output.txt", "Linked list way:")
write_message("output.txt", "From file")
link.traverse()
write_to_file('output.txt', link)
write_message("output.txt", "Append 7")
link.append_l(7)
write_to_file('output.txt', link)
write_message("output.txt", "Prepend 8")
link.prepend(8)
write_to_file('output.txt', link)
link.remove_l(2)
write_to_file('output.txt', link)
write_message("output.txt", "insert a to 1")
link.insert_l(1, 'a')
write_to_file('output.txt', link)
write_message("output.txt", "Remove a num, at index 3")
link.remove_index(3)
write_to_file('output.txt', link)
write_message("output.txt", "Clear")
link.clear_l()
write_to_file('output.txt', link)
