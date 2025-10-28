from array_list import ArrayList
import json

if __name__ == "__main__":
    with open("input_arraylist.txt", "r") as file:
        readed = file.read().split()

    arr = []
    try:
        arr = [int(el) for el in readed]
    except ValueError:
        print("invalid data in file")

    array_list = ArrayList(arr)
    changes = dict()
    changes["list"] = str(array_list)

    array_list.remove(7)
    changes["remove 7"] = str(array_list)

    array_list.insert(6, 3)
    changes["add 3"] = str(array_list)
    changes["starting list"] = {"list": str(array_list),"size:": array_list.size,"capacity:": array_list.capacity}

    for i in range(100, 105):
        array_list.append(i)
    changes["eq size and capacity"] = {"list": str(array_list), "size:":array_list.size, "capacity:": array_list.capacity}
    array_list.append(1)
    changes["new capacity"] = {"list": str(array_list), "size:": array_list.size, "capacity:": array_list.capacity}

    with open("output_arraylist.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(changes, indent=2))
    print("Зміни записані")