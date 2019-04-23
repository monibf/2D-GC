import numpy as np


class Integration:

    def __init__(self, key, selector):
        """
        Container for a selection mask of a chromatogram
        Holds its own selector controller object to enable interacting with specific selectors
        Calculates mean area under the curve 
        :param key: an identifier which is unique over all integrations in the model
        :param selector: a Selector object which contains an ROI drawer
        :return: None
        """
        self.label = "integration " + str(key + 1)  # generate name
        self.id = key
        self.selector = selector
        self.mask = None
        self.pos = None
        self.value = None
        self.show = False

    def update(self, region=None, label=None):
        """
        updates the mask + integration value and/or the label
        :param mask: an updated mask
        :param label: an new label
        :return: None
        """
        if region is not None:
            mask = region[1]
            self.value = np.sum(mask) / np.count_nonzero(mask)
            self.mask = mask
            self.pos = region[0].topLeft()
        if label is not None:
            self.label = label

    def toggle_show(self):
        self.show = not self.show

