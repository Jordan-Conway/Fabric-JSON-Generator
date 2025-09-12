import os
from PyQt6.QtWidgets import QGridLayout, QLabel, QFileDialog, QPushButton

class ModPathSelection():
    """A class that manages the current path to the mod
    """    
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
        """Creates a gridLayout that allows for the mod path to be changed.

        Returns:
            _type_: A gridLayout containing a label and pushButton
        """        
        self.modPath = QGridLayout()
        self.modPath.addWidget(self.modPathLabel, 0, 0)
        self.modPath.addWidget(self.modPathSelector, 1, 0)

        return self.modPath
    
    def changeSelectedFile(self) -> str:
        """Opens a dialog to allow the user to select their mod's fabric.json file

        Returns:
            str: A string represeting the path to the directory containing fabric.json file.
        """        
        print("Changing file")
        
        filePath = self.getFileSelection()

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
    
    def getFileSelection(self) -> str | None:
        fileSelection = QFileDialog(caption="Select fabric.mod.json")
        fileSelection.setNameFilter("*.json")
        fileSelection.exec()
        selectedFiles = fileSelection.selectedFiles()

        # If no files were selected
        if len(selectedFiles) == 0:
            return None
        
        return selectedFiles[0]