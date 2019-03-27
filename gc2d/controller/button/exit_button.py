from PyQt5.QtWidgets import QAction


class ExitButton(QAction):

    def __init__(self, parent):
        """
        An ExitButton is a QAction that will close the application when triggered.
        :param parent: the parent widget
        """
        super().__init__('Quit', parent)
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        self.triggered.connect(parent.close)
