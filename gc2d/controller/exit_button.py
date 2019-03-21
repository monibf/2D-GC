from PyQt5.QtWidgets import QAction


class ExitButton(QAction):

    def __init__(self, window):
        super().__init__('Quit', window)
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        self.triggered.connect(window.close)
