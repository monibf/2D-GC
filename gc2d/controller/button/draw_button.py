from PyQt5.QtWidgets import QAction
from gc2d.controller.selector import Selector

class DrawButton(QAction):

    def __init__(self, parent, model_wrapper):
        """ #TODO: this comment is what it should do, not what it does
        A DrawButton has a QAction that when triggered, draws a Region of Interest,
        and upon enter-key sends the selected region as mask to the model.
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
        Selector(self.window, self.model_wrapper)
