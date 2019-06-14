from PyQt5.QtWidgets import QAction


class ExitAction(QAction):

    def __init__(self, parent, shortcut=None):
        """
        An ExitAction is a QAction that will close the application when triggered.
        :param parent: the parent widget
        """
        super().__init__('Quit', parent)
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setStatusTip('Exit application')
        self.triggered.connect(parent.close)
