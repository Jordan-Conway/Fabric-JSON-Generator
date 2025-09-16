from .Generator import Generator
import json

class BlockModelGenerator(Generator):
    def __init__(self, name, mod_name):
        super().__init__(name, mod_name)

    def generate(self, path):
        if(Generator.checkValidPath(path) is False):
            print("Error: Invalid path. Are you sure the models folder exists?")
            print("Using path: " + path)
            return None
        
        path += "\\assets\\" + self.mod_name + "\\models\\block\\"

        self.outputFile(path)

    def _createString(self) -> str | None:
        data = {
            "parent": "block/cube_all",
            "textures":
            {
                "all": self.mod_name + ":block/" + self.name
            }
        }

        return json.dumps(data, indent=2)
