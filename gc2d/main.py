import os

from model.model_wrapper import ModelWrapper
from view.main_window import Window
from PyQt5.QtWidgets import QApplication


def main():
    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """
    datafile = os.path.join(os.path.dirname(__file__), "..", "exampledata", "MF_AE3.txt")
    model_wrapper.load_model(datafile)
    win = Window(model_wrapper)  # create the window.

    app.exec_()  # Start the application
