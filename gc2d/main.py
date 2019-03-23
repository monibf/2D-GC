import os

from PyQt5.QtWidgets import QApplication

from gc2d.model.model_wrapper import ModelWrapper
from gc2d.view.main_window import Window


def main():
    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """
    datafile = os.path.join(os.path.dirname(__file__), "..", "exampledata", "MF_AE3.txt")
    model_wrapper.load_model(datafile)
    model_wrapper.model.lower_bound = -30000
    model_wrapper.model.upper_bound = 581910
    win = Window(model_wrapper)  # create the window.

    app.exec_()  # Start the application
