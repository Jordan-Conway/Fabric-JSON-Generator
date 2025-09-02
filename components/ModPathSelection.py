import os
from PyQt6.QtWidgets import QGridLayout, QLabel, QFileDialog, QPushButton

class ModPathSelection():
    directory: str | None

    modPath: QGridLayout
    modPathLabel: QLabel
    modPathSelector: QPushButton

    def __init__(self):
        self.directory = None
        self.modPathLabel = QLabel("No fabric.json selected")
        self.modPathSelector = QPushButton()
        self.modPathSelector.setText("Select fabric.json")

    def createModPathSelection(self):
        self.modPath = QGridLayout()
        self.modPath.addWidget(self.modPathLabel, 0, 0)
        self.modPath.addWidget(self.modPathSelector, 1, 0)

        return self.modPath
    
    def changeSelectedFile(self) -> str:
        print("Changing file")
        fileSelection = QFileDialog(caption="Select fabric.mod.json")
        fileSelection.setNameFilter("*.json")
        fileSelection.exec()
        filePath = fileSelection.selectedFiles()[0]
        if(filePath == None):
            print("Directory is None")
            self.modPathLabel.setText("No fabric.json selected")
            self.modPathSelector.setText("Set fabric.json")
        else:
            print("File is: " + filePath)
            self.modPathLabel.setText("Using " + filePath)
            self.modPathSelector.setText("Change")

        self.directory = os.path.dirname(filePath)

        return self.directory