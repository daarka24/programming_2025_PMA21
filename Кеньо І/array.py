

class Arraylist(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cap = len(self)


    def resize(self):

        new_cap = float(len(self) * 1.5) + 1
        self.cap = new_cap

    def append(self, item):
        if len(self) >= self.cap:
            self.resize()
        self=super().append(item)


    def remove(self, item):
        super().remove(item)

    def insert(self, index, item):
        super().insert(index, item)

    def rem_index(self, index):
        super().pop(index)

    def clear(self):
        super().clear()

        self.cap = 0


