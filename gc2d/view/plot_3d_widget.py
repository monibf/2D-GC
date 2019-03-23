import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget

from gc2d.view.palette.red_green_blue import RedGreenBlue
from gc2d.view.palette.shader import PaletteShader


class Plot3DWidget(GLViewWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.model_wrapper = model_wrapper
        model = model_wrapper.model

        self.setCameraPosition(distance=400)

        self.surface = gl.GLSurfacePlotItem(z=model.get_2d_chromatogram_data(), computeNormals=False,
                                            shader=PaletteShader(model.lower_bound, model.upper_bound, RedGreenBlue()))
        self.addItem(self.surface)

        self.surface.translate(-len(model_wrapper.model.get_2d_chromatogram_data()) / 2,
                               -len(model_wrapper.model.get_2d_chromatogram_data()[0]) / 2, 0)
        # This will need to be done dynamically later. TODO
        self.surface.scale(1, 1, 0.00001)

        self.notify()
        self.model_wrapper.add_observer(self, self.notify)

    def notify(self):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        model = self.model_wrapper.model
        self.surface.setData(z=model.get_2d_chromatogram_data())
        self.surface.setShader(PaletteShader(model.lower_bound, model.upper_bound, RedGreenBlue()))
