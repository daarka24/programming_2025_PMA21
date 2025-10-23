from LinkedList import LinkedList

def load_from_file(filename):
    linkedlist = LinkedList()
    try:
        with open(filename) as f:
            for line in f:
                data = line.strip()
                if data:
                    linkedlist.append(data)
    except:
        print("File not found")
        raise FileNotFoundError
    return linkedlist

methods = {}
file = load_from_file("data.txt")
print("------ List forward ------")
forward = file.display_forward()
methods["display_forward"] = forward
print("------ List backward ------")
back = file.display_back()
methods["display_backward"] = back
try:
    n = (int(input("Index: ")))
    if n < 0:
        raise IndexError("Index out of range")
    print("With index ", n, " - ", file.get_by_index(n - 1))
    methods["get_by_index"] = "With index ", n - 1, file.get_by_index(n - 1)
except IndexError:
    print("Index out of range")
    raise
except ValueError:
    print("Value error")
    raise ValueError
try:
    n = int(input("Delete by index: "))
    file.remove(n-1)
    file.save_to_file("data.txt")
    methods["delete"] = f'Delete by index {n}'
except IndexError:
    print("Index out of range")
try:
    new = str(input("New hero to end: "))
    file.append(new)
    file.save_to_file("data.txt")
    methods["append"] = f'New hero to end {new}'
except Exception as e:
    print("ERROR:", e)
    raise
try:
    new = str(input("New hero to begin: "))
    file.prepend(new)
    file.save_to_file("data.txt")
    methods["prepend"] = f'New hero to begin {new}'
except Exception as e:
    print("ERROR:", e)
    raise
try:
    n = int(input("Add by index: "))
    hero = (str(input("Hero: ")))
    file.insert(n, hero)
    file.save_to_file("data.txt")
    methods["insert"] = f'Add by index {n} - {hero}'
except IndexError:
    print("Index out of range")
print("------ New list forward ------")
new = file.display_forward()
methods["New display_forward"] = new
with open("out.txt", "w") as f:
    for key, item in methods.items():
        f.write(f"{key}: {item}\n")