from gc2d.controller.listener.widget_listener import WidgetListener


class Plot3DListener(WidgetListener):

    def __init__(self, plot3d, model_wrapper):
        """
        A stub listener for the plot_3d_widget
        :param plot3d: the plot_3d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot3d)
        self.model_wrapper = model_wrapper

