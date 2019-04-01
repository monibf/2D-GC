from PyQt5.QtWidgets import QAction


class ExitButton:

    def __init__(self, parent):
        """
        An ExitButton has a QAction that will close the application when triggered.
        :param parent: the parent widget
        """
        self.button = QAction('Quit', parent)
        self.button.setShortcut('Ctrl+Q')
        self.button.setStatusTip('Exit application')
        self.button.triggered.connect(parent.close)
