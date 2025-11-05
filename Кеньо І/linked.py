class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Linkedlist:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None

        if iterable is not None:

            for item in iterable:
                self.append_l(item)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append_l(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def traverse(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next

    def insert_l(self, index, data):
        new_node = Node(data)

        if index < 0:
            print("Index cannot be negative.")

        if index == 0:
            return self.prepend(data)

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            return "Index out of bounds."

        new_node.next = current.next
        current.next = new_node

    def remove_index(self, index):
        if not self.head:
            print("List is empty")
            return

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        previous_node = None
        current_index = 0
        while current_node and current_index < index:
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

        if not current_node:
            print("Index out of bounds")
            return

        previous_node.next = current_node.next

    def remove_l(self, key):
        temp = self.head


        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def clear_l(self):
        self.head = None

