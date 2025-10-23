from linkedlist import LinkedList

with open("in.txt") as file:
    data = file.read().split()

data = [float(el) for el in data if el.isdigit()]

linkedlist = LinkedList()
for el in data:
    linkedlist.back(el)

metods = {"og":str(linkedlist)}
# front
linkedlist.front(0)
metods["front"] = str(linkedlist)
# back
linkedlist.back(5)
metods["back"] = str(linkedlist)
# index
try:
    linkedlist.index(6,4)
    metods["index"] = str(linkedlist)
except IndexError as e:
    print(e)
# delete
try:
    linkedlist.delete(1)
    metods["delete"] = str(linkedlist)
except IndexError as e:
    print(e)

with open("out.txt", "w") as file:
    for key,item in metods.items():
        file.write(f"{key}: {item}\n")



