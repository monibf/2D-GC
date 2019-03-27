import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget

from controller.listener.plot_3d_listener import Plot3DListener
from gc2d.view.palette.shader import PaletteShader


class Plot3DWidget(GLViewWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.listener = Plot3DListener(self, model_wrapper)

        self.setCameraPosition(distance=400)
        self.surface = gl.GLSurfacePlotItem(computeNormals=False)
        self.addItem(self.surface)

        self.surface.translate(-len(model_wrapper.model.get_2d_chromatogram_data()) / 2,
                               -len(model_wrapper.model.get_2d_chromatogram_data()[0]) / 2, 0)
        # This will need to be done dynamically later. TODO
        self.surface.scale(1, 1, 0.00001)

        self.notify('model', model_wrapper.model)

        model_wrapper.add_observer(self, self.notify)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        if name == 'model':
            if value is None:
                self.setVisible(False)
            else:
                if not self.isVisible():
                    self.setVisible(True)

                self.surface.setData(z=value.get_2d_chromatogram_data())
                self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))
        if name == 'model.palette':
            self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))
