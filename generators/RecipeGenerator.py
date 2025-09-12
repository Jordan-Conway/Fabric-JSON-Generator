from .Generator import Generator
import json
from enum import Enum

class RecipeTemplate(Enum):
    r_1x1 = 1
    r_2x2 = 2
    r_3x3 = 3
    r_1x2 = 4
    r_2x1 = 5
    r_1x3 = 6
    r_3x1 = 7
    r_3x2 = 8
    r_2x3 = 9
    r_diamond = 10
    r_stair = 11

class RecipeFlags():
    template: RecipeTemplate
    componentName: str
    numCreated: int

    def __init__(self, template: RecipeTemplate, componentName: str, numCreated: int):
        self.template = template
        self.componentName = componentName
        self.numCreated = numCreated

class RecipeGenerator(Generator):
    flags: RecipeFlags

    def __init__(self, name, mod_name, flags: RecipeFlags):
        super().__init__(name, mod_name)
        self.flags = flags

    def generate(self, path):
        if(Generator.checkValidPath(path) is False):
            print("Error: Invalid path. Are you sure the recipe folder exists?")
            return None
            
        pathForRecipe = path + "\\data\\" + self.mod_name + "\\recipe\\"

        self.outputFile(pathForRecipe)

    def _createString(self) -> str | None:
        data = {
            "type": "minecraft:crafting_shaped",
            "pattern": self._getRecipePattern(),
            "key": {
                "#": self.flags.componentName
            },
            "result":{
                "id": self.mod_name + ":" + self.name,
                "count": self.flags.numCreated
            }
        }

        return json.dumps(data, indent=2)

    def _getRecipePattern(self) -> list:
        """Gets the recipe pattern based on the template flag

        Raises:
            NotImplementedError: Raised if an unsupported template flag is provided

        Returns:
            list: A list representing the recipe pattern
        """        
        match self.flags.template:
            case RecipeTemplate.r_1x1:
                return ["#"]
            case RecipeTemplate.r_1x2:
                return ["#", "#"]
            case RecipeTemplate.r_1x3:
                return ["#", "#", "#"]
            case RecipeTemplate.r_2x1:
                return ["##"]
            case RecipeTemplate.r_2x2:
                return ["##", "##"]
            case RecipeTemplate.r_2x3:
                return ["##", "##", "##"]
            case RecipeTemplate.r_3x1:
                return ["###"]
            case RecipeTemplate.r_3x2:
                return ["###", "###"]
            case RecipeTemplate.r_3x3:
                return ["###", "###", "###"]
            case RecipeTemplate.r_diamond:
                return [" # ", "# #", " # "]
            case RecipeTemplate.r_stair:
                return ["#  ", "## ", "###"]
            case _:
                raise NotImplementedError("Recipe selection is not implemented")
