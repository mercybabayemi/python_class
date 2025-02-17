class StackMethod:
    def __init__(self):
        self.array_list = []

    def size(self):
        return len(self.array_list)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.array_list.append(item)

    def pop(self):
        if self.size() == 0:
            raise IndexError("pop from empty stack")
        return self.array_list.pop()

    def peek(self):
        if self.size() == 0:
            raise IndexError("peek from empty stack")
        return self.array_list[-1]

    def search(self, item):
        try:
            return self.size() - self.array_list.index(item)
        except ValueError:
            return -1