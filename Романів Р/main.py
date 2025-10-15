from linked_list import LinkedList
import json

if __name__ == "__main__":
    with open("input_list.txt", "r") as file:
        readed = file.read().split()

    arr = []
    try:
        arr = [int(el) for el in readed]
    except ValueError:
        print("invalid data in file")

    #створити список
    linked_list = LinkedList(arr)
    changes = {"list": str(linked_list)}

    linked_list.remove(7)
    changes["remove 7"] = str(linked_list)

    linked_list.insert(6, 3)
    changes["add 3"] = str(linked_list)


    with open("output.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(changes, indent=2))
    print("Зміни записані")
