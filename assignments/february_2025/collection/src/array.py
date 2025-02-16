class ArrayMethod:
    def __init__(self):
        self.capacity = 3
        self.array = [None] * self.capacity
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def add(self, element) -> None:
        if element is None:
            raise ValueError("Argument cannot be None")
        if self.is_full():
            raise Exception("Array is full")
        self.array[self.size] = element
        self.size += 1

    def is_full(self) -> bool:
        if self.size == self.capacity:
            return True
        return False

    def get(self, index) :
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        return self.array[index]

    def add_at_index(self, index, element):
        if element is None:
            raise ValueError("Argument cannot be None")
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        if self.is_full():
            raise Exception("Array is full")
        self.size += 1
        for i in range(self.size - 1, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element

    def remove(self, element):
        try:
            index = self.array.index(element)
        except ValueError:
            raise Exception("Element not found!")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be between 0 and {self.size - 1}")
        self.array[index] = element

    def contains(self, element):
        return element in self.array[:self.size]

    def clear(self):
        self.size = 0

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Element not found!")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

