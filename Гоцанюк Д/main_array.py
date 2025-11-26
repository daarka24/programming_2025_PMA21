class ArrayList:
    def __init__(self, init_size=10):
        self.capacity = init_size
        self.length = 0
        self.array_buffer = [None] * init_size

    def _expand_capacity(self):
        new_capacity = int(self.capacity * 1.5 + 1)
        new_buffer = [None] * new_capacity

        for i in range(self.length):
            new_buffer[i] = self.array_buffer[i]

        self.array_buffer = new_buffer
        self.capacity = new_capacity

    def add(self, element):
        try:
            if self.length == self.capacity:
                self._expand_capacity()

            self.array_buffer[self.length] = element
            self.length += 1
        except Exception as e:
            print(f"Error in add: {e}")

    def insert(self, element, index):
        try:
            if index < 0 or index > self.length:
                print("Error: Index out of range")
                return

            if self.length == self.capacity:
                self._expand_capacity()

            for i in range(self.length, index, -1):
                self.array_buffer[i] = self.array_buffer[i - 1]

            self.array_buffer[index] = element
            self.length += 1
        except Exception as e:
            print(f"Error in insert: {e}")

    def remove(self, index):
        try:
            if index < 0 or index >= self.length:
                print("Error: Index out of range")
                return

            for i in range(index, self.length - 1):
                self.array_buffer[i] = self.array_buffer[i + 1]

            self.array_buffer[self.length - 1] = None
            self.length -= 1
        except Exception as e:
            print(f"Error in remove: {e}")

    def clear(self):
        self.array_buffer = [None] * self.capacity
        self.length = 0

    def get_element(self, index):
        if 0 <= index < self.length:
            return self.array_buffer[index]
        return None


if __name__ == "__main__":
    my_list = ArrayList(8)

    my_list.add(101)
    my_list.insert(103, 0)
    my_list.insert(105, 0)
    my_list.remove(2)

    input_filename = "input.txt"
    output_filename = "output_array.txt"

    try:
        with open(input_filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    num = int(line)
                    my_list.add(num)
    except FileNotFoundError:
        print(f"File {input_filename} not found.")

    try:
        with open(output_filename, "w") as f:
            f.write(f"ArrayList (Final Capacity={my_list.capacity})\n")
            f.write("Elements:\n")
            for i in range(my_list.length):
                f.write(str(my_list.get_element(i)) + "\n")
        print(f"Done. Saved to {output_filename}")
    except Exception as e:
        print(f"Write error: {e}")