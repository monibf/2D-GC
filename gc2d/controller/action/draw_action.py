from PyQt5.QtWidgets import QAction

from gc2d.controller.integration.selector import Selector


class DrawAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A DrawAction is a QAction that when triggered, makes a Selector object
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Draw Selection', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+D')
        self.setStatusTip('Select integration area')
        self.triggered.connect(self.draw)

    def draw(self):
        """
        Makes a new Selector object, which initializes itself in the model wrapper
        :return: None
        """
        Selector(self.model_wrapper)
