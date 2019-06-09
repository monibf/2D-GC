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
        self.pos = None  # track position of bounding box
        self.show = False
        self.mean = None
        self.sum = None

    def update(self, region=None, label=None):
        """
        updates the mask + integration value and/or the label
        :param mask: an updated mask
        :param label: an new label
        :return: None
        """
        if region is not None:
            mask = region[1]
            self.mask = mask
            self.pos = region[0].topLeft()
            self.sum = np.sum(mask)
            if self.sum > 0.0:
                self.mean = self.sum / np.count_nonzero(mask)
            else:
                # outside of graph
                self.sum = 0
                self.mean = 0
        if label is not None:
            self.label = label

    def recompute(self):
        self.selector.update_mask()

    def get_state(self):
        """ return state values to be serialized """
        handles, pos = self.selector.get_handles()
        return (self.label,
                [(handle[1].x(), handle[1].y()) for handle in handles],
                (pos.x(), pos.y()))

    def set_show(self, mode):
        """
        setthe show parameter between True and False, used for highlighting in 3d view
        :return: Bool whether the setting has been changed (to reduce traffic)
        """
        if self.show == mode:
            return False
        self.selector.set_current(mode)
        self.show = mode
        return True
