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
    
    def outputFile(self, path: str):
        try:
            fileName = path + self.name + ".json"
            data = self._createString()
            if(data is None):
                print("Skipped generating " + fileName)
            else:
                with open(fileName, "x") as file:
                    file.write(data)  
                
        except OSError:
            print("Failed to create and open file. Make sure a file called " + (self.name + ".json") + " does not already exist")

    @abstractmethod
    def _createString() -> str | None:
        """
        Creates the string to be written to the generated file.

        Returns:
            string: A string representation of the json data
            None: Returns none if the file should not be generated
        """
        pass