from gc2d.view.palette import palette


class Model:

    def __init__(self, chromatogram_data, period):
        """
        The Model is responsible for storing the state of the program.

        :param chromatogram_data: The 1D array containing the chromatography data.
        :param period: The period of the data.
        """

        self.__chromatogram_data = chromatogram_data
        """The data of the chromatogram stored as a 1D array """
        self.palette = palette.viridis
        """The palette to color the data with """
        self.lowest = float('inf')
        """The lowest value in the chromatogram """
        self.highest = float('-inf')
        """The highest value in the chromatogram """
        for row in chromatogram_data:
            for element in row:
                if self.highest < element:
                    self.highest = element
                if self.lowest > element:
                    self.lowest = element

        self.lower_bound = self.lowest
        """ The lower bound of the intensity scale """
        self.upper_bound = self.highest
        """ The upper bound of the intensity scale """

        self.period = period
        """The period of the second GC. """

    def get_2d_chromatogram_data(self):
        return self.__chromatogram_data
