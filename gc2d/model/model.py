class Model:
    __chromatogram_data = None
    """The data of the chromatogram stored as a 2D numpy array"""
    __data_x_offset = 0
    """The x_offset to start drawing at."""
    __data_y_offset = 0
    """The y_offset to start drawing at."""
    __data_z_offset = 0
    """The z_offset to start drawing at."""
    __period = 0
    """The period of the second GC. """

    def __init__(self, chromatogram_data):
        """
        Initialises the model with the given data.

        :param chromatogram_data: The 2d numpy array containing the chromatography data.
        """
        self.__chromatogram_data = chromatogram_data

    def get_chromatogram_data(self):
        """
        :return: the chromatography data.
        """
        return self.__chromatogram_data

    def get_data_x_offset(self):
        """
        :return: the x offset of the data. Any data before this should be ignored.
        """
        return self.__data_x_offset

    def get_data_y_offset(self):
        """
        :return: the y offset of the data. Any data before this should be ignored.
        """
        return self.__data_y_offset

    def get_data_z_offset(self):
        """
        :return: the z offset of the data. Any data before this value should be ignored.
        """
        return self.__data_z_offset

    def get_period(self):
        """
        :return: the period of the data.
        """
        return self.__period

    def set_data_x_offset(self, data_x_offset):
        """
        :param data_x_offset: the x offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__data_x_offset = data_x_offset

    def set_data_y_offset(self, data_y_offset):
        """
        :param data_y_offset: the y offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__data_y_offset = data_y_offset

    def set_data_y_offset(self, data_z_offset):
        """
        :param data_z_offset: the z offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__data_z_offset = data_z_offset
