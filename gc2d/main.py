from model.model_wrapper import ModelWrapper
from view.main_window import Window
from PyQt5.QtWidgets import QApplication


def main():
    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """

    Window(model_wrapper)  # create the window.

    app.exec()  # Start the application
