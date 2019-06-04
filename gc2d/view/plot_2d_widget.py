from pyqtgraph import ImageItem, PlotWidget

from gc2d.controller.listener.plot_2d_listener import Plot2DListener
from gc2d.model.preferences import ScaleEnum
from gc2d.model.time_unit import TimeUnit


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
        self.getPlotItem().getAxis('bottom').enableAutoSIPrefix(False)
        self.getPlotItem().getAxis('left').enableAutoSIPrefix(False)

        model_wrapper.add_observer(self, self.notify)

        # call notify to draw the model. NOTE: The if statement isn't nesessary, it checks in notify if there is
        # a model or not.
        self.notify('model', model_wrapper.model)

    def refresh_x_period(self, x_period):
        if x_period == 0:
            self.getPlotItem().getAxis('bottom').setScale(1)
        else:
            self.getPlotItem().getAxis('bottom').setScale(x_period / self.wrapper_temp.model.get_width())

    def refresh_y_period(self, y_period):
        if y_period == 0:
            self.getPlotItem().getAxis('left').setScale(1)
        else:
            self.getPlotItem().getAxis('left').setScale(y_period / self.wrapper_temp.model.get_height())

    def refresh_x_unit(self, x_unit):
        if x_unit is TimeUnit.NONE:
            self.getPlotItem().getAxis('bottom').setLabel(units="")
        else:
            self.getPlotItem().getAxis('bottom').setLabel(units=x_unit.name.lower())

    def refresh_y_unit(self, y_unit):
        if y_unit is TimeUnit.NONE:
            self.getPlotItem().getAxis('left').setLabel(units="")
        else:
            self.getPlotItem().getAxis('left').setLabel(units=y_unit.name.lower())

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
        elif name in {'model', 'model.viewTransformed'}:
            if value is None or value.get_2d_chromatogram_data() is None:
                self.img.clear()
            else:
                self.img.setImage(value.get_2d_chromatogram_data().clip(value.lower_bound, value.upper_bound),
                                  lut=value.palette)

                self.refresh_x_period(self.wrapper_temp.get_preference(ScaleEnum.X_PERIOD))
                self.refresh_y_period(self.wrapper_temp.get_preference(ScaleEnum.Y_PERIOD))
                self.refresh_x_unit(self.wrapper_temp.get_preference(ScaleEnum.X_UNIT))
                self.refresh_y_unit(self.wrapper_temp.get_preference(ScaleEnum.Y_UNIT))
        elif name == 'model.palette':
            self.img.setLookupTable(value.palette)
        elif name == 'model.lower_bound' or name == 'model.upper_bound':
            self.img.setImage(value.get_2d_chromatogram_data().clip(value.lower_bound, value.upper_bound),
                              lut=value.palette)
        elif name == ScaleEnum.X_UNIT.name:
            self.refresh_x_unit(value)
        elif name == ScaleEnum.Y_UNIT.name:
            self.refresh_y_unit(value)
        elif name == ScaleEnum.X_PERIOD.name:
            self.refresh_x_period(value)
        elif name == ScaleEnum.Y_PERIOD.name:
            self.refresh_y_period(value)
