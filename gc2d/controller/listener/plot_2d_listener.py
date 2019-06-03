import math
from gc2d.controller.listener.widget_listener import WidgetListener


class Plot2DListener(WidgetListener):

    def __init__(self, plot2d, model_wrapper, statusbar):
        """
        A stub listener for the plot_2d_widget
        :param plot2d: the plot_2d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot2d)
        self.model_wrapper = model_wrapper
        self.statusbar = statusbar

    def mouse_move_event(self, event):
        if self.model_wrapper.model is None:
            self.statusbar.showMessage("No data")
            return
        mouse_point = self.widget.plotItem.vb.mapSceneToView(event.localPos())
        mouse_x = math.floor(mouse_point.x())
        mouse_y = math.floor(mouse_point.y())

        z_data = self.model_wrapper.model.get_2d_chromatogram_data()
        if 0 <= mouse_x < len(z_data) and 0 <= mouse_y < len(z_data[mouse_x]):
            z_value = int(z_data[mouse_x][mouse_y])
        else:
            z_value = "no data"

        self.statusbar.showMessage("x, y, z: " + str(mouse_x) +
                                   ", " + str(mouse_y) +
                                   ", " + str(z_value))

        # Do the default stuff.
        super().mouse_move_event(event)

    def mouse_leave_event(self, event):
        self.statusbar.clearMessage()
        super().mouse_leave_event(event)
