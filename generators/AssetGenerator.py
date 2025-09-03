from .Generator import Generator
import json

class AssetsFlags():
    isBlock: bool

class AssetsGenerator(Generator):
    flags: AssetsFlags

    def __init__(self, name, mod_name, flags: AssetsFlags):
        super().__init__(name, mod_name)
        self.flags = flags

    def generate(self, path):
        if(Generator.checkValidPath(path) is False):
            print("Error: Invalid path. Are you sure the blockstates folder exists?")
            return None
        
        pathForBlocks = path + "src\\main\\resources\\assets\\" + self.mod_name + "\\blocks\\"
        pathForItems = path + "src\\main\\resources\\assets\\" + self.mod_name + "\\items\\"

        self.outputFile(pathForItems)
        print("Finished generating item asset file")

        if self.flags.isBlock:
            self.outputFile(pathForBlocks)
            print("Finished generating block asset file")

    def _createString(self) -> str | None:
        data = {
            "model":
            {
                "type": "minecraft:model",
                "model": (self.mod_name + ":" + "block/" + self.name)
            }
        }
        return json.dumps(data, indent=2)

