from PyQt5.Qt import QColor, QObject, QPen
from pyqtgraph import PolyLineROI

from gc2d.model.preferences import PreferenceEnum

class Selector(QObject):

    def __init__(self, model_wrapper, label=None, handles=None, pos=None):
        """ 
        Selector can draw a Region of Interest once a viewport (pyqtgraph plot) is set
        It sends + updates the selected region as mask in the model
        :param model_wrapper: The Model Wrapper
         - optional params are used for reloading saved data -
        :param label: a preset integration label
        :param handles: handle positions of a region of interest within a bounding box
        :param pos: the location of the bounding box in the scene
        """
        super().__init__()
        self.model_wrapper = model_wrapper
        self.roi = None
        self.id = None
        self.viewport = None
        self.label = label 
        self.draw(handles, pos)
        

    def draw(self, handles, pos):
        """
        Initialize a region of interest (ROI) with the default pen preference
        If handles and pos are specified, an ROI is reloaded
        :return: None
        """
        pen = self.model_wrapper.get_preference(PreferenceEnum.PEN)
        pen.setCosmetic(True)
        if handles == None:
            self.roi = PolyLineROI([[80, 60], [90, 30], [60, 40]], pos=(100,100), pen=pen, closed=True)
        else: 
            self.roi = PolyLineROI(handles, pos=pos, pen=pen, closed=True)       
        self.id = self.model_wrapper.get_new_key()
        self.model_wrapper.add_integration(self, self.id)

    def update_mask(self):
        """
        Updates region mask in model 
        :return: None
        """
        if self.viewport is None:
            return
        self.model_wrapper.update_integration(self.id, mask=self.get_region())

    def set_viewport(self, plot):
        """
        sets a pyqtgraph imageItem to find the viewport of the screen, so the current array region can be found
        :param plot: a pyqtgraph imageitem, usually a 2d plot
        :return: None
        """
        self.viewport = plot
        self.roi.sigRegionChangeFinished.connect(self.update_mask)
        self.update_mask()
        if self.label != None: self.model_wrapper.update_integration(self.id, label=self.label)

    def get_region(self):
        """
        TODO this is region not maks tuple!
        generates a mask for ROI region of the current chromatogram
        :return: The generated mask of the chromatogram 
        """
        return (self.roi.parentBounds(), self.roi.getArrayRegion(self.model_wrapper.model.get_2d_chromatogram_data(), self.viewport))

    def get_handles(self):
        """ returns the handles in local space and the position of the bounding box in the scene """
        return self.roi.getLocalHandlePositions(), self.roi.pos()
 
