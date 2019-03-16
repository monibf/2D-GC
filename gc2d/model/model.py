import numpy as np
import math
class Model:
    __chromatogram_data = None
    """The data of the chromatogram stored as a 1D array """
    data_x_offset = 0
    """The x_offset to start drawing at."""
    data_y_offset = 0
    """The y_offset to start drawing at."""
    data_z_offset = 0
    """The z_offset to start drawing at."""
    period = 0
    """The period of the second GC. """

    def __init__(self, chromatogram_data, period):
        """
        Initialises the model with the given data.

        :param chromatogram_data: The 1D array containing the chromatography data.
        """
        self.__chromatogram_data = chromatogram_data
        self.period = period

    def get_2d_chromatogram_data(self):
        """
        Constructs a 2D numpy array from the __chromatogram_data, period and data offsets.
        :return: The 2D numpy array corresponding to the current state of the model.
        """
        x = math.ceil(len(self.__chromatogram_data)/self.period)
        y = self.period
        arr = np.zeros((x - self.get_data_x_offset(), y - self.get_data_y_offset()))

        for i in range(self.get_data_x_offset(), x):
            for j in range(self.get_data_y_offset(), y):
                if i*y + j >= len(self.__chromatogram_data):
                    return arr
                arr[i-self.get_data_x_offset()][j-self.get_data_y_offset()] \
                    = max(self.data_z_offset, self.__chromatogram_data[i*y + j])

        return arr

    def get_data_x_offset(self):
        """
        :return: The bounded value of data_x_offset
        """
        return max(0, min(self.data_x_offset, math.ceil(len(self.__chromatogram_data) / self.period)))

    def get_data_y_offset(self):
        """
        :return: The bounded value of data_y_offset

        """
        return max(0, min(self.data_y_offset, self.period))
