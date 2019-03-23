from gc2d.view.palette.palette import Palette


class RedGreenBlue(Palette):

    colors = [
        (000, 000, 255),
        (000, 255, 255),
        (000, 255, 000),
        (255, 255, 000),
        (255, 000, 000)
    ]

    def __init__(self):
        """
        Based on Jet. It's simpler and provides a little better color range.
        """
        super().__init__(self.colors)

