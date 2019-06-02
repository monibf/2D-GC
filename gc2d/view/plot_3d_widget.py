import pyqtgraph.opengl as gl
from pyqtgraph.opengl import GLViewWidget
import numpy as np

from gc2d.controller.listener.plot_3d_listener import Plot3DListener
from gc2d.view.palette.shader import PaletteShader
from gc2d.view.palette import palette


class Plot3DWidget(GLViewWidget):

    def __init__(self, model_wrapper, parent=None):
        """
        The Plot3DWidget is responsible for rendering the 3D chromatogram data, and showing highlights of integration areas
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent=parent)
        self.listener = Plot3DListener(self, model_wrapper)
        """The listener for the 3D plot"""
        self.integrations = {}
        """The integrations array"""
        self.surface = gl.GLSurfacePlotItem(computeNormals=False)
        """The surface to render the chromatogram"""

        # add the surface to the plot
        self.addItem(self.surface)

        # move the camera back a bit
        self.setCameraPosition(distance=400)

        # Scale down the height of the mesh.
        self.surface.scale(1, 1, 0.00001)  # TODO This will need to be done dynamically later.
        
        #TODO What is this?
        self.translation_x, self.translation_y = 0, 0

        # Register this widget as an observer of the model_wrapper.
        model_wrapper.add_observer(self, self.notify)

        # call notify to draw the model. NOTE: again, if statement not  required as notify already checks if   model is None.
        self.notify('model', model_wrapper.model)

    def notify(self, name, value):
        """
        Updates the image rendered to match the model; is able to draw and remove integration highlights.
        :return: None
        """

        if name == 'integrationUpdate' and value.show is True:
                self.set_highlight(value)

        if name == "showIntegration":
            if value.show is True:
                highlight = gl.GLSurfacePlotItem(computeNormals=False)
                self.addItem(highlight)
                highlight.setShader(PaletteShader(self.lower_bound + self.offset, self.upper_bound +self.offset, palette.jet))
                self.integrations[value.id] = highlight
                self.set_highlight(value)
                self.integrations[value.id].scale(1, 1, 0.00001)
            else:
                self.removeItem(self.integrations[value.id]) 

        if name == "removeIntegration" and value.id in self.integrations:
            self.removeItem(self.integrations[value.id])            
                    
        if name == 'model':
            if value is None or value.get_2d_chromatogram_data() is None:
                self.setVisible(False)
            else:
                if not self.isVisible():
                    prev_x, prev_y = self.translation_x, self.translation_y
                    self.translation_x = -len(value.get_2d_chromatogram_data()) / 2
                    self.translation_y = -len(value.get_2d_chromatogram_data()[0]) / 2
                    self.surface.translate(self.translation_x - prev_x, self.translation_y - prev_y, 0)
                    self.surface.setData(z=value.get_2d_chromatogram_data())
                    self.setVisible(True)
                self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))
                self.lower_bound = value.lower_bound
                self.upper_bound = value.upper_bound
                self.offset = self.upper_bound
        if name == 'model.palette' or name == 'model.lower_bound' or name == 'model.upper_bound':
            self.surface.setShader(PaletteShader(value.lower_bound, value.upper_bound, value.palette))

    def set_highlight(self, integration):
        """
        Computes where the bounding box of an ROI is located and sets the data for a surface plot in self.integrations[id]
        with, if the data is inside the ROI the model data (somewhat higher to avoid clipping) and np.nan in the rest of the 
        bounding box + outside model region
        """
        bound_x = int(integration.pos.x()) + self.translation_x
        bound_y = int(integration.pos.y()) + self.translation_y
        range_x = np.arange(bound_x, bound_x + len(integration.mask))
        range_y = np.arange(bound_y, bound_y + len(integration.mask[0]))

        highlight = np.where(integration.mask > 0, integration.mask + self.offset, np.nan)
        self.integrations[integration.id].setData(x=range_x, y=range_y, z=highlight) 
