from PyQt6.QtWidgets import QGridLayout, QLabel, QComboBox

def createDropTableTemplateSelection(updateDropTable: callable) -> QGridLayout:
    dropTableTemplateLabel = QLabel("Drop Table Template")
    dropTableTemplateSelection = QComboBox()
    # These have to be added in the same order as they are listed in the LootTableTemplate class.
    # TODO: Ensure this automatically
    dropTableTemplateSelection.addItem("None")
    dropTableTemplateSelection.addItem("Drops Self")
    dropTableTemplateSelection.currentIndexChanged.connect(lambda: updateDropTable(dropTableTemplateSelection.currentIndex()))

    dropTableTemplate = QGridLayout()
    dropTableTemplate.addWidget(dropTableTemplateLabel, 0, 0)
    dropTableTemplate.addWidget(dropTableTemplateSelection, 0, 1)

    return dropTableTemplate