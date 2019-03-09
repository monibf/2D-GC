class ModelWrapper:
    __model = None
    __viewport = None

    def set_viewport(self, viewport):
        self.__viewport = viewport

    def get_chromatogram_data(self):
        """
        :return: the chromatography data.
        """
        return self.__model.get_chromatogram_data()

    def get_data_x_offset(self):
        """
        :return: the x offset of the data. Any data before this should be ignored.
        """
        return self.__model.get_data_x_offset()

    def get_data_y_offset(self):
        """
        :return: the y offset of the data. Any data before this should be ignored.
        """
        return self.__model.get_data_y_offset()

    def get_data_z_offset(self):
        """
        :return: the z offset of the data. Any data before this value should be ignored.
        """
        return self.__model.get_data_z_offset()

    def get_period(self):
        """
        :return: the period of the data.
        """
        return self.__model.get_period()

    def set_data_x_offset(self, data_x_offset):
        """
        :param data_x_offset: the x offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__model.set_data_x_offset(data_x_offset)

    def set_data_y_offset(self, data_y_offset):
        """
        :param data_y_offset: the y offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__model.set_data_y_offset(data_y_offset)

    def set_data_z_offset(self, data_z_offset):
        """
        :param data_z_offset: the z offset to set. Any data before this value will be ignored.
        :return: Nothing
        """
        self.__model.set_data_z_offset(data_z_offset)

    def set_period(self, period):
        """
        :param period: the new period of the data.
        :return: Nothing
        """
        self.__model.set_period(period)

    def save_model(self, location):
        """
        Later in development we may wish to save the settings of the program to file.
        :param location: The location to save to.
        :return: Nothing
        """
        print("ModelWrapper.save_model() not yet implemented.")

    def load_model(self, location):
        """
        Loads the chromatogram data into a new model.
        Later in development this may be responsible for loading more than just the chromatogram data.
        :param location:
        :return:
        """
        print("ModelWrapper.load_lodel() not yet implemented.")

    def close_model(self):
        """Sets the model to None, effectively closing the chromatogram without closing the program."""
        self.__model = None

    def has_model(self):
        """
        :return: True if there is a model, False if there isn't.
        """
        return self.__model is not None