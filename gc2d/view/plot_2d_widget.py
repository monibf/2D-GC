from pyqtgraph import PlotWidget, ImageItem

from view.palette.red_green_blue import RedGreenBlue


class Plot2DWidget(PlotWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.model_wrapper = model_wrapper

        self.img = ImageItem()
        self.addItem(self.img)

        self.setAspectLocked(True)
        self.update()
        self.model_wrapper.add_observer(self, self.update)

    def update(self):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        model = self.model_wrapper.model

        if model is None:
            self.img.clear()
        else:
            self.img.setImage(model.get_2d_chromatogram_data().clip(model.lower_bound, model.upper_bound),
                              lut=RedGreenBlue())
