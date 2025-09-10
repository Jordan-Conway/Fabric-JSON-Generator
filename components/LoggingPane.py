from PyQt6.QtWidgets import QPlainTextEdit, QLabel, QGridLayout
import logging

class LoggingPane(logging.Handler):
    pane: QGridLayout = None
    label: QLabel
    log: QPlainTextEdit

    def __init__(self, parent):
        super(LoggingPane, self).__init__()
        self.pane = QGridLayout()
        self.label = QLabel("Log")
        self.log = QPlainTextEdit(parent)
        self.log.setReadOnly(True)
            
        self.pane.addWidget(self.label, 0, 0)
        self.pane.addWidget(self.log, 1, 0)

    def getPane(self) -> QGridLayout:
        """Returns the pane for displaying logs

        Returns:
            QGridLayout: A QGridLayout containing a label and the logging pane
        """           
        return self.pane

    def emit(self, record):
        msg = self.format(record)
        self.log.appendPlainText(msg)

    def write(self, m):
        pass