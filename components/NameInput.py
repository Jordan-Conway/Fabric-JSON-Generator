from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit
from .Type import Type

def createNameInput(type: Type, updateName: callable) -> tuple[QGridLayout, QLabel]:
    """Creates an input for the name of the block or item to be added.

    Args:
        type (Type): The type of the item or block being added
        updateName (callable): A function to be called when the inputted name changed

    Returns:
        tuple[QGridLayout, QLabel]: A tuple of a gridLayout containing a label and a lineEdit, and a reference to that label
    """    
    nameInputLabel = QLabel(createNameLabelText(type))
    nameInputBox = QLineEdit()
    nameInputBox.textChanged.connect(lambda: updateName(nameInputBox.text()))

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