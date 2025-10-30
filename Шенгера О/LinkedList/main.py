class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_data(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node       # -> determinate next link
            new_node.previous = self.tail   # -> determinate previous link
            self.tail = new_node            # -> set next value

    def remove_end(self):
        if self.head is None:
            raise ValueError("list is empty")

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.previous
        self.tail.next = None

    def show_list(self):
        current_element = self.head
        print("linked_list: ", end="")
        while current_element:
            print(current_element.data, end=" <-> ")
            current_element = current_element.next
        print("end")

    def list_getter(self):
        if self.head is None:
            raise ValueError("linkedlist is empty.")

        linkedlist = []
        current_element = self.head
        while current_element:
            linkedlist.append(current_element.data)
            current_element = current_element.next

        return linkedlist

    def insert_by_idx(self, idx, data):

        new_node = Node(data)

        if idx < 0:
            raise IndexError("index cannot be negative")

        if idx == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
            return

        current = self.head
        current_index = 0

        while current and current_index < idx - 1:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("index out of range")

        if current.next is None:
            current.next = new_node
            new_node.previous = current
            self.tail = new_node
        else:
            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node

    def remove_by_idx(self, idx):
        if self.head is None:
            raise ValueError("list is empty")

        if idx < 0:
            raise IndexError("index cannot be negative")

        if idx == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return

        current = self.head
        current_index = 0

        while current and current_index < idx:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("index out of range")

        if current == self.tail:
            self.tail = current.previous
            self.tail.next = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

def read_file(file):
    with open(file, "r") as r:
        line = r.readline().strip()

    if not line:
        raise IndexError("error: file is empty.")

    data = [d for d in line.split(",")]
    print(f"parsed numbers: {data}")
    return data

def distribute_data(data,  linkedlist):
    for i in data:
        linkedlist.add_data(i)


def write_file(file, linkedlist):
    with open(file, "a") as a:
        try:
            a.write("linked_list: " + str(linkedlist.list_getter()) + "\n")
        except ValueError as v:
            print(f"error: {v}")
            exit(1)

if __name__=="__main__":
    try:
        data = read_file("data.txt")
    except ValueError as e:
        print(f"error: {e}.")
        exit(1)
    except IndexError:
        print("error: file is empty.")
        exit(1)

    linked_list = LinkedList()

    distribute_data(data, linked_list)

    linked_list.remove_end() # end
    linked_list.remove_by_idx(0) # first
    linked_list.remove_by_idx(3)
    linked_list.insert_by_idx(0, "hello")

    linked_list.show_list()

    write_file("data_result.txt", linked_list)