import numpy as np

from gc2d.model.model import Model
from gc2d.observable import Observable
from gc2d.model.integration import Integration


class ModelWrapper(Observable):

    def __init__(self):
        """
        The model wrapper is responsible for facilitating complex interaction with the model.
        """
        super().__init__()
        self.model = None
        """The model containing all information relating to the chromatogram"""
        self.integrations = []

    def set_palette(self, palette):
        """

        :param palette:
        :return:
        """
        self.model.palette = palette
        self.notify('model.palette', self.model)

    def save_model(self, location):
        """
        Later in development we may wish to save the settings of the program to file.
        :param location: The location to save to.
        :return: None
        """

        # Insert some hook to the save/load module.
        print("ModelWrapper.save_model() not yet implemented.")

    def load_model(self, file_name):
        """
        Loads the chromatogram data into a new model.
        Later in development this may be responsible for loading more than just the chromatogram data.
        :param file_name: The name of the chromatogram file to open.
        :return: None
        """
        self.close_model()
        data = []
        with open(file_name) as sourcefile:
            for line in sourcefile:
                row = [float(val.strip()) for val in line.split(",") if val.strip()]
                data.append(row)
        arr = np.array(data, dtype=np.float64)

        self.model = Model(arr, len(data[0]))

        self.notify('model', self.model)  # Notify all observers.

    def close_model(self):
        """
        Sets the model to None, effectively closing the chromatogram without closing the program.
        :return: None
        """

        self.model = None

        self.notify('model', self.model)  # Notify all observers
    
    def add_integration(self, mask):
        index = len(self.integrations)
        self.integrations.append(Integration(self, mask, index))
        self.notify('integrationUpdate', index)
        return index
    
    def update_integration(self, mask, index):
        print(index)
        self.integrations[index].update(mask)
        self.notify('integrationUpdate', index)