from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QGridLayout, QPushButton
import sys
import components

currentType = components.Type.ITEM

app: QApplication = None
mainWindow: components.MainWindow = None

def main():
    app = QApplication([])

    mainWindow = components.MainWindow()

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()