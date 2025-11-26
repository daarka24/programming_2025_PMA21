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
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            self.count += 1
        except Exception as e:
            print(f"LinkedList add error: {e}")

    def insert(self, data, index):
        try:
            if index < 0 or index > self.count:
                print("Index out of bounds")
                return

            if index == self.count:
                self.add(data)
                return

            new_node = Node(data)

            if index == 0:
                new_node.next = self.head
                if self.head:
                    self.head.prev = new_node
                self.head = new_node
                if self.count == 0:
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

            self.count += 1
        except Exception as e:
            print(f"LinkedList insert error: {e}")

    def remove(self, index):
        try:
            if index < 0 or index >= self.count:
                print("Index out of bounds")
                return

            if index == 0:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            elif index == self.count - 1:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
                else:
                    self.head = None
            else:
                current = self.head
                for _ in range(index):
                    current = current.next

                current.prev.next = current.next
                current.next.prev = current.prev

            self.count -= 1
        except Exception as e:
            print(f"LinkedList remove error: {e}")

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0


if __name__ == "__main__":
    linked_list = LinkedList()

    input_filename = "input.txt"
    output_filename = "output_linked.txt"

    try:
        with open(input_filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    number = int(line)
                    linked_list.add(number)
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")

    try:
        with open(output_filename, "w") as f:
            f.write(f"LinkedList Output (Total Items: {linked_list.count})\n")
            current = linked_list.head
            while current:
                f.write(str(current.data) + "\n")
                current = current.next
        print(f"Done. Saved to {output_filename}")
    except Exception as e:
        print(f"Write error: {e}")