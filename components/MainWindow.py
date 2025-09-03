from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton, QLayout
import sys
from .Type import Type
import components
import generators

class MainWindow():
    currentType: Type = Type.ITEM
    window: QWidget = None
    windowLayout: QGridLayout = None
    currentSelections: QGridLayout = None
    namePromptLabel: QLabel = None
    modName: str = "expanded-building-blocks"
    path: str = ""
    modSelection = None
    name: str = ""

    def __init__(self, parent = ..., flags = ...):
        self.window = QWidget()
        self.window.setWindowTitle("Fabric JSON Generator")

        self.windowLayout = QGridLayout()
        self.window.setLayout(self.windowLayout)

        self.populateLayout()

    def populateLayout(self):
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
        if self.currentSelections is None:
            self.currentSelections = QGridLayout()
            self.windowLayout.addLayout(self.currentSelections, 3, 0)

        selections = []

        nameInput, self.namePromptLabel = components.createNameInput(self.currentType, self.setName)

        selections.append(nameInput)
        selections.append(components.createDropTableTemplateSelection())
        selections.append(components.createRecipeTemplateSelection())
        selections.append(components.createblockstateSelection())

        for i in range(0, len(selections)):
            self.currentSelections.addLayout(selections[i], i, 0)

    def setName(self, name: str):
        self.name = name
        print("Name is now: " + self.name)

    def setCurrentType(self, type: Type):
        self.currentType = type
        self.namePromptLabel.setText(components.createNameLabelText(self.currentType))

    def changePath(self) -> None:
        self.path = self.modSelection.changeSelectedFile()
        #self.windowLayout.addLayout(self.modSelection.createModPathSelection(),1,0)
        print("Path is set to: " + self.path)

    def show(self):
        self.window.show()

    def generate(self):
        print("Generating Files")
        # blockstateGenFlags = generators.BlockstateFlags()
        # blockstateGenFlags.type = generators.BlockstateType.SINGLE
        # blockstateGen = generators.BlockstateGenerator("iron_grate_block", self.modName, blockstateGenFlags)
        # blockstateGen.generate("./")

        # assetGenFlags = generators.AssetsFlags()
        # assetGenFlags.isBlock = True
        # assetGen = generators.AssetsGenerator("iron_grate_block", self.modName, assetGenFlags)
        # assetGen.generate("./")

        return
    
def clearLayout(layout: QLayout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()