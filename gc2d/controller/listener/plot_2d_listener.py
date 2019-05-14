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
        mouse_point = self.widget.plotItem.vb.mapSceneToView(event.localPos())
        self.statusbar.showMessage("(x, y): (" + str(round(mouse_point.x())) +
                                   ", " + str(round(mouse_point.y())) + ")")

        # Do the default stuff.
        super().mouse_move_event(event)
