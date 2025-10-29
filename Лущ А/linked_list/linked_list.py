from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        print(f"add: Added -> {value}")

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            self.add(value)
            return
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
        self.size += 1
        print(f"insert: Added at index {index} -> {value}")

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        value = current.value
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        self.size -= 1
        print(f"remove: Deleted index {index} -> {value}")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("clear: LinkedList cleared")

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def display_forward(self):
        result = self.to_list()
        print("display_forward:", ", ".join(map(str, result)))
        return result

    def display_backward(self):
        result = []
        current = self.tail
        while current:
            result.append(current.value)
            current = current.prev
        print("display_backward:", ", ".join(map(str, result)))
        return result

    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        print(("get_by_index:", index, current.value))
        return current.value

    def load_from_file(self, filename):

        self.clear()
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                self.add(line.strip())
        print(f"load_from_file: Loaded from {filename}")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            current = self.head
            while current:
                file.write(str(current.value) + "\n")
                current = current.next
        print(f"save_to_file: Saved to {filename}")
