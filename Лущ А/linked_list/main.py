from linked_list import LinkedList

INPUT_FILE = "input_data.txt"
OUTPUT_FILE = "output_data.txt"

if __name__ == "__main__":
    ll = LinkedList()

    ll.load_from_file(INPUT_FILE)

    ll.display_forward()
    ll.display_backward()

    ll.get_by_index(2)
    ll.remove(3)
    ll.add("New element to end")
    ll.insert(0, "New element to begin")
    ll.insert(3, "Inserted at index 3")

    ll.display_forward()

    ll.save_to_file(OUTPUT_FILE)
