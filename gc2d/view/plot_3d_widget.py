import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget
import numpy as np

from gc2d.controller.listener.plot_3d_listener import Plot3DListener
from gc2d.view.palette.shader import PaletteShader
from gc2d.view.palette import palette


class Plot3DWidget(GLViewWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)
        self.listener = Plot3DListener(self, model_wrapper)
        self.setCameraPosition(distance=400)
        
        self.integrations = {}

        self.surface = gl.GLSurfacePlotItem(computeNormals=False)
        self.addItem(self.surface)

        self.translation_x = -len(model_wrapper.model.get_2d_chromatogram_data()) / 2
        self.translation_y = -len(model_wrapper.model.get_2d_chromatogram_data()[0]) / 2
        self.surface.translate(self.translation_x, self.translation_y, 0)
        # This will need to be done dynamically later. TODO
        self.surface.scale(1, 1, 0.00001)

        self.notify('model', model_wrapper.model)

        model_wrapper.add_observer(self, self.notify)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model.
        :return: None
        """
        if name == 'integrationUpdate':
            
            if value.show is True:
                
                if value.id not in self.integrations:
                    highlight = gl.GLSurfacePlotItem(computeNormals=False)
                    self.addItem(highlight)
                    highlight.setShader(PaletteShader(self.lower_bound, self.upper_bound, palette.jet))
                    self.integrations[value.id] = highlight
                    self.set_highlight(value)
                    self.integrations[value.id].scale(1, 1, 0.00001)
                else:
                    self.set_highlight(value)
                    # indices = self.bounding_box_indices(value.pos)
                    # highlight.setData(x=indices[0], y=indices[1], z=value.mask + 100000) 
                    
        if name == 'model':
            if value is None:
                self.setVisible(False)
            else:
                if not self.isVisible():
                    self.setVisible(True)

                self.surface.setData(z=value.get_2d_chromatogram_data())
                self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))
                self.lower_bound = value.lower_bound
                self.upper_bound = value.upper_bound
        if name == 'model.palette':
            self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))

    def set_highlight(self, integration):
        bound_x = int(integration.pos.x()) + self.translation_x
        bound_y = int(integration.pos.y()) + self.translation_y
        range_x = np.arange(bound_x, bound_x + len(integration.mask))
        range_y = np.arange(bound_y, bound_y + len(integration.mask[0]))
        integration.mask[integration.mask > 0] += self.upper_bound * 0.01
        self.integrations[integration.id].setData(x=range_x, y=range_y, z=integration.mask) 
