from PyQt6.QtWidgets import QGridLayout, QLabel, QComboBox


def createRecipeTemplateSelection() -> QGridLayout:
    """Creates a drop down to select a recipe template

    Returns:
        QGridLayout: A gridLayout containing a label and a drop down
    """    
    recipeTemplateLabel = QLabel("Recipe Template")
    recipeTemplateSelection = QComboBox()
    recipeTemplateSelection.addItem("None")
    recipeTemplateSelection.addItem("2x2")
    recipeTemplateSelection.addItem("3x3")

    recipeTemplate = QGridLayout()
    recipeTemplate.addWidget(recipeTemplateLabel, 0, 0)
    recipeTemplate.addWidget(recipeTemplateSelection, 0, 1)

    return recipeTemplate