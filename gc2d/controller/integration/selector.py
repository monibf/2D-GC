from PyQt5.Qt import QColor, QObject, QPen
from pyqtgraph import PolyLineROI


class Selector(QObject):

    def __init__(self, model_wrapper):
        """ 
        Selector draws a Region of Interest, and sends + updates the selected region as mask to the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__()
        self.model_wrapper = model_wrapper
        self.roi = None
        self.id = None
        self.draw()

    def draw(self):
        """
        Draw region of interest (ROI)
        the ROI is connected to save(self) which is called every time the ROI has been edited
        :return: None
        """
        pen = QPen()
        pen.setStyle(1)  # solid line
        pen.setWidth(4)
        pen.setColor(QColor("red"))
        self.roi = PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=pen, closed=True)
        self.id = self.model_wrapper.get_new_key()
        self.model_wrapper.add_integration(self, self.id)

    def update_mask(self):
        """
        Updates region mask in model 
        :return: None
        """
        self.model_wrapper.update_integration(self.id, mask=self.get_region())

    def set_viewport(self, img):
        self.viewport = img
        self.roi.sigRegionChangeFinished.connect(self.update_mask)
        self.update_mask()

    def get_region(self):
        """
        generates a mask for ROI region of the current chromatogram
        :return: The generated mask of the chromatogram 
        """
        return self.roi.getArrayRegion(self.model_wrapper.model.get_2d_chromatogram_data(), self.viewport)

    def get_handles(self):
        return self.roi.getSceneHandlePositions()
        
