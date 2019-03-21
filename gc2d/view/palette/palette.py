from pyqtgraph import ColorMap
import numpy as np


class Palette(ColorMap):

    def __init__(self, colors):
        """
        A callable implementation of the ColorMap from pyqtgraph that returns the lookup table when called.
        :param colors: The array storing the colors of the palette
        """
        super().__init__(pos=np.linspace(0.0, 1.0, len(colors)), color=colors)

    def __call__(self, *args):
        """
        :param args:
        :return: the lookup table that corresponds to this palette.
        """
        return self.getLookupTable(alpha=False)
