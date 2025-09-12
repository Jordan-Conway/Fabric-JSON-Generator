from .Generator import Generator
import json
from enum import Enum

class LootTableTemplate(Enum):
    NODROPS = 0
    DROPSELF = 1

class LootTableFlags():
    type: LootTableTemplate
    dropName: str
    mustSurviveExplosion: bool

    def __init__(self, type: LootTableTemplate, dropName: str, mustSurviveExplosion = True):
        self.type = type
        self.dropName = dropName
        self.mustSurviveExplosion = mustSurviveExplosion

class LootTableGenerator(Generator):
    flags: LootTableFlags

    def __init__(self, name, mod_name, flags: LootTableFlags):
        super().__init__(name, mod_name)
        self.flags = flags

    def generate(self, path):
        if(Generator.checkValidPath(path) is False):
            print("Error: Invalid path. Are you sure the loot table folder exists?")
            print("Path: " + path)
            return None
        
        pathForLootTable = path + "\\data\\" + self.mod_name + "\\loot_table\\blocks\\"
        
        self.outputFile(pathForLootTable)

        print("Finished generating loot table files")
    
    def _createString(self) -> str | None:
        match self.flags.type:
            case LootTableTemplate.NODROPS:
                print("No loot table to generate")
                return None
            case LootTableTemplate.DROPSELF:
                return self._createSelfLootTableString()
            case _:
                print("Unsupported loot table selected: " + str(self.flags.type))
                return None

    def _createSelfLootTableString(self) -> str:
        """Creates a string representation of a drop table for a block that drops itself.

        Returns:
            str: A string representation of the generated drop table
        """        
        data = {
            "type": "minecraft:block",
            "pools":
            [
                {
                    "rolls": 1,
                    "entries": 
                    [
                        {
                            "type": "minecraft:item",
                            "name": self.mod_name + ":" + self.flags.dropName
                        }
                    ],
                    "conditions":
                    [
                        
                    ]
                }
            ]
        }

        if self.flags.mustSurviveExplosion == True:
            data["pools"][0]["conditions"].append({"condition": "minecraft:survives_explosion"})

        return json.dumps(data, indent=2)
