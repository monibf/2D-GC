from PyQt5.Qt import QListWidgetItem
import numpy as np


class Integration:

    def __init__(self, mask, index, selector):
        """
        Container for a selection mask of a chromatogram
        Calculates mean area under the curve 
        :param mask: a mask of a chromatogram (a copy of the data with zeroes outside the selected region)
        :param index: an index to generate a label
        :return: None
        """
        self.label = "integration " + str(index + 1) # generate name 
        self.mask = mask
        self.selector = selector
        self.value = np.sum(mask) / np.count_nonzero(mask)

    def update (self, mask=None, label=None):
        """
        updates the mask and integration value and/or label
        :param mask: the new mask 
        :return: None
        """
        if mask is not None:
            self.mask = mask
            self.value = np.sum(mask) / np.count_nonzero(mask)
        if label is not None:
            self.label = label
        

    def destroy(self):
        self.selector.destroy()