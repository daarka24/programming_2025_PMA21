from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display_forward(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        output = ", ".join(values)
        print(output)
        return output
    def display_back(self):
        current = self.tail
        values = []
        while current:
            values.append(str(current.data))
            current = current.prev
        output = ", ".join(values)
        print(output)
        return output
    def get_by_index(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1
        raise IndexError("Index out of range")
    def insert(self, index, data):
        new_node = Node(data)
        if index <= 0 or not self.head:
            self.prepend(data)
            return
        current = self.head
        current_index = 0

        while current.next and current_index < index - 1:
            current = current.next
            current_index += 1
        if not current_index:
            self.append(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
    def remove(self, index):
        if not self.head:
            raise IndexError("Index out of range")
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        current_index = 0
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        while current and current_index < index:
            current = current.next
            current_index += 1
        if not current:
            raise IndexError("Index out of range")
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            current = self.head
            while current:
                f.write(str(current.data) + "\n")
                current = current.next
