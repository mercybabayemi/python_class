from abc import abstractmethod, ABC

class Logger(ABC):

    @abstractmethod
    def log(self, message, level):
        ...

    @staticmethod
    def info(message):
        print(message)


class FileLogger(Logger):
    def log(self, message, level):
        print(f'Message: {message} Level: {level}')

class DataBaseLogger(Logger):
    def log(self, message, level):
        print(f'Logging to Database: {message} Level: {level}')