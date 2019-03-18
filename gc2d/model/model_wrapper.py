class ModelWrapper:

    def __init__(self):
        """The model containing all information relating to the chromatogram"""
        model = None

    def get_integration(self):
        """
        Integrate using the current settings in the model.
        :return: The integration value.
        """

        # Insert some hook to the integration module.
        print("ModelWrapper.save_model() not yet implemented.")

    def save_model(self, location):
        """
        Later in development we may wish to save the settings of the program to file.
        :param location: The location to save to.
        :return: Nothing
        """

        # Insert some hook to the save/load module.
        print("ModelWrapper.save_model() not yet implemented.")

    def load_model(self, location):
        """
        Loads the chromatogram data into a new model.
        Later in development this may be responsible for loading more than just the chromatogram data.
        :param location: TODO
        :return: Nothing
        """

        # Insert some hook to the save/load module.
        print("ModelWrapper.load_model() not yet implemented.")

    def close_model(self):
        """
        Sets the model to None, effectively closing the chromatogram without closing the program.
        :return: Nothing
        """

        self.model = None
