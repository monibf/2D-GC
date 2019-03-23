from gc2d.view.palette.palette import Palette


class Viridis(Palette):
    colors = [
        (68, 1, 84),
        (33, 144, 140),
        (255, 231, 37)
    ]

    def __init__(self):
        """
        Based on Viridis. Looks nice, is uniform and accessible for the colorblind.
        """
        super().__init__(self.colors)

