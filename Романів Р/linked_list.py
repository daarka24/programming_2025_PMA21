class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkedList:
    def __init__(self, iterable=None):
        self.top = None
        self.tail = None

        if iterable:
            for element in iterable:
                self.append(element)

    def __str__(self):
        cur_node = self.top
        result = []
        while cur_node:
            result.append(str(cur_node.data))
            cur_node = cur_node.next
        return '[' + ', '.join(result) + ']'

    def __len__(self):
        count = 0
        cur_node = self.top
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def __iter__(self):
        cur_node = self.top
        while cur_node:
            yield cur_node.data
            cur_node = cur_node.next

    def __getitem__(self, index):
        if not self.top:
            raise IndexError("Index out of range")

        idx = len(self) + index if index < 0 else index

        if idx >= len(self) or idx < 0:
            raise IndexError("Index out of range")

        cur_node = self.top
        for _ in range(idx):
            cur_node = cur_node.next

        return cur_node.data


    def copy(self):
        new_list = LinkedList()
        if self.top is None:
            return new_list

        new_list.top = Node(self.top.data)
        cur_old = self.top.next
        cur_new = new_list.top

        while cur_old:
            new_node = Node(cur_old.data)
            cur_new.next = new_node
            new_node.previous = cur_new

            cur_new = new_node
            cur_old = cur_old.next

        new_list.tail = cur_new

        return new_list


    def insert_at_beginning(self, val):
        new_node = Node(val, next=self.top)

        if self.top:
            self.top.previous = new_node
        else:
            self.tail = new_node

        self.top = new_node


    def append(self, val):
        new_node = Node(val, previous=self.tail)

        if self.tail:
            self.tail.next = new_node
        else:
            self.top = new_node

        self.tail = new_node

    def insert(self, index, val):
        idx = len(self) + 1 + index if index < 0 else index

        if idx <= 0:
            self.insert_at_beginning(val)
            return

        if idx >= len(self):
            self.append(val)
            return

        new_node = Node(val)
        cur_node = self.top
        for _ in range(idx - 1):
            cur_node = cur_node.next

        next_node = cur_node.next

        new_node.previous = cur_node
        new_node.next = next_node

        cur_node.next = new_node
        next_node.previous = new_node


    def pop(self, index=-1):
        if not self.top:
            raise IndexError("The list is empty")

        idx = len(self) + index if index < 0 else index

        if idx >= len(self) or idx < 0:
            raise IndexError("Index out of range")

        if idx == 0:
            val = self.top.data
            self.top = self.top.next
            if self.top:
                self.top.previous = None
            else:
                self.tail = None
            return val

        cur_node = self.top
        for _ in range(idx):
            cur_node = cur_node.next


        cur_node.previous.next = cur_node.next

        if cur_node.next:
            cur_node.next.previous = cur_node.previous
        else:
            self.tail = cur_node.previous

        return cur_node.data


    def remove(self, val):
        cur_node = self.top

        if not cur_node:
            raise ValueError("The list is empty")

        if cur_node.data == val:
            self.pop(0)
            return

        while cur_node:
            if cur_node.data == val:
                break
            cur_node = cur_node.next

        if not cur_node:
            raise ValueError(f"Element {val} does not exist.")

        cur_node.previous.next = cur_node.next

        if cur_node.next:
            cur_node.next.previous = cur_node.previous
        else:
            self.tail = cur_node.previous



if __name__ == "__main__":
    a = LinkedList([1, 2, 3, 4, 5])

    a.pop(4)

    print(a, "last:", a.tail.data)

