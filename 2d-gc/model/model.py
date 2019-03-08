class Model:
    __chromatogram_data = None
    __data_offset = 0
    __period = 0

    def __init__(self, data):
        self.__chromatogram_data = data

    def get_data(self):
        return self.__arr

    def get_data_offset(self):
        return self.__data_offset

    def get_period(self):
        return self.__period
