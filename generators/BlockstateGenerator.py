from .Generator import Generator
from enum import Enum
from components import Type
import json

class BlockstateType(Enum):
    SINGLE = 1

class BlockstateFlags():
    type: BlockstateType

class BlockstateGenerator(Generator):
    flags: BlockstateFlags

    def __init__(self, name, mod_name: str, flags: BlockstateFlags):
        super().__init__(name, mod_name)
        self.flags = flags

    def generate(self, path: str) -> None:
        print("Generating blockstate file")

        if(self.flags.type is not BlockstateType.SINGLE):
            print("Error: Incorrect blockstate selection")
            return None
            
        if(Generator.checkValidPath(path) is False):
            print("Error: Invalid path. Are you sure the blockstates folder exists?")
            return None
        
        path += "src\\main\\resources\\assets\\" + self.mod_name + "\\blockstates\\"

        self.outputFile(path)

        print("Finished generating blockstate file")
    
    def _createString(self) -> str | None:
        match self.flags.type:
            case BlockstateType.SINGLE:
                return self._createSingleBlocktypeString()
            case _:
                print("Unsupported blockstate")
        return None
    
    def _createSingleBlocktypeString(self) -> str:
        data = {
            "variants":
            {
                "":
                {
                    "model": (self.mod_name + ":" + "block/" + self.name)
                }
            }
        }
        return json.dumps(data, indent=2)