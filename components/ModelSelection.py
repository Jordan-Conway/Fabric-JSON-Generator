from PyQt6.QtWidgets import QLabel, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt

itemTooltipMsg = "If selected, an item model file will be generated"
blockTooltipMsg = "If selected, a block model file will be generated"

def createModelSelection(updateItemModel: callable, updateBlockModel: callable) -> QGridLayout:
    itemLabel = QLabel("Generate Item Model?")
    itemLabel.setToolTip(itemTooltipMsg)
    itemCheckbox = QCheckBox()
    itemCheckbox.checkStateChanged.connect(lambda: updateItemModel(itemCheckbox.checkState() == Qt.CheckState.Checked))

    blockLabel = QLabel("Generate Block Model?")
    blockLabel.setToolTip(blockTooltipMsg)
    blockCheckbox = QCheckBox()
    blockCheckbox.checkStateChanged.connect(lambda: updateBlockModel(blockCheckbox.checkState() == Qt.CheckState.Checked))

    layout = QGridLayout()
    layout.addWidget(itemLabel, 0, 0)
    layout.addWidget(itemCheckbox, 0, 1)
    layout.addWidget(blockLabel, 1, 0)
    layout.addWidget(blockCheckbox, 1, 1)

    return layout