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
