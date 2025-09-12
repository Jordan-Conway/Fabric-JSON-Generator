from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton, QLayout

from generators.BlockstateGenerator import BlockstateType
from .Type import Type
import components
import generators
from .LoggingPane import LoggingPane

logger: LoggingPane = None

class MainWindow():
    """The main window of the app
    """    
    currentType: Type = Type.ITEM
    window: QWidget = None
    topLevelLayout: QGridLayout = None
    windowLayout: QGridLayout = None
    currentSelections: QGridLayout = None
    namePromptLabel: QLabel = None
    modName: str = "expanded-building-blocks"
    path: str = ""
    modSelection = None
    name: str = ""
    dropType: generators.LootTableTemplate = generators.LootTableTemplate.NODROPS
    generateBlockstate: bool = False

    generateRecipe: bool = False
    recipeTemplate: generators.RecipeTemplate
    recipeMaterial: str
    recipeCount: int

    def __init__(self, parent = ..., flags = ...):
        self.window = QWidget()
        self.window.setWindowTitle("Fabric JSON Generator")

        global logger
        logger = LoggingPane()

        self.topLevelLayout = QGridLayout()
        self.topLevelLayout.addLayout(logger.getPane(), 0, 1)

        self.windowLayout = QGridLayout()

        self.populateLayout()

        self.window.setLayout(self.topLevelLayout)

        self.topLevelLayout.addLayout(self.windowLayout, 0, 0)

    def populateLayout(self):
        """Populates the window with all panes
        """        
        msg = QLabel("<h1>Fabric JSON Generator</h1>")
        self.windowLayout.addWidget(msg, 0, 0)

        self.modSelection = components.ModPathSelection()
        self.modSelection.modPathSelector.clicked.connect(self.changePath)
        self.windowLayout.addLayout(self.modSelection.createModPathSelection(), 1, 0)

        typeSelection = components.TypeSelection()
        typeSelection.addChangedEvent(self.setCurrentType)
        self.windowLayout.addLayout(typeSelection.createTypeSelection(), 2, 0)

        self.addSelections()

        generateButton = QPushButton()
        generateButton.setText("Generate")
        generateButton.clicked.connect(self.generate)
        self.windowLayout.addWidget(generateButton, 4, 0)    

    def addSelections(self):
        """Populates the selections pane with options for what file to generate
        """        
        if self.currentSelections is None:
            self.currentSelections = QGridLayout()
            self.windowLayout.addLayout(self.currentSelections, 3, 0)

        selections = []

        nameInput, self.namePromptLabel = components.createNameInput(self.currentType, self.setName)

        selections.append(nameInput)
        selections.append(components.createDropTableTemplateSelection(self.setDropType))
        selections.append(components.createRecipeTemplateSelection(self.setRecipeGeneration, self.setRecipeTemplate, self.setRecipeMaterial, self.setRecipeCount))
        selections.append(components.createblockstateSelection(self.setBlockstate))

        for i in range(0, len(selections)):
            self.currentSelections.addLayout(selections[i], i, 0)

    def setName(self, name: str):
        self.name = name

    def setCurrentType(self, type: Type):
        self.currentType = type
        self.namePromptLabel.setText(components.createNameLabelText(self.currentType))

    def setDropType(self, type: generators.LootTableTemplate):
        """Sets the type of drop table to generate

        Args:
            type (generators.LootTableTemplate): The drop table template to use
        """        
        self.dropType = generators.LootTableTemplate(type)
        logger.logInfo("Set dropType to " + str(self.dropType))

    def setRecipeGeneration(self, option: bool):
        """Sets whether a recipe file should be generated

        Args:
            option (bool)
        """        
        self.generateRecipe = option

    def setRecipeTemplate(self, template: generators.RecipeTemplate):
        """Sets the recipe template to be used

        Args:
            template (generators.RecipeTemplate): The template to be used
        """        
        self.recipeTemplate = template
    
    def setRecipeMaterial(self, material: str):
        """Sets the item to be used in the crafting recipe

        Args:
            material (str): A string representing the item. Must include the identifier (E.g. minecraft:iron_ingot)
        """        
        self.recipeMaterial = material

    def setRecipeCount(self, count: int):
        """Sets the number of items that the recipe should produce

        Args:
            count (int)
        """        
        self.recipeCount = count

    def setBlockstate(self, shouldGenerate: bool):
        """Sets whether a blockstate file should be generated

        Args:
            shouldGenerate (bool)
        """        
        self.generateBlockstate = shouldGenerate

    def changePath(self) -> None:
        """Updates the current path to the mod being used
        """        
        self.path = self.modSelection.changeSelectedFile()
        #self.windowLayout.addLayout(self.modSelection.createModPathSelection(),1,0)
        logger.logInfo("Path is set to: " + str(self.path))

    def show(self):
        self.window.show()

    def generate(self):
        """Generates files according to the current selections
        """        
        logger.logInfo("Generating Files for " + self.name)
        blockstateGenFlags = generators.BlockstateFlags()
        if self.generateBlockstate:
            blockstateGenFlags.type = BlockstateType.SINGLE
            blockstateGen = generators.BlockstateGenerator(self.name, self.modName, blockstateGenFlags)
            blockstateGen.generate(self.path)

        assetGenFlags = generators.AssetsFlags()
        assetGenFlags.isBlock = (self.currentType == Type.BLOCK)
        assetGen = generators.AssetsGenerator(self.name, self.modName, assetGenFlags)
        assetGen.generate(self.path)

        lootTableGenFlags = generators.LootTableFlags(self.dropType, self.name)
        lootTableGen = generators.LootTableGenerator(self.name, self.modName, lootTableGenFlags)
        lootTableGen.generate(self.path)

        if(self.generateRecipe):
            recipeGenFlags = generators.RecipeFlags(self.recipeTemplate, self.recipeMaterial, self.recipeCount)
            recipeGen = generators.RecipeGenerator(self.name, self.modName, recipeGenFlags)
            recipeGen.generate(self.path)

        return
    
def clearLayout(layout: QLayout):
    """Clears all widgets from a layout

    Args:
        layout (QLayout): The layout to clear
    """    
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()