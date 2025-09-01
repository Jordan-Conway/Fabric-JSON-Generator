from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton
import sys
from .Type import Type
import components
import generators

class MainWindow():
    currentType: Type = Type.ITEM
    window: QWidget = None
    windowLayout: QGridLayout = None
    currentSelections: QGridLayout = None
    nameLabel: QLabel = None
    modName: str = ""

    def __init__(self, parent = ..., flags = ...):
        self.window = QWidget()
        self.window.setWindowTitle("Fabric JSON Generator")

        self.windowLayout = QGridLayout()
        self.window.setLayout(self.windowLayout)

        self.populateLayout()

    def populateLayout(self):
        msg = QLabel("<h1>Fabric JSON Generator</h1>")
        self.windowLayout.addWidget(msg, 0, 0)

        typeSelection = components.TypeSelection()
        typeSelection.addChangedEvent(self.setCurrentType)
        self.windowLayout.addLayout(typeSelection.createTypeSelection(), 1, 0)

        self.addSelections()

        generateButton = QPushButton()
        generateButton.setText("Generate")
        generateButton.clicked.connect(self.generate)
        self.windowLayout.addWidget(generateButton, 3, 0)    

    def addSelections(self):
        if self.currentSelections is None:
            self.currentSelections = QGridLayout()
            self.windowLayout.addLayout(self.currentSelections, 2, 0)

        selections = []

        nameInput, self.nameLabel = components.createNameInput(self.currentType)

        selections.append(nameInput)
        selections.append(components.createDropTableTemplateSelection())
        selections.append(components.createRecipeTemplateSelection())
        selections.append(components.createblockstateSelection())

        for i in range(0, len(selections)):
            self.currentSelections.addLayout(selections[i], i, 0)

    def setCurrentType(self, type: Type):
        self.currentType = type
        self.nameLabel.setText(components.createNameLabelText(self.currentType))

    def show(self):
        self.window.show()

    def generate(self):
        pass