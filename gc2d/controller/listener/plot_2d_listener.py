from gc2d.controller.listener.widget_listener import WidgetListener
from pyqtgraph import SignalProxy


class Plot2DListener(WidgetListener):

    def __init__(self, plot2d, model_wrapper):
        """
        A stub listener for the plot_2d_widget
        :param plot2d: the plot_2d_widget
        :param model_wrapper: the model wrapper
        """

        super().__init__(plot2d)
        self.model_wrapper = model_wrapper
        self.plot2d = plot2d
        self.proxy = SignalProxy(self.plot2d.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_moved)
        self.drawing_selector = None
        self.mouse_position = None

    def mouse_moved(self, event):
        vb = self.plot2d.plotItem.vb
        mouse_pointer = vb.mapSceneToView(event[0])
        self.mouse_position = [mouse_pointer.x(), mouse_pointer.y()]
