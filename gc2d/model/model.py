class Model:
    chromatogram_data = None
    """The data of the chromatogram stored as a 2D numpy array"""
    data_x_offset = 0
    """The x_offset to start drawing at."""
    data_y_offset = 0
    """The y_offset to start drawing at."""
    data_z_offset = 0
    """The z_offset to start drawing at."""
    period = 0
    """The period of the second GC. """

    def __init__(self, chromatogram_data):
        """
        Initialises the model with the given data.

        :param chromatogram_data: The 2d numpy array containing the chromatography data.
        """
        self.chromatogram_data = chromatogram_data
