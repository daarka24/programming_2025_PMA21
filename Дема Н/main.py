from my_array import ArrayList
import os

def main():
    filename = "in.txt"
    if not os.path.exists(filename):
        print("File doesn't exist")
        return
    list = ArrayList(size=10)
    try:
        with open(filename, "r") as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    list.add(clean_line)
        print("Array added\n")
        print(list)
    except Exception as e:
        print("Something went wrong")
        return
    print("Add by index\n")
    if list.count > 0:
        try:
            i = int(input("Index: "))
            v = str(input("Value: "))
            list.insert(i, v)
            print("Inserted value at index", i, v)
        except ValueError:
            print("Value must be an integer")
            return
        except IndexError as e:
            print("Index out of range")
        except Exception as e:
            print("Something went wrong")
    print("Remove by index\n")
    if list.count > 0:
        try:
            i = int(input("Index: "))
            list.remove(i)
            print("Removed value at index", i, "list:", list)
        except ValueError:
            print("Value must be an integer")
            return
        except IndexError as e:
            print("Index out of range")
        except Exception as e:
            print("Something went wrong")
if __name__ == "__main__":
    main()

