from PyQt6.QtWidgets import QGridLayout, QLabel, QComboBox, QCheckBox, QLineEdit, QSpinBox
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt
from generators import RecipeTemplate

def createRecipeTemplateSelection(updateToggle: callable, updateTemplate: callable, updateMaterial: callable, updateCount: callable) -> QGridLayout:
    """Creates a drop down to select a recipe template

    Returns:
        QGridLayout: A gridLayout containing a label and a drop down
    """

    checkboxLabel: QLabel = QLabel("Generate Recipe?")
    checkbox: QCheckBox = QCheckBox()
    checkbox.checkStateChanged.connect(lambda: updateToggle((checkbox.checkState() == Qt.CheckState.Checked)))

    recipeTemplateLabel = QLabel("Recipe Template")
    recipeTemplateSelection = QComboBox()
    _addOptions(recipeTemplateSelection)
    recipeTemplateSelection.currentIndexChanged.connect(lambda: updateTemplate(RecipeTemplate(recipeTemplateSelection.currentIndex())))

    materialLabel: QLabel = QLabel("Material:")
    materialInput: QLineEdit = QLineEdit()
    materialInput.textChanged.connect(lambda: updateMaterial(materialInput.text()))

    countLabel: QLabel = QLabel("Number of items produced:")
    countInput: QSpinBox = QSpinBox()
    countInput.setRange(1, 64)
    countInput.valueChanged.connect(lambda: updateCount(countInput.value()))

    recipeTemplate = QGridLayout()

    recipeTemplate.addWidget(checkboxLabel, 0, 0)
    recipeTemplate.addWidget(checkbox, 0, 1)

    recipeTemplate.addWidget(recipeTemplateLabel, 1, 0)
    recipeTemplate.addWidget(recipeTemplateSelection, 1, 1)

    recipeTemplate.addWidget(countLabel, 2, 0)
    recipeTemplate.addWidget(countInput, 2, 1)

    recipeTemplate.addWidget(materialLabel, 3, 0)
    recipeTemplate.addWidget(materialInput, 3, 1)

    return recipeTemplate

def _addOptions(comboBox: QComboBox):
    """Adds the recipe template options to a QComboBox

    Args:
        comboBox (QComboBox): The QComboBox that will contain the items
    """    
    comboBox.addItem("Select a template")
    for e in RecipeTemplate:
        comboBox.addItem((e.name.split('_')[1]))