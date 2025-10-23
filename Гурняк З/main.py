class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def _normalize_index(self, index, allow_end=False):
        if index < 0:
            index += self._size
        upper = self._size if allow_end else self._size - 1
        if index < 0 or index > upper:
            raise IndexError("index out of range")
        return index

    def _node_at(self, index):
        index = self._normalize_index(index, allow_end=False)
        if index <= self._size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self._size - 1, index, -1):
                cur = cur.prev
        return cur

    def _unlink(self, node):
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        else:
            self.head = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        self._size -= 1
        return node.value

    def append(self, value):
        new = Node(value, prev=self.tail, next=None)
        if self.tail:
            self.tail.next = new
        else:
            self.head = new
        self.tail = new
        self._size += 1

    def insert(self, index, value):
        index = self._normalize_index(index, allow_end=True)
        if index == self._size:
            self.append(value)
            return
        if index == 0:
            new = Node(value, prev=None, next=self.head)
            if self.head:
                self.head.prev = new
            else:
                self.tail = new
            self.head = new
            self._size += 1
            return
        succ = self._node_at(index)
        pred = succ.prev
        new = Node(value, prev=pred, next=succ)
        if pred:
            pred.next = new
        else:
            self.head = new
        succ.prev = new
        self._size += 1

    def remove(self, value):
        cur = self.head
        while cur and cur.value != value:
            cur = cur.next
        if cur is None:
            raise ValueError("value not found")
        self._unlink(cur)

    def clear(self):
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            cur = nxt
        self.head = None
        self.tail = None
        self._size = 0

if __name__ == "main":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert(1, 1.5)
    print([node.value for node in (ll._node_at(i) for i in range(ll._size))])
    ll.remove(1.5)
    print([node.value for node in (ll._node_at(i) for i in range(ll._size))])
    ll.clear()
    print(ll._size)