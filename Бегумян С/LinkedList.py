class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.add_to_file("linked list []")

    def add_to_file(self, text):
        with open("list.txt", "a") as f:
            f.write(text + "\n")

    def add(self, value):
        if not isinstance(value, (int, float)):
            self.add_to_file("Value should be a number")
            return

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        self.add_to_file("Added " + str(value) + " (size = " + str(self.size) + ")")

    def insert(self, index, value):
        if not isinstance(value, (int, float)):
            self.add_to_file("Value should be a number")
            return

        if index < 0 or index > self.size:
            self.add_to_file("Index out of range")
            return

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.add(value)
            return
        else:
            current = self.head
            for i in range(index):
                current = current.next
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
        self.size += 1
        self.add_to_file("Inserted " + str(value) + " at index " + str(index) + " (size = " + str(self.size) + ")")

    def remove(self, index):
        if index < 0 or index >= self.size:
            self.add_to_file("Index out of range")
            return

        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            if self.size == 1:
                self.tail = None
        elif index == self.size - 1:
            removed_value = self.tail.value
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            current = self.head
            for i in range(index):
                current = current.next
            removed_value = current.value
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node

        self.size -= 1
        self.add_to_file("removed " + str(removed_value) + " from index " + str(index) + " (size = " + str(self.size) + ")")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.add_to_file("All elements cleared ((size = 0)")

    def print_list(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.value)
            current = current.next
        self.add_to_file("Elements: " + str(elements) + " (size = " + str(self.size) + ")\n")

open("list.txt", "w").close()

lst = LinkedList()
lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.add(5)
lst.add(6)
lst.add(7)
lst.add(8)
lst.print_list()

lst.insert(1, 15)
lst.print_list()

lst.insert(7, 11)
lst.insert(5, 66)
lst.insert(0, 9)
lst.print_list()

lst.remove(4)
lst.print_list()

lst.clear()
lst.print_list()
