from gc2d.view.palette import palette


class Model:

    def __init__(self, chromatogram_data, period):
        """
        The Model is responsible for storing the state of the program.

        :param chromatogram_data: The 2D array containing the chromatography data.
        :param period: The period of the data.
        """

        self.__chromatogram_data = chromatogram_data
        """The data of the chromatogram stored as a 2D array """
        self.convolved_data = None
        """The convolved data for convolution display."""
        self.show_convolved = False
        """Whether to show convolved data."""
        self.palette = palette.viridis
        """The palette to color the data with """
      
        
        self.lowest = self.__chromatogram_data.min()
        """The lowest value in the chromatogram """
        self.highest = self.__chromatogram_data.max()
        """The highest value in the chromatogram """

        #TODO: do not hardcode this!
        self.lower_bound = self.lowest/100
        """ The lower bound of the intensity scale """
        self.upper_bound = self.highest/100
        """ The upper bound of the intensity scale """

        self.period = period
        """The period of the second GC. """

    def get_2d_chromatogram_data(self):
        if self.show_convolved and self.convolved_data is not None:
            return self.convolved_data
        return self.__chromatogram_data

    def set_convolved_data(self, data):
        self.convolved_data = data

    def get_raw_data(self):
        return self.__chromatogram_data

    def toggle_convolved(self, b):
        self.show_convolved = b

    def get_width(self):
        return self.get_2d_chromatogram_data().shape()[0]

    def get_height(self):
        return self.get_2d_chromatogram_data().shape()[1]
