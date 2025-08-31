from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton
import sys
import components
    
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

    dropTableTemplate = components.createDropTableTemplateSelection()
    selectionLayout.addLayout(dropTableTemplate, 0, 0)

    recipeTemplate = components.createRecipeTemplateSelection()
    selectionLayout.addLayout(recipeTemplate, 1, 0)

    blockstate = components.createblockstateSelection()
    selectionLayout.addLayout(blockstate, 2, 0)

def main():
    app = QApplication([])

    window = QWidget()

    initialise(window)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()