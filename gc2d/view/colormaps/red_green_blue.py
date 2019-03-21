import numpy as np

from pyqtgraph import ColorMap


class RedGreenBlue(ColorMap):

    colors = [
        (  0,   0, 255),
        (  0, 255, 255),
        (  0, 255,   0),
        (255, 255,   0),
        (255,   0,   0)
    ]

    def __init__(self):
        """
        Based on Jet. It's simpler and provides a little better color range.
        """
        super().__init__(pos=np.linspace(0.0, 1.0, len(self.colors)), color=self.colors)
        self.lut = self.getLookupTable(alpha=False)

    def __call__(self, *args, **kwargs):
        """
        :param args: Ignored
        :param kwargs: Ignored
        :return: the lookup table that corresponds to this colormap.
        """
        return self.lut
