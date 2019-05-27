from PyQt5.QtWidgets import QAction

from gc2d.controller.integration.selector import Selector

class NewSelectorAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A NewSelectorAction is a QAction that when triggered, causes the next mouse click to create a new selector
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('New selector', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+Shift+D')
        self.triggered.connect(self.new_selector)
        self.current_selector = None

    def new_selector(self):
        self.window.plot_2d.listener.selector_drawn = False
