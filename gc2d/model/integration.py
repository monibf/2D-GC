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
        self.pos = None # track position of bounding box
        self.mean = None
        self.sum = None

    def update(self, mask=None, label=None):
        """
        updates the mask + integration value and/or the label
        :param mask: an updated mask
        :param label: an new label
        :return: None
        """
        if mask is not None:
            self.mask = mask[1]
            self.sum = np.sum(mask[1])
            if self.sum > 0.0:
                self.mean = self.sum / np.count_nonzero(mask[1])
            else: 
                # outside of graph
                self.sum = np.nan
                self.mean = np.nan
        if label is not None:
            self.label = label

    def get_state(self):
        """ return state values to be serialized """
        handles, pos = self.selector.get_handles()
        return (self.label, 
                [(handle[1].x(), handle[1].y()) for handle in handles], 
                (pos.x(), pos.y()))