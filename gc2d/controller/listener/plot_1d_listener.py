import math
from PyQt5.QtCore import Qt

from gc2d.controller.listener.widget_listener import WidgetListener


class Plot1DListener(WidgetListener):

    def __init__(self, plot1d, model_wrapper, statusbar):
        """
        A stub listener for the plot_1d_widget
        :param plot1d: the plot_1d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot1d)
        self.model_wrapper = model_wrapper
        self.statusbar = statusbar

        """ The model wrapper this potentially interacts with. This may not be necessary later on. """

    def mouse_move_event(self, event):
        # Get the x coordinate of the mouse location relative to the widget
        mouse_point = self.widget.plotItem.vb.mapSceneToView(event.localPos())
        mouse_x = math.floor(mouse_point.x())

        # Get the y value at x if it exists
        y_data = self.widget.plotItem.dataItems[0].curve.yData
        if 0 <= mouse_x < len(y_data):
            y_value = int(y_data[mouse_x])

        else:
            y_value = "no data"

        self.statusbar.showMessage("x, y: " + str(mouse_x) +
                                   ", " + str(y_value))

        # Do the default stuff.
        super().mouse_move_event(event)

    def mouse_scroll_event(self, event):
        """
        TODO Currently this is a template to show the potential of this.
        :param event: The scroll_event.
        :return: None? Check the returns of the default events. This might be a requirement.
        """

        mods = event.modifiers()

        # Strip modifiers.
        ctrl = mods & Qt.ControlModifier
        shift = mods & Qt.ShiftModifier
        alt = mods & Qt.AltModifier

        # Every combination of them.
        if ctrl and shift and alt:
            print("Ctrl + Shift + Alt")
        elif ctrl and shift:
            print("Ctrl + Shift")
        elif ctrl and alt:
            print("Ctrl + Alt")
        elif shift and alt:
            print("Shift + Alt")
        elif ctrl:
            print("Ctrl")
        elif shift:
            print("Shift")
        elif alt:
            print("Alt")
        else:
            print("none")

        # Do the default stuff.
        super().mouse_scroll_event(event)

    def mouse_leave_event(self, event):
        self.statusbar.clearMessage()
        super().mouse_leave_event(event)
