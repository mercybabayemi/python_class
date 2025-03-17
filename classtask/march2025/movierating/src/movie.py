from datetime import datetime


class Movie:
    def __init__(self, title):
        self.name = title
        self.date = datetime.now().date()
        self.time = datetime.now().time()

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value
    #
    # def __str__(self):
    #     return f'{self.name} {self.date} {self.time}'