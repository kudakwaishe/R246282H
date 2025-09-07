#R246282H
#Assignment 2
#Question 5

from abc import ABC, abstractmethod

class FileHandler(ABC):

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(filepath='{self.filepath}')"

class TextFileHandler(FileHandler):
    def read(self):
        print(f"Reading text data from: '{self.filepath}'")
        return "This is sample text data."

    def write(self, data):
        print(f"Writing text data to: '{self.filepath}'")
        print(f"Text data '{data}' written successfully.")

class BinaryFileHandler(FileHandler):
    def read(self):
        print(f"Reading binary data from: '{self.filepath}'")
        return b'\x00\x01\x02\x03'

    def write(self, data):
        print(f"Writing binary data to: '{self.filepath}'")
        print(f"Binary data '{data}' written successfully.")


if __name__ == "__main__":
    print("--- Demonstrating TextFileHandler ---")
    text_handler = TextFileHandler('document.txt')
    print(text_handler)
    text_data = text_handler.read()
    text_handler.write("Hello, World!")
    print("-" * 30)

    print("--- Demonstrating BinaryFileHandler ---")
    binary_handler = BinaryFileHandler('image.jpg')
    print(binary_handler)
    binary_data = binary_handler.read()
    binary_handler.write(b'\xde\xad\xbe\xef')
    print("-" * 30)
    try:
         invalid_handler = FileHandler('some_file.dat')
    except TypeError as e:
         print(f"Caught expected error: {e}")
