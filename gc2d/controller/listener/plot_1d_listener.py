from PyQt5.QtCore import Qt

from gc2d.controller.listener.widget_listener import WidgetListener


class Plot1DListener(WidgetListener):

    def __init__(self, plot1d, model_wrapper):
        """
        A stub listener for the plot_1d_widget
        :param plot1d: the plot_1d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot1d)
        self.model_wrapper = model_wrapper

    def mouse_scroll_event(self, event):
        mods = event.modifiers()

        ctrl = mods & Qt.ControlModifier
        shift = mods & Qt.ShiftModifier
        alt = mods & Qt.AltModifier

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

        super().mouse_scroll_event(event)