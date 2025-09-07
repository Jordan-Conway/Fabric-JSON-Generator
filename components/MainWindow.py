from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton, QLayout
import sys
from .Type import Type
import components
import generators

class MainWindow():
    """The main window of the app
    """    
    currentType: Type = Type.ITEM
    window: QWidget = None
    windowLayout: QGridLayout = None
    currentSelections: QGridLayout = None
    namePromptLabel: QLabel = None
    modName: str = "expanded-building-blocks"
    path: str = ""
    modSelection = None
    name: str = ""
    dropType: generators.LootTableTemplate = generators.LootTableTemplate.NODROPS

    def __init__(self, parent = ..., flags = ...):
        self.window = QWidget()
        self.window.setWindowTitle("Fabric JSON Generator")

        self.windowLayout = QGridLayout()
        self.window.setLayout(self.windowLayout)

        self.populateLayout()

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
        selections.append(components.createRecipeTemplateSelection())
        selections.append(components.createblockstateSelection())

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
        print("Set dropType to " + str(self.dropType))

    def changePath(self) -> None:
        """Updates the current path to the mod being used
        """        
        self.path = self.modSelection.changeSelectedFile()
        #self.windowLayout.addLayout(self.modSelection.createModPathSelection(),1,0)
        print("Path is set to: " + self.path)

    def show(self):
        self.window.show()

    def generate(self):
        """Generates files according to the current selections
        """        
        print("Generating Files for " + self.name)
        # blockstateGenFlags = generators.BlockstateFlags()
        # blockstateGenFlags.type = generators.BlockstateType.SINGLE
        # blockstateGen = generators.BlockstateGenerator("iron_grate_block", self.modName, blockstateGenFlags)
        # blockstateGen.generate("./")

        # assetGenFlags = generators.AssetsFlags()
        # assetGenFlags.isBlock = True
        # assetGen = generators.AssetsGenerator("iron_grate_block", self.modName, assetGenFlags)
        # assetGen.generate("./")

        lootTableGenFlags = generators.LootTableFlags(self.dropType, self.name)
        lootTableGen = generators.LootTableGenerator(self.name, self.modName, lootTableGenFlags)
        lootTableGen.generate("./")

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