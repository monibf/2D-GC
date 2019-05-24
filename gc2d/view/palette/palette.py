import os
import numpy as np
from pyqtgraph import ColorMap


class Palette(ColorMap):

    palettes = []

    def __init__(self, name, colors):
        """
        A callable implementation of the ColorMap from pyqtgraph that returns the lookup table when called.
        :param colors: The array storing the colors of the palette
        """
        super().__init__(pos=np.linspace(0.0, 1.0, len(colors)), color=colors)
        self.name = name
        Palette.palettes.append(self)

    def __call__(self, *args):
        """
        :param args:
        :return: the lookup table that corresponds to this palette.
        """
        return self.getLookupTable(alpha=False)

    @staticmethod
    def load_custom_palette(path):
        if not os.path.exists(path):
            return

        if os.path.isdir(path):
            Palette.load_custom_palettes(path)
            return

        if os.path.isfile(path) and path.endswith(".palette"):
            data = []
            with open(path) as sourcefile:
                for line in sourcefile:
                    row = [int(val.strip()) for val in line.split(",") if val.strip()]
                    data.append(row)
            Palette(os.path.basename(path).split(".")[0], data)
            print(data)

    @staticmethod
    def load_custom_palettes(path):
        if not os.path.exists(path):
            return

        if not os.path.isdir(path):
            Palette.load_custom_palette(path)

        for file in os.listdir(path):
            p = os.path.join(path, file)
            if os.path.isfile(p):
                Palette.load_custom_palette(p)


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