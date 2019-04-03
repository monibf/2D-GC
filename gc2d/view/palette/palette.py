import numpy as np
from pyqtgraph import ColorMap

palettes = []


class Palette(ColorMap):

    def __init__(self, name, colors):
        """
        A callable implementation of the ColorMap from pyqtgraph that returns the lookup table when called.
        :param colors: The array storing the colors of the palette
        """
        super().__init__(pos=np.linspace(0.0, 1.0, len(colors)), color=colors)
        self.name = name
        palettes.append(self)

    def __call__(self, *args):
        """
        :param args:
        :return: the lookup table that corresponds to this palette.
        """
        return self.getLookupTable(alpha=False)


jet = Palette(
    'jet',
    [
        (000, 000, 127),
        (000, 000, 255),
        (000, 127, 255),
        (000, 255, 255),
        (127, 255, 127),
        (255, 255, 000),
        (255, 127, 000),
        (255, 000, 000),
        (127, 000, 000)
    ]
)

red_green_blue = Palette(
    'red-green-blue',
    [
        (000, 000, 255),
        (000, 255, 255),
        (000, 255, 000),
        (255, 255, 000),
        (255, 000, 000)
    ]
)

viridis = Palette(
    'viridis',
    [
        (68, 1, 84),
        (33, 144, 140),
        (255, 231, 37)
    ]
)
