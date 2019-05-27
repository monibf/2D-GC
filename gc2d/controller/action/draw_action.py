from PyQt5.QtWidgets import QAction
from gc2d.controller.integration.selector import Selector


class DrawAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A DrawAction is a QAction that when toggled switched between draw- and non-draw mode
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Draw Selection', parent, checkable=True)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+D')
        self.setStatusTip('Select integration area')
        self.toggled.connect(self.toggle_draw_mode)
        self.current_selector = None

    def toggle_draw_mode(self):
        """
        Toggles drawing mode on or off
        :return: None
        """
        self.window.plot_2d.listener.drawing_mode = not self.window.plot_2d.listener.drawing_mode
        self.window.plot_2d.scene().sigMouseClicked.connect(self.draw)

    def draw(self):
        """
        Adds new point to current selector in case the first point is drawn, else it creates a new selector at mouse location
        :return: None
        """
        if self.window.plot_2d.listener.drawing_mode is True and self.window.plot_2d.listener.selector_drawn is False:
            mouse_position = self.window.plot_2d.listener.mouse_position
            self.current_selector = Selector(self.model_wrapper, mouse_position)
            self.window.plot_2d.listener.selector_drawn = True

        elif self.window.plot_2d.listener.drawing_mode is True:
            self.current_selector.add_point(self.window.plot_2d.listener.mouse_position)