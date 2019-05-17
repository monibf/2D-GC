from PyQt5.QtWidgets import QAction


class HandleAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A HandleAction is a QAction that when triggered, adds a new point to the integration selector currently being
        edited
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Draw Selection', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+R')
        self.triggered.connect(self.add_point)

    def add_point(self):
        if self.window.listener.drawing_selector is not None:
            self.window.listener.drawing_selector.add_point(self.window.listener.mouse_position)
