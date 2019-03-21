import numpy as np

from model.model import Model


class ModelWrapper:

    def __init__(self):
        self.model = None
        """The model containing all information relating to the chromatogram"""

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

    def load_model(self, file_name):
        """
        Loads the chromatogram data into a new model.
        Later in development this may be responsible for loading more than just the chromatogram data.
        :param location: TODO
        :return: Nothing
        """
        self.model.period
        # Insert some hook to the save/load module.
        data = []
        with open(file_name) as sourcefile:
            for line in sourcefile:
                row = [float(val.strip()) for val in line.split(",") if val.strip()]
                data.append(row)
        arr = np.array(data, dtype=np.float64)

        self.model = Model(arr, len(data[0]))

        print('chromatogram data loaded successfully: {} by {}'.format(len(data), len(data[0])))

    def close_model(self):
        """
        Sets the model to None, effectively closing the chromatogram without closing the program.
        :return: Nothing
        """

        self.model = None
