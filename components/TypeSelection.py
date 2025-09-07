from PyQt6.QtWidgets import QLabel, QGridLayout, QComboBox
from .Type import Type

class TypeSelection():
    typeSelectionLabel: QLabel
    typeSelectionList: QComboBox

    def __init__(self):
        self.typeSelectionLabel = QLabel("Type:")

        self.typeSelectionList = QComboBox()
        self.typeSelectionList.addItem("Item")
        self.typeSelectionList.addItem("Block")

    def addChangedEvent(self, func: callable):
        """Adds a function to the drop down's currentIndexChanged signal

        Args:
            func (callable): A function that will be caalled when the selection changes
        """        
        self.typeSelectionList.currentIndexChanged.connect(
            lambda index: func(Type(index + 1))
        )

    def createTypeSelection(self) -> QGridLayout:
        """Creates a drop down to select a type (either Block or Item)

        Returns:
            QGridLayout: A gridLayout containing a label and a drop down
        """        
        typeSelection = QGridLayout()
        typeSelection.addWidget(self.typeSelectionLabel, 0, 0)
        typeSelection.addWidget(self.typeSelectionList, 0, 1)

        return typeSelection