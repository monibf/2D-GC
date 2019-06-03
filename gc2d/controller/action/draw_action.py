from PyQt5.QtWidgets import QAction
import pyqtgraph as pg
from gc2d.controller.integration.selector import Selector


class DrawAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A DrawAction is a QAction that when triggered, makes a Selector object
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Draw Selection', parent, checkable=True)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+D')
        self.setStatusTip('Select integration area')
        self.setEnabled(self.model_wrapper.model is not None)
        self.model_wrapper.add_observer(self, self.notify)
        self.toggled.connect(self.toggle_draw_mode)
        self.hover = None
    def toggle_draw_mode(self):
        """
        Toggles drawing mode on or off
        :return: None
        """
        self.window.plot_2d.listener.drawing_mode = not self.window.plot_2d.listener.drawing_mode
        self.window.plot_2d.scene().sigMouseClicked.connect(lambda event: self.signal(event))
        self.window.plot_2d.scene().sigMouseHover.connect(lambda event: self.signal2(event))

    def signal2(self, object):
        if len(object) > 1:
            self.hover = object[1]
        else:
            self.hover = None

    def signal(self, object):
        """
        Make it so that the draw function is only called in case left-mouse button is pressed
        :return: None
        """
        if object.button() == 1 and not isinstance(self.hover, pg.graphicsItems.ROI._PolyLineSegment):
            self.draw()

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

    def notify(self, name, value):
        if name == 'model':
            self.setEnabled(value is not None)