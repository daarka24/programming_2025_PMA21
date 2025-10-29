class ArrayList:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.items = [None] * size

    def len(self):
        return self.count

    def expandarray(self):
        newsize = int(self.size * 1.5 + 1)
        newitems = [None] * newsize
        for i in range(self.count):
            newitems[i] = self.items[i]
        self.items = newitems
        self.size = newsize

    def add(self, element):
        try:
            if self.count == self.size:
                self.expandarray()
            self.items[self.count] = element
            self.count += 1
        except Exception as error:
            print("something went wrong with add in ArrayList:", error)

    def retutnbyindex(self, index):
        try:
            print(f"your element is: {self.items[index]}")
        except IndexError:
            print("something wrong with your index in ArrayList")

    def insert(self, element, index):
        try:
            if index < 0 or index > self.count:
                print("index out of range in ArrayList insert")
                return

            if self.count == self.size:
                self.expandarray()

            for i in range(self.count, index, -1):
                self.items[i] = self.items[i - 1]

            self.items[index] = element
            self.count += 1
        except Exception as error:
            print("something went wrong with insert in ArrayList:", error)

    def remove(self, index):
        try:
            if index < 0 or index >= self.count:
                print("index out of range in ArrayList remove")
                return

            for i in range(index, self.count - 1):
                self.items[i] = self.items[i + 1]

            self.items[self.count - 1] = None
            self.count -= 1

        except Exception as error:
            print("something went wrong with remove in ArrayList:", error)

    def clear(self):
        try:
            for i in range(self.count):
                self.items[i] = None
            self.count = 0
        except Exception as error:
            print("something went wrong with clear in ArrayList:", error)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, data):
        try:
            node = Node(data)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.count += 1
        except Exception as error:
            print("something went wrong with add in LinkedList:", error)

    def insert(self, data, index):
        try:
            if index < 0 or index > self.count:
                print("index out of range in LinkedList insert")
                return

            node = Node(data)

            if index == 0:
                node.next = self.head
                if self.head:
                    self.head.prev = node
                self.head = node
                if self.count == 0:
                    self.tail = node
                self.count += 1

            elif index == self.count:
                self.add(data)

            else:
                current = self.head
                for i in range(index):
                    current = current.next
                prev_node = current.prev
                node.prev = prev_node
                node.next = current
                prev_node.next = node
                current.prev = node
                self.count += 1
        except Exception as error:
            print("something went wrong with insert in LinkedList:", error)

    def remove(self, index):
        try:
            if index < 0 or index >= self.count:
                print("index out of range in LinkedList remove")
                return

            if index == 0:
                self.head = self.head.next
                self.count -= 1
                if self.head:
                    self.head.prev = None
                if self.count == 0:
                    self.tail = None

            elif index == self.count - 1:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
                self.count -= 1

            else:
                current = self.head
                for i in range(index):
                    current = current.next
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self.count -= 1
        except Exception as error:
            print("something went wrong with remove in LinkedList:", error)



ArrayListnew = ArrayList(8)
ArrayListnew.add(101)
ArrayListnew.insert(103, 0)
ArrayListnew.insert(105, 0)
ArrayListnew.remove(2)

LinkedListnew = LinkedList()

try:
    with open("starters.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                LinkedListnew.add(number)
            else:
                ArrayListnew.add(number)

except FileNotFoundError:
    print("file not found")

try:
    with open("result.txt", "w") as file:
        try:
            file.write(f"ArrayList (capacity={ArrayListnew.size})\n")
            for i in range(ArrayListnew.len()):
                file.write(str(ArrayListnew.items[i]) + "\n")

            file.write("LinkedList:\n")
            current = LinkedListnew.head
            while current is not None:
                file.write(str(current.data) + "\n")
                current = current.next
        except Exception as error:
            print("something went wrong with results:", error)
except FileNotFoundError:
    print("something went wrong with file")
