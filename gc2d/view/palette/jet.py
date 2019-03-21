from view.palette.palette import Palette


class Jet(Palette):

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
        super().__init__(self.colors)
