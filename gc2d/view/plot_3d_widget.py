import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget
import matplotlib.pyplot as plt
from view.palette.red_green_blue import RedGreenBlue


class Plot3DWidget(GLViewWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.model_wrapper = model_wrapper
        self.setCameraPosition(distance=50)
        z = model_wrapper.model.get_2d_chromatogram_data()
        cmap = plt.get_cmap('jet')
        minZ = model_wrapper.model.lower_bound
        maxZ = model_wrapper.model.upper_bound
        rgba_img = cmap((model_wrapper.model.get_2d_chromatogram_data() - minZ) / (maxZ - minZ))
        self.surface = gl.GLSurfacePlotItem(z=z/100000, computeNormals=False, shader='heightColor')
        self.surface.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
        self.addItem(self.surface)

        self.notify()
        self.model_wrapper.add_observer(self, self.notify)

    def notify(self):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        model = self.model_wrapper.model
