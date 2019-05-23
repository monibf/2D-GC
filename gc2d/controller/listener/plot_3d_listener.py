from gc2d.controller.listener.widget_listener import WidgetListener
from PyQt5.QtCore import Qt


class Plot3DListener(WidgetListener):

    def __init__(self, plot3d, model_wrapper):
        """
        A stub listener for the plot_3d_widget
        :param plot3d: the plot_3d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot3d)
        self.model_wrapper = model_wrapper

    def key_press_event(self, event):
        mods = event.modifiers()
        ctrl = mods & Qt.ControlModifier

        if event.key() == Qt.Key_S and ctrl:
            self.widget.grabFrameBuffer().save('fileName.png')
            print('saved')

        super().key_press_event(event)

