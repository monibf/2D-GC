import os
import sys

from PyQt5.QtWidgets import QApplication

from gc2d.model.model_wrapper import ModelWrapper
from gc2d.view.main_window import Window

PREFERENCES_PATH = os.path.join(os.path.expanduser("~"), ".2D-GC")
CUSTOM_PALETTE_PATH = os.path.join(PREFERENCES_PATH, "palettes")
CUSTOM_KERNEL_PATH = os.path.join(PREFERENCES_PATH, "kernels")


def check_preferences_dir():
    if not os.path.exists(PREFERENCES_PATH):
        os.mkdir(PREFERENCES_PATH)
        # TODO save default preferences?

    if not os.path.exists(CUSTOM_PALETTE_PATH):
        os.mkdir(CUSTOM_PALETTE_PATH)

    if not os.path.exists(CUSTOM_KERNEL_PATH):
        os.mkdir(CUSTOM_KERNEL_PATH)


def main():
    check_preferences_dir()

    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """
    datafile = os.path.join(os.path.dirname(__file__), "..", "exampledata", "MF_AE3.txt")
    model_wrapper.load_model(datafile)
    model_wrapper.model.lower_bound = -30000
    model_wrapper.model.upper_bound = 581910
    win = Window(model_wrapper)  # create the window.

    sys.exit(app.exec_())
