from view.palette.palette import Palette


class Jet(Palette):

    colors = [
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

    def __init__(self):
        """
        Jet is a rather bad color scheme, but it looks pretty so here it is. It's not perfect, determining the color
        array properly would be better, but it is basically jet.
        """
        super().__init__(self.colors)
