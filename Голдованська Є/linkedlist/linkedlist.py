class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_node = self.head
        res = []
        while cur_node:
           res.append(cur_node.data)
           cur_node = cur_node.next
        return str(res)

    def __len__(self):
        cur_node = self.head
        res = 0
        while cur_node:
            res += 1
            cur_node = cur_node.next
        return res

    def front(self,value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def back(self, value):
        new_node = Node(value)
        new_node.previous = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def index(self, value, position):

        if len(self) < position or position < 0:
            raise IndexError("індекс виходить за межі списку")

        new_node = Node(value)
        if position == 0:
            self.front(value)
            return

        if len(self) == position:
            self.back(value)
            return

        cur_node = self.head
        for _ in range(position - 1):
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete(self,position):

       if len(self) <= position or position < 0:
           raise IndexError("індекс виходить за межі списку")

       if position == 0:
           self.head = self.head.next
           self.head.previous = None
           return

       if len(self)-1 == position:
           self.tail = self.tail.previous
           self.tail.next = None
           return

       cur_node = self.head
       for _ in range(position):
           cur_node = cur_node.next
       cur_node.previous.next = cur_node.next
       cur_node.next.previous = cur_node.previous


if __name__ == "__main__":

    a = LinkedList()
    a.front(2)
    a.front(1)
    a.back(3)
    try:
        a.index(4,3)
    except IndexError as e:
        print(e)
    print(str(a))
    a.delete(2)
    print(str(a))