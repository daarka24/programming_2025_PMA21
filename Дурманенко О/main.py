class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.list_size = 0

    def __len__(self):
        return self.list_size

    def __str__(self):
        if self.list_size == 0:
            return "LinkedList([])"
        list_elements = []
        current_node = self.head_node
        while current_node:
            list_elements.append(str(current_node.data))
            current_node = current_node.next_node
        return f"LinkedList([{', '.join(list_elements)}])"

    def append(self, data):
        try:
            new_node = Node(data)
            if self.list_size == 0:
                self.head_node = new_node
                self.tail_node = new_node
            else:
                new_node.previous_node = self.tail_node
                self.tail_node.next_node = new_node
                self.tail_node = new_node
            self.list_size += 1
            return True
        except:
            print(f"Error adding element")
            return False

    def insert(self, index, data):
        try:
            if index < 0 or index > self.list_size:
                print(f"Invalid index: {index}")
                return False
            if index == self.list_size:
                return self.append(data)
            if index == 0:
                new_node = Node(data)
                new_node.next_node = self.head_node
                self.head_node.previous_node = new_node
                self.head_node = new_node
                self.list_size += 1
                return True
            new_node = Node(data)
            current_node = self._get_node_at_index(index)
            new_node.previous_node = current_node.previous_node
            new_node.next_node = current_node
            current_node.previous_node.next_node = new_node
            current_node.previous_node = new_node
            self.list_size += 1
            return True
        except:
            print(f"Error inserting element")
            return False

    def remove_at(self, index):
        try:
            if self.list_size == 0:
                print("List is empty")
                return None
            if index < 0 or index >= self.list_size:
                print(f"Invalid index: {index}")
                return None
            node_to_remove = self._get_node_at_index(index)
            removed_data = node_to_remove.data
            if self.list_size == 1:
                self.head_node = None
                self.tail_node = None
            elif node_to_remove == self.head_node:
                self.head_node = node_to_remove.next_node
                self.head_node.previous_node = None
            elif node_to_remove == self.tail_node:
                self.tail_node = node_to_remove.previous_node
                self.tail_node.next_node = None
            else:
                node_to_remove.previous_node.next_node = node_to_remove.next_node
                node_to_remove.next_node.previous_node = node_to_remove.previous_node
            self.list_size -= 1
            return removed_data
        except:
            print(f"Error removing element")
            return None

    def clear(self):
        try:
            self.head_node = None
            self.tail_node = None
            self.list_size = 0
            return True
        except:
            print(f"Error clearing list")
            return False

    def get(self, index):
        try:
            if index < 0 or index >= self.list_size:
                print(f"Invalid index: {index}")
                return None
            target_node = self._get_node_at_index(index)
            return target_node.data
        except:
            print(f"Error getting element")
            return None

    def _get_node_at_index(self, index):
        if index < self.list_size // 2:
            current_node = self.head_node
            for i in range(index):
                current_node = current_node.next_node
        else:
            current_node = self.tail_node
            for i in range(self.list_size - 1 - index):
                current_node = current_node.previous_node
        return current_node

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                current_node = self.head_node
                while current_node:
                    file.write(f"{current_node.data}\n")
                    current_node = current_node.next_node
            print(f"List successfully saved to file '{filename}'")
            return True
        except IOError:
            print(f"Error saving to file")
            return False
        except:
            print(f"Unexpected error")
            return False

    def load_from_file(self, filename):
        try:
            self.clear()
            with open(filename, 'r') as file:
                lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    try:
                        data = int(line)
                    except ValueError:
                        try:
                            data = float(line)
                        except ValueError:
                            data = line
                    self.append(data)
            print(f"List successfully loaded from file '{filename}'")
            return True
        except FileNotFoundError:
            print(f"File '{filename}' not found")
            return False
        except IOError:
            print(f"Error reading file")
            return False
        except:
            print(f"Unexpected error")
            return False


def print_menu():
    print("\nLinkedList - OPERATIONS MENU")
    print("1. Add element to the end")
    print("2. Insert element at index")
    print("3. Remove element at index")
    print("4. Get element at index")
    print("5. Clear list")
    print("6. Show list")
    print("7. List size")
    print("8. Save to file")
    print("9. Load from file")
    print("0. Exit")


linked_list = LinkedList()
while True:
    print_menu()
    try:
        choice = int(input("Select option: "))
    except ValueError:
        print("Error: enter a number!")
        continue

    if choice == 1:
        data = input("Enter value to add: ")
        try:
            data = int(data)
        except ValueError:
            try:
                data = float(data)
            except ValueError:
                pass
        if linked_list.append(data):
            print(f"Element '{data}' successfully added")

    elif choice == 2:
        try:
            index = int(input("Enter index: "))
            data = input("Enter value: ")
            try:
                data = int(data)
            except ValueError:
                try:
                    data = float(data)
                except ValueError:
                    pass
            if linked_list.insert(index, data):
                print(f"Element '{data}' inserted at position {index}")
        except ValueError:
            print("Error: invalid index!")

    elif choice == 3:
        try:
            index = int(input("Enter index to remove: "))
            removed = linked_list.remove_at(index)
            if removed is not None:
                print(f"Removed element '{removed}' from position {index}")
        except ValueError:
            print("Error: invalid index!")

    elif choice == 4:
        try:
            index = int(input("Enter index: "))
            element = linked_list.get(index)
            if element is not None:
                print(f"Element at position {index}: {element}")
        except ValueError:
            print("Error: invalid index!")

    elif choice == 5:
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            if linked_list.clear():
                print("List cleared")
        else:
            print("Operation cancelled")

    elif choice == 6:
        print(linked_list)

    elif choice == 7:
        print(f"List size: {len(linked_list)}")

    elif choice == 8:
        filename = input("Enter filename: ")
        linked_list.save_to_file(filename)

    elif choice == 9:
        filename = input("Enter filename: ")
        linked_list.load_from_file(filename)

    elif choice == 0:
        print("Exiting program...")
        break

    else:
        print("Invalid option! Please select 0-9")