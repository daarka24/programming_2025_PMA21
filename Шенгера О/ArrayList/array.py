# -> array methods (add[idx], add[end], remove[idx], remove[end], clear_array)

class ArrayList:
    def __init__(self):
        self.array = []
        self.curr_size = len(self.array)
        self.max_size = 1

    def update_size(self):
        self.max_size = len(self.array) * 1.5 + 1
        print(f"current max size of an array: {self.max_size}, current size: {self.curr_size}")

    def show_curr_size(self):
        print(f"current size: {self.curr_size}")
    def is_place(self):
        return len(self.array) < self.max_size

    def add_end(self, data):
        if not self.is_place():
            self.update_size()
        self.array.append(data)
        self.curr_size = len(self.array)

    def add_idx(self, data, idx):
        if not self.is_place():
            self.update_size()

        new_array = []

        for i in range(self.curr_size):
            if i == idx:
                new_array.append(data)
            else:
                new_array.append(self.array[i])
        self.array.clear()
        self.array = new_array

        self.curr_size = len(self.array)

    def remove_end(self):
        if not self.array:
            raise ValueError("array is empty.")
        self.array.pop(-1)
        self.curr_size = len(self.array)
    def remove_idx(self, idx):
        if not self.array:
            raise ValueError("array is empty.")

        new_array = []

        for i in range(self.curr_size):
            if i == idx:
                continue
            new_array.append(self.array[i])

        self.array.clear()
        self.array = new_array
        self.curr_size = len(self.array)

    def clear_array(self):
        self.array.clear()
        self.curr_size = len(self.array)

    def get_array(self):
        if not self.array:
            raise ValueError("array is empty.")
        return self.array

    def show_array(self):
        print(self.array)

def read_file(file):
    with open(file, "r") as r:
        line = r.readline().strip()

    if not line:
        raise IndexError("error: file is empty.")

    data = [d for d in line.split(",")]
    print(f"parsed numbers: {data}")
    return data

def distribute_data(data, array):
    for n, i in enumerate(data):
        array.add_end(data[n])

def write_file(file, data):
    with open(file, "a") as a:
        a.write(f"array: {data}\n")

if __name__=="__main__":
    try:
        data = read_file("../LinkedList/data.txt")
    except ValueError as e:
        print(f"error: {e}.")
        exit(1)
    except IndexError:
        print("error: file is empty.")
        exit(1)

    my_array = ArrayList()

    distribute_data(data, my_array)

    my_array.show_array()

    my_array.remove_end() # remove 20

    my_array.remove_idx(0) # remove 1

    my_array.remove_idx(8)
    my_array.show_array()
    my_array.show_curr_size()

    array_data = my_array.get_array()

    write_file("../data_result.txt", array_data)