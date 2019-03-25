from pyqtgraph import ImageItem, PlotWidget


class Plot2DWidget(PlotWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)

        self.img = ImageItem()
        self.addItem(self.img)

        self.setAspectLocked(True)
        self.update('model', model_wrapper.model)

        model_wrapper.add_observer(self, self.update)

    def update(self, name, value):
        """
        Updates the image rendered to match the model.
        :return: None
        """

        if name == 'model':
            if value is None:
                self.img.clear()
            else:
                self.img.setImage(value.get_2d_chromatogram_data().clip(value.lower_bound, value.upper_bound),
                                  lut=value.palette)
        if name == 'model.palette':
            self.img.setLookupTable(value.palette)
