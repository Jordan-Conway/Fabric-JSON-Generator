from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton
import sys

def initialise(window: QWidget):
    window.setWindowTitle("Fabric JSON Generator")

    windowLayout = QGridLayout()
    window.setLayout(windowLayout)

    msg = QLabel("<h1>Fabric JSON Generator</h1>", parent=window)
    windowLayout.addWidget(msg, 0, 0)

    addSelections(windowLayout)

    generateButton = QPushButton()
    generateButton.setText("Generate")
    windowLayout.addWidget(generateButton, 2, 0)    

def addSelections(window: QGridLayout):
    selectionLayout = QGridLayout()
    window.addLayout(selectionLayout, 1, 0)

    dropTableTemplate = createDropTableTemplateSelection()
    selectionLayout.addLayout(dropTableTemplate, 0, 0)

def createDropTableTemplateSelection() -> QGridLayout:
    dropTableTemplateLabel = QLabel("Drop Table Template")
    dropTableTemplateSelection = QComboBox()
    dropTableTemplateSelection.addItem("None")
    dropTableTemplateSelection.addItem("Drops Self")

    dropTableTemplate = QGridLayout()
    dropTableTemplate.addWidget(dropTableTemplateLabel, 0, 0)
    dropTableTemplate.addWidget(dropTableTemplateSelection, 0, 1)

    return dropTableTemplate

def main():
    app = QApplication([])

    window = QWidget()

    initialise(window)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()