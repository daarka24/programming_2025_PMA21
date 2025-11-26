class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self._size += 1

    def insert(self, index, element):
        new_node = Node(element)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self._size += 1
            return

        if index == self._size:
            self.append(element)
            return

        current = self.head
        for _ in range(index):
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self._size += 1

    def remove_at(self, index):
        current = self.head

        for _ in range(index):
            current = current.next

        value = current.data
        self._remove_node(current)
        return value

    def _remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self._size -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "".join(items)
