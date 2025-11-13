from array_list import ArrayList


def main():
    arr = ArrayList()
    while True:
        print("\nMenu:")
        print("1. Append element")
        print("2. Insert element at index")
        print("3. Remove element at index")
        print("4. Clear list")
        print("5. Show list")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            value = input("Enter value to append: ")
            arr.append(value)
        elif choice == "2":
            index = int(input("Enter index: "))
            value = input("Enter value: ")
            try:
                arr.insert(index, value)
            except IndexError as e:
                print(e)
        elif choice == "3":
            index = int(input("Enter index to remove: "))
            try:
                arr.remove(index)
            except IndexError as e:
                print(e)
        elif choice == "4":
            arr.clear()
            print("List cleared.")
        elif choice == "5":
            print(arr)
        elif choice == "6":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
