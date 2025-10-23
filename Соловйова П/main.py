class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        elements = []
        current = self.start
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"LinkedList([{', '.join(elements)}])"

    def add(self, value):
        try:
            node = Node(value)
            if self.count == 0:
                self.start = self.end = node
            else:
                node.prev = self.end
                self.end.next = node
                self.end = node
            self.count += 1
            return True
        except Exception:
            print("Failed to add element")
            return False

    def insert_at(self, pos, value):
        try:
            if pos < 0 or pos > self.count:
                print("Invalid position")
                return False
            if pos == self.count:
                return self.add(value)
            node = Node(value)
            if pos == 0:
                node.next = self.start
                self.start.prev = node
                self.start = node
            else:
                current = self._get_node(pos)
                node.prev = current.prev
                node.next = current
                current.prev.next = node
                current.prev = node
            self.count += 1
            return True
        except Exception:
            print("Insertion error")
            return False

    def remove(self, pos):
        try:
            if self.count == 0:
                print("List is empty")
                return None
            if pos < 0 or pos >= self.count:
                print("Invalid position")
                return None
            target = self._get_node(pos)
            data = target.value
            if self.count == 1:
                self.start = self.end = None
            elif target == self.start:
                self.start = target.next
                self.start.prev = None
            elif target == self.end:
                self.end = target.prev
                self.end.next = None
            else:
                target.prev.next = target.next
                target.next.prev = target.prev
            self.count -= 1
            return data
        except Exception:
            print("Removal error")
            return None

    def clear_all(self):
        self.start = self.end = None
        self.count = 0
        return True

    def get_value(self, pos):
        try:
            if pos < 0 or pos >= self.count:
                print("Invalid position")
                return None
            return self._get_node(pos).value
        except Exception:
            print("Retrieval error")
            return None

    def _get_node(self, pos):
        if pos < self.count // 2:
            current = self.start
            for _ in range(pos):
                current = current.next
        else:
            current = self.end
            for _ in range(self.count - 1, pos, -1):
                current = current.prev
        return current

    def export(self, path):
        try:
            with open(path, 'w') as f:
                current = self.start
                while current:
                    f.write(f"{current.value}\n")
                    current = current.next
            print(f"Saved to '{path}'")
            return True
        except Exception:
            print("Save error")
            return False

    def import_data(self, path):
        try:
            self.clear_all()
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            val = int(line)
                        except ValueError:
                            try:val = float(line)
                            except ValueError:
                                val = line
                        self.add(val)
            print(f"Loaded from '{path}'")
            return True
        except FileNotFoundError:
            print("File not found")
            return False
        except Exception:
            print("Load error")
            return False


linked = LinkedList()

print("Adding elements...")
linked.add(10)
linked.add(20)
linked.add(30)
linked.add(8)
linked.add(60)
linked.add(3)
linked.add(2)
linked.add(32)
print(linked)

print("Inserting element 15 at position 1...")
linked.insert_at(1, 15)
print(linked)
print("Inserting element 8 at position 2...")
linked.insert_at(2, 8)
print(linked)
print("Inserting element 14 at position 4...")
linked.insert_at(4, 14)
print(linked)
print("Value at index 2:", linked.get_value(2))

print("Removing element at index 1...")
removed = linked.remove(1)
print("Removed:", removed)
print(linked)

print("Current size:", len(linked))

print("Exporting list to file...")
linked.export("linkedlist.txt")

print("Clearing list...")
linked.clear_all()
print(linked)

print("Importing list from file...")
linked.import_data("linkedlist.txt")
print(linked)