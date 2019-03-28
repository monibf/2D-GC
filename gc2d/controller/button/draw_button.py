from PyQt5.QtWidgets import QAction
from pyqtgraph import PolyLineROI 
import numpy as np


class DrawButton:

    def __init__(self, parent, model_wrapper):
        """ #TODO: this comment is what it should do, not what it does
        A DrawButton has a QAction that when triggered, draws a Region of Interest,
        and upon enter-key sends the selected region as mask to the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        self.button = QAction('Draw Selection', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.button.setShortcut('Ctrl+D')
        self.button.setStatusTip('Select integration area')
        self.button.triggered.connect(self.draw)
        
    # def draw(self):
    #     Selector(self.window)

    def draw(self):
        """
        Draw region of interest (ROI), the ROI is connected to save(self) which is called once an edit has been filled
        :return: None
        """
        self.roi = PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True) 
        self.window.plot_2d.addItem(self.roi)
        self.roi.sigRegionChangeFinished.connect(self.save)

    def save(self):
        """
        Should save the region or mask in the model part of the architecture, right now prints it
        #TODO: make this output to persistant data outside of controller
        """
        region = self.roi.getArrayRegion(self.model_wrapper.model.get_2d_chromatogram_data(), self.window.plot_2d.img)
        print (np.sum(region))
        print (np.count_nonzero(region))
        print(np.sum(region) / np.count_nonzero(region))
   