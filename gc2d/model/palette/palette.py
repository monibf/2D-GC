import os
import numpy as np
from PyQt5.QtGui import QImage, qRgb
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

        for i, p in enumerate(palettes):
            if p.name == self.name:
                palettes[i] = self
                return
        palettes.append(self)
        palettes.sort(key=(lambda palette: palette.name))

    def __call__(self, *args):
        """
        :param args:
        :return: the lookup table that corresponds to this palette.
        """
        return self.getLookupTable(alpha=False)

    def generate_preview(self, width=400, height=100):
        gradient = self.getLookupTable(start=0.0, stop=1.0, nPts=width, mode='byte', alpha=False)
        img = QImage(width, height, QImage.Format_RGB32)
        x = 0
        for color in gradient:
            for y in range(0, height):
                img.setPixel(x, y, qRgb(color[0], color[1], color[2]))
            x += 1
        return img


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

def load_custom_palette(path):
    loaded = []
    if not os.path.exists(path):
        return loaded

    if os.path.isdir(path):
        return loaded

    if os.path.isfile(path) and path.endswith(".palette"):
        data = []
        with open(path) as sourcefile:
            for line in sourcefile:
                row = [int(val.strip()) for val in line.split(",") if val.strip()]
                data.append(row)
        Palette(os.path.basename(path).split(".")[0], data)
        loaded.append(path)
    return loaded

def load_custom_palettes(path):
    loaded = []
    if not os.path.exists(path):
        return loaded

    if not os.path.isdir(path):
        loaded.extend(load_custom_palette(path))
    else:
        for file in os.listdir(path):
            p = os.path.join(path, file)
            if os.path.isfile(p):
                loaded.extend(load_custom_palette(p))
    return loaded