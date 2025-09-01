from abc import ABC, abstractmethod
import os

class Generator(ABC):
    #Name of item to be added
    name: str
    #Id of mod
    mod_name: str

    def __init__(self, name: str, mod_name: str):
        super().__init__()
        self.name = name
        self.mod_name = mod_name

    @abstractmethod
    def generate(self, path: str) -> None:
        pass

    def checkValidPath(path: str) -> bool:
        return os.path.isdir(path)