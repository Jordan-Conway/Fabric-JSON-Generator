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
        self.typeSelectionList.currentIndexChanged.connect(
            lambda index: func(Type(index + 1))
        )

    def createTypeSelection(self) -> QGridLayout:
        typeSelection = QGridLayout()
        typeSelection.addWidget(self.typeSelectionLabel, 0, 0)
        typeSelection.addWidget(self.typeSelectionList, 0, 1)

        return typeSelection