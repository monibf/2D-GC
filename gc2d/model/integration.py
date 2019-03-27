from PyQt5.Qt import QListWidgetItem
import numpy as np


class Integration:

    def __init__(self, model_wrapper, mask, index):
        """
        Integration mask of the chromatogram in model_wrapper in the selected region
        """
        self.label = "integration " + str(index + 1) # count from 1 
        self.mask = mask
        self.value = np.sum(mask) / np.count_nonzero(mask)


    def update (self, mask):
        self.mask = mask
        self.value = np.sum(mask) / np.count_nonzero(mask)
        print (self.label)
        print (self.value)


    def get_list_item(self):
        QListWidgetItem(self.label)