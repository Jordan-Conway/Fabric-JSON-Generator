from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit
from .Type import Type

def createNameInput(type: Type) -> tuple[QGridLayout, QLabel]:
    nameInputLabel = QLabel(createNameLabelText(type))
    nameInputBox = QLineEdit()

    nameInput = QGridLayout()
    nameInput.addWidget(nameInputLabel, 0, 0)
    nameInput.addWidget(nameInputBox, 0, 1)

    return nameInput, nameInputLabel

def createNameLabelText(type: Type) -> str:
    labelText = "Enter "
    if(type == Type.BLOCK):
        labelText += "Block"
    else:
        labelText += "Item"

    labelText += " Name: "

    return labelText