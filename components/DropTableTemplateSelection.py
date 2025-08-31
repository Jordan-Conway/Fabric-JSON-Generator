from PyQt6.QtWidgets import QGridLayout, QLabel, QComboBox

def createDropTableTemplateSelection() -> QGridLayout:
    dropTableTemplateLabel = QLabel("Drop Table Template")
    dropTableTemplateSelection = QComboBox()
    dropTableTemplateSelection.addItem("None")
    dropTableTemplateSelection.addItem("Drops Self")

    dropTableTemplate = QGridLayout()
    dropTableTemplate.addWidget(dropTableTemplateLabel, 0, 0)
    dropTableTemplate.addWidget(dropTableTemplateSelection, 0, 1)

    return dropTableTemplate