class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, log_file="result.txt"):
        self.head = None
        self.tail = None
        self.size = 0
        self.log_file = log_file
        open(self.log_file, "w").close()
        self.log("Linked list []")

    def log(self, text):
        with open(self.log_file, "a") as f:
            f.write(text + "\n")

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        self.log(f"Added {value} (size = {self.size})")

    def insert(self, index, value):
        if index < 0 or index > self.size:
            self.log("Index out of range")
            return
        if index == self.size:
            self.add(value)
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
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
        self.log(f"Inserted {value} at index {index} (size = {self.size})")

    def remove(self, index):
        if index < 0 or index >= self.size:
            self.log("Index out of range")
            return
        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if self.size == 1:
                self.tail = None
        elif index == self.size - 1:
            removed_value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removed_value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        self.log(f"removed {removed_value} from index {index} (size = {self.size})")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.log("All elements cleared (size = 0)")

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        self.log(f"Elements: {elements} (size = {self.size})\n")


lst = LinkedList()

lst.add(12)
lst.add(7)
lst.add(25)
lst.add(3)
lst.add(18)
lst.print_list()

lst.insert(2, 50)
lst.print_list()

lst.insert(0, 99)
lst.insert(4, 33)
lst.insert(6, 5)
lst.print_list()

lst.remove(3)
lst.print_list()

lst.clear()
lst.print_list()
