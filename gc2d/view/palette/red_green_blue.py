from view.palette.palette import Palette


class RedGreenBlue(Palette):

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
        super().__init__(self.colors)

