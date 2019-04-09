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
        self.palette = palette.viridis
        """The palette to color the data with """
      
        self.lowest = self.__chromatogram_data.min()
        """The lowest value in the chromatogram """
        self.highest = self.__chromatogram_data.max()
        """The highest value in the chromatogram """

        self.lower_bound = self.lowest
        """ The lower bound of the intensity scale """
        self.upper_bound = self.highest
        """ The upper bound of the intensity scale """

        self.period = period
        """The period of the second GC. """

    def get_2d_chromatogram_data(self):
        return self.__chromatogram_data
