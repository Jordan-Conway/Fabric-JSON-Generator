from PyQt6.QtWidgets import QTextEdit, QLabel, QGridLayout
from PyQt6.QtGui import QTextCharFormat, QColor

infoFont = QTextCharFormat()
errorFont = QTextCharFormat()
warningFont = QTextCharFormat()

infoColor = QColor()
errorColor = QColor()
warningColor = QColor()

infoColor.setRgb(0,0,0)
errorColor.setRgb(209, 53, 33)
warningColor.setRgb(214, 195, 23)

infoFont.setForeground(infoColor)
infoFont.setFontPointSize(9)
errorFont.setForeground(errorColor)
errorFont.setFontPointSize(9)
warningFont.setForeground(warningColor)
warningFont.setFontPointSize(9)

class LoggingPane():
    pane: QGridLayout = None
    label: QLabel = None
    log: QTextEdit = None

    def __init__(self):
        if self.pane is None:
            super(LoggingPane, self).__init__()
            self.pane = QGridLayout()
            self.label = QLabel("Log")
            self.log = QTextEdit()
            self.log.setReadOnly(True)
                
            self.pane.addWidget(self.label, 0, 0)
            self.pane.addWidget(self.log, 1, 0)

    def getPane(self) -> QGridLayout:
        """Returns the pane for displaying logs

        Returns:
            QGridLayout: A QGridLayout containing a label and the logging pane
        """           
        return self.pane

    def logInfo(self, msg: str):
        """Logs at info level

        Args:
            msg (str): The message to be logged
        """        
        self.log.textCursor().insertText(msg + "\n", infoFont)
    
    def logError(self, msg: str):
        """Logs at error level

        Args:
            msg (str): The message to be logged
        """        
        self.log.textCursor().insertText(msg + "\n", errorFont)

    def logWarning(self, msg: str):
        """Logs at warning level

        Args:
            msg (str): The message to be logged
        """        
        self.log.textCursor().insertText(msg + "\n", warningFont)