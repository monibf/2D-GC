from gc2d.controller.listener.widget_listener import WidgetListener
from gc2d.controller.integration.selector import Selector
from PyQt5 import QtCore
from pyqtgraph import SignalProxy
class Plot2DListener(WidgetListener):

    def __init__(self, plot2d, model_wrapper):
        """
        A stub listener for the plot_2d_widget
        :param plot2d: the plot_2d_widget
        :param model_wrapper: the model wrapper
        """

        WidgetListener.key_press_event = self.key_pressq_event

        super().__init__(plot2d)
        self.model_wrapper = model_wrapper
        self.plot2d = plot2d
        self.proxy = SignalProxy(self.plot2d.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_moved)
        # plot2d.scene().sigMouseMoved.connect(mouseMoved)

    "press 'q' to create new integration area in 2d graph and 't' to draw new points and 'r' to exit drawing mode"



    def mouse_moved(self, event):
        vb = self.plot2d.plotItem.vb
        mousepoint = vb.mapSceneToView(event[0])
        self.mousepos = [mousepoint.x(), mousepoint.y()]

    def key_pressq_event(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.drawing = True
            self.selector = Selector(self.model_wrapper, self.mousepos)

        if event.key() == QtCore.Qt.Key_T and self.drawing == True:
            self.selector.add_point(self.mousepos)
        if event.key() == QtCore.Qt.Key_R:
            self.drawing = False