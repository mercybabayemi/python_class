class QueueMethod:
    def __init__(self):
        self.array = []  # This will simulate an ArrayMethod
        self.head = 0
        self.size = 0

    def is_empty(self):
        return len(self.array) == 0

    def offer(self, element):
        if len(self.array) < 3:  # Assuming size of queue is 3 (like the Java example)
            self.array.insert(self.size, element)
            self.size += 1
            return True
        return False

    def add(self, element):
        if element is None:
            raise ValueError("Element is null")
        if len(self.array) < 3:
            self.array.insert(self.size, element)
            self.size += 1
            return True
        else:
            raise OverflowError("Queue is full")

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.head]

    def poll(self):
        if self.is_empty():
            return None
        self.size -= 1
        return self.array.pop(self.head)


    def remove(self):
        return self.poll()

    def element(self):
        return self.peek()

    def __len__(self):
        return self.size