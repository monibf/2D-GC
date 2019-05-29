import os
import sys

from PyQt5.QtWidgets import QApplication

from gc2d.model.model_wrapper import ModelWrapper
from gc2d.view.main_window import Window


def main():
    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """
    if len(sys.argv) > 1:
        datafile = os.path.join(os.getcwd(), sys.argv[1])
        model_wrapper.import_model(datafile)
    
    win = Window(model_wrapper)  # create the window.

    sys.exit(app.exec_())
