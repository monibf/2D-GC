from gc2d.controller.listener.widget_listener import WidgetListener


class Plot2DListener(WidgetListener):

    def __init__(self, plot2d, model_wrapper):
        """
        A stub listener for the plot_2d_widget
        :param plot2d: the plot_2d_widget
        :param model_wrapper: the model wrapper
        """
        super().__init__(plot2d)
        self.model_wrapper = model_wrapper
