import numpy as np
from pyqtgraph import PlotWidget

from gc2d.controller.listener.plot_1d_listener import Plot1DListener


class Plot1DWidget(PlotWidget):

    def __init__(self, model_wrapper, statusbar, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)

        self.listener = Plot1DListener(self, model_wrapper, statusbar)
        """ The listener for the 1D plot """
        self.curve = self.plot(pen='y')
        """ The curve drawn on the 1D plot """

        # Register this widget as an observer of the model_wrapper.
        model_wrapper.add_observer(self, self.notify)

        # call notify to draw the model.
        self.notify('model', model_wrapper.model)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :param name: A String representation of the data that has changed.
        :param value: The Value of the data that has changed.
        :return: None
        """

        if name == 'model':
            if value is None:
                # Then Draw nothing.
                self.curve.setData([])
            else:
                # Draw the 2D chromatogram data as a 1D plot. This reversal of GCxGC is simply the integration over each
                # Column. Thanks to the nature of GC data, this is simply the sum of each column.
                self.curve.setData(np.sum(a=value.get_2d_chromatogram_data(), axis=1))
