import numpy as np
from pyqtgraph import ColorMap


class Jet(ColorMap):

    colors = [
        (  0,   0, 127),
        (  0,   0, 255),
        (  0, 127, 255),
        (  0, 255, 255),
        (127, 255, 127),
        (255, 255,   0),
        (255, 127,   0),
        (255,   0,   0),
        (127,   0,   0)
    ]

    def __init__(self):
        """
        Jet is a rather bad color scheme, but it looks pretty so here it is. It's not perfect, determining the color
        array properly would be better, but it is basically jet.
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
