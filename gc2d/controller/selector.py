from PyQt5.Qt import QObject
from pyqtgraph import PolyLineROI 

class Selector(QObject):

    def __init__(self, parent, model_wrapper):
        """ 
        Selector draws a Region of Interest, and sends + updates the selected region as mask to the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__(parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.draw()
        
        
    # def draw(self):
    #     Selector(self.window)

    def draw(self):
        """
        Draw region of interest (ROI), the ROI is connected to save(self) which is called once an edit has been filled
        :return: None
        """
        self.roi = PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True) 
        self.window.plot_2d.addItem(self.roi)
        self.roi.sigRegionChangeFinished.connect(self.update)
        self.id = self.model_wrapper.add_integration(self.get_region())

    def update(self):
        """
        Updates region in model 
        """
        self.model_wrapper.update_integration(self.get_region(), self.id)

   
    def get_region(self):
        return self.roi.getArrayRegion(self.model_wrapper.model.get_2d_chromatogram_data(), self.window.plot_2d.img)