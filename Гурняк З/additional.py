class ArrayList:
    def __init__(self, initial=None):
        if initial is None:
            self._capacity = 4
            self._data = [None] * self._capacity
            self._size = 0
        else:
            self._size = len(initial)
            self._capacity = max(4, self._size)
            self._data = list(initial) + [None] * (self._capacity - self._size)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size >= self._capacity:
            new_capacity = int(1.5 * self._capacity) + 1
            self._resize(new_capacity)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size >= self._capacity:
            new_capacity = int(1.5 * self._capacity) + 1
            self._resize(new_capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1

    def clear(self):
        self._data = [None] * self._capacity
        self._size = 0

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._data[index] = value

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"ArrayList({[self._data[i] for i in range(self._size)]})"

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