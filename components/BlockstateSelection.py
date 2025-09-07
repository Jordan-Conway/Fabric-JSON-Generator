from PyQt6.QtWidgets import QGridLayout, QLabel, QCheckBox

def createblockstateSelection() -> QGridLayout:
    """Creates a checkbox for choosing whether to generate a blockstate file

    Returns:
        QGridLayout: A gridlayout containing a label and checkbox
    """    
    blockstateLabel = QLabel("Singular Blockstate?")
    blockstateSelection = QCheckBox()

    blockstate = QGridLayout()
    blockstate.addWidget(blockstateLabel, 0, 0)
    blockstate.addWidget(blockstateSelection, 0, 1)

    return blockstate