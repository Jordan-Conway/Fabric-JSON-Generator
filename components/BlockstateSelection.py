from PyQt6.QtWidgets import QGridLayout, QLabel, QCheckBox
from PyQt6.QtCore import Qt

toolTipMsg = "If selected, a blockstate file will be generated containing a default blockstate"

def createblockstateSelection(setBlockstate: callable) -> QGridLayout:
    """Creates a checkbox for choosing whether to generate a blockstate file

    Returns:
        QGridLayout: A gridlayout containing a label and checkbox
    """    
    blockstateLabel = QLabel("Singular Blockstate?")
    blockstateSelection = QCheckBox()

    blockstateLabel.setToolTip(toolTipMsg)

    blockstateSelection.checkStateChanged.connect(lambda: setBlockstate(blockstateSelection.checkState() == Qt.CheckState.Checked))

    blockstate = QGridLayout()
    blockstate.addWidget(blockstateLabel, 0, 0)
    blockstate.addWidget(blockstateSelection, 0, 1)

    return blockstate