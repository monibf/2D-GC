from gc2d.controller.listener.plot_listener import PlotListener


class Plot2DListener(PlotListener):

    def __init__(self, plot2d, model_wrapper):
        super().__init__(plot2d, model_wrapper)
