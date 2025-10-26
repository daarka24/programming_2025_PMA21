class ArrayList:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity
    def resize(self):
        new_capacity = int(self.capacity * 1.5) + 1
        new_array = [None] * new_capacity
        for index in range(self.size):
            new_array[index] = self.array[index]
        self.array = new_array
        self.capacity = new_capacity
    def append(self, element):
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = element
        self.size += 1
    def insert(self, position, element):
        if position < 0 or position > self.size:
            print("Position out of bounds")
            return
        if self.size >= self.capacity:
            self.resize()
        for index in range(self.size, position, -1):
            self.array[index] = self.array[index - 1]
        self.array[position] = element
        self.size += 1
    def remove(self, position):
        if position < 0 or position >= self.size:
            print("Position out of bounds")
            return
        for index in range(position, self.size - 1):
            self.array[index] = self.array[index + 1]
        self.array[self.size - 1] = None
        self.size -= 1
    def remove_all(self):
        self.array = [None] * self.capacity
        self.size = 0
    def print_list(self):
        print(" ".join(str(self.array[index]) for index in range(self.size)),end="\n")
        print("Capacity:"+ f'{self.capacity}')
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                numbers = file.read().split()
                for number in numbers:
                    self.append(int(number))
        except:
            print(f"File {filename} not found. Empty list created.")
    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for index in range(self.size):
                file.write(str(self.array[index]) + " ")
def menu_arraylist_file(array_list, filename):
    array_list.load_from_file(filename)
    while True:
        print("""
1. Insert at position
2. Remove from position
3. Remove all elements
4. Print ArrayList
5. Append to end
0. Exit program""")
        try:
            user_choice = int(input("Make a choice: "))
        except:
            print("Choice must be an integer, try again")
            continue
        if user_choice == 0:
            array_list.save_to_file(filename)
            print(f"Data saved to file '{filename}'. Program terminated.")
            break
        elif user_choice == 1:
            insert_position = int(input("Enter index: "))
            insert_data = int(input("Enter data: "))
            array_list.insert(insert_position, insert_data)
            array_list.print_list()
            array_list.save_to_file(filename)
        elif user_choice == 2:
            remove_position = int(input("Enter index: "))
            array_list.remove(remove_position)
            array_list.print_list()
            array_list.save_to_file(filename)
        elif user_choice == 3:
            array_list.remove_all()
            array_list.print_list()
            array_list.save_to_file(filename)
        elif user_choice == 4:
            array_list.print_list()
        elif user_choice == 5:
            append_data = int(input("Enter data: "))
            array_list.append(append_data)
            array_list.print_list()
            array_list.save_to_file(filename)
        else:
            print("Choice out of range, try again")
filename = "array_list_data.txt"
array_list_instance = ArrayList()
menu_arraylist_file(array_list_instance, filename)