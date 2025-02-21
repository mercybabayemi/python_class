class ArrayListMethod:
    def __init__(self):
        self.capacity = 3
        self.array = [None] * self.capacity
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def add(self, item):
        if item is None:
            raise ValueError("Argument cannot be null")
        if self.is_full():
            self._increase_capacity()
        self.array[self.size] = item
        self.size += 1

    def _increase_capacity(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.capacity):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def is_full(self):
        return self.size == self.capacity

    def add_at_index(self, index, item):
        if item is None:
            raise ValueError("Argument cannot be null")
        if index < 0 or index > self.size:
            raise IndexError(f"Index must be between 0 and {self.size}")
        if self.is_full():
            self._increase_capacity()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.size += 1

    def remove(self, item):
        index = -1
        for i in range(self.size):
            if self.array[i] == item:
                index = i
                break
        if index == -1:
            raise ValueError("Element not found!")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        return self.array[index]

    def set(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        self.array[index] = item

    def contains(self, item):
        return item in self.array[:self.size]

    def clear(self):
        self.size = 0

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def remove_all(self):
        self.size = 0
        self.array = [None] * self.capacity