from PyQt6.QtWidgets import QPlainTextEdit, QLabel, QGridLayout
import logging

class LoggingPane():
    pane: QGridLayout = None
    label: QLabel = None
    log: QPlainTextEdit = None

    def __init__(self):
        if self.pane is None:
            super(LoggingPane, self).__init__()
            self.pane = QGridLayout()
            self.label = QLabel("Log")
            self.log = QPlainTextEdit()
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
        self.log.appendPlainText(msg)