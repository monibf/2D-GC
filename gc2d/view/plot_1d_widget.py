import numpy as np
from pyqtgraph import PlotWidget

from gc2d.controller.listener.plot_1d_listener import Plot1DListener


class Plot1DWidget(PlotWidget):

    def __init__(self, model_wrapper, statusbar, parent=None):
        """
        The Plot1DWidget is responsible for rendering the 1D chromatogram data.
        The data is represented as a curve plot of the integrated data over the x axis. 
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)

        self.listener = Plot1DListener(self, model_wrapper, statusbar)
        """ The listener for the 1D plot """
        self.curve = self.plot(pen='y')
        """ The curve drawn on the 1D plot """

        # Disable right click context menu.
        self.getPlotItem().setMenuEnabled(False)

        # Register this widget as an observer of the model_wrapper.
        model_wrapper.add_observer(self, self.notify)

        # call notify to draw the model.
        if model_wrapper.model is not None: 
            self.notify('model', model_wrapper.model)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :param name: A String representation of the data that has changed.
        :param value: The Value of the data that has changed.
        :return: None
        """

        if name == 'model':
            if value is None or value.get_2d_chromatogram_data() is None:
                # Then Draw nothing.
                self.curve.setData([])
            else:
                # Draw the 2D chromatogram data as a 1D plot. This reversal of GCxGC is simply the integration over each
                # Column. Thanks to the nature of GC data, this is simply the sum of each column.
                self.curve.setData(np.sum(a=value.get_2d_chromatogram_data(), axis=1))
