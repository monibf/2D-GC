import numpy as np
from pyqtgraph import PlotWidget

from gc2d.controller.listener.plot_1d_listener import Plot1DListener


class Plot1DWidget(PlotWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)

        self.listener = Plot1DListener(self, model_wrapper)
        self.curve = self.plot(pen='y')
        self.notify('model', model_wrapper.model)
        model_wrapper.add_observer(self, self.notify)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :return: None
        """

        if name == 'model':
            if value is None:
                self.curve.setData([])
            else:
                self.curve.setData(np.sum(a=value.get_2d_chromatogram_data(), axis=1))
