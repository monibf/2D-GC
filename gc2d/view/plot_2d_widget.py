from pyqtgraph import ImageItem, PlotWidget

from gc2d.controller.listener.plot_2d_listener import Plot2DListener


class Plot2DWidget(PlotWidget):

    def __init__(self, model_wrapper, statusbar, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)

        self.listener = Plot2DListener(self, model_wrapper, statusbar)
        """ The listener for the 2D plot """
        self.img = ImageItem()
        """ The image of the chromatogram"""
        self.wrapper_temp = model_wrapper  # TEMPORARY TODO What is this for?
        """A temporary reference to the wrapper?"""

        # Add the image to the plot.
        self.addItem(self.img)

        # Disable right click context menu.
        self.getPlotItem().setMenuEnabled(False)

        # Register this widget as an observer of the model_wrapper.
        model_wrapper.add_observer(self, self.notify)

        # call notify to draw the model.
        self.notify('model', model_wrapper.model)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        
        if name == 'newIntegration':
            self.addItem(value.selector.roi)
            value.selector.set_viewport(self.img)
        elif name == 'removeIntegration':
            self.removeItem(value.selector.roi)
        elif name == 'model':
            if value is None or value.get_2d_chromatogram_data() is None:
                self.img.clear()
            else:
                self.img.setImage(value.get_2d_chromatogram_data().clip(value.lower_bound, value.upper_bound),
                                  lut=value.palette)
        elif name == 'model.palette':
            self.img.setLookupTable(value.palette)
