import os
import sys

from PyQt5.QtWidgets import QApplication

from gc2d.model.model_wrapper import ModelWrapper
from gc2d.model.palette.palette import load_custom_palettes
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
    load_custom_palettes(CUSTOM_PALETTE_PATH)

    model_wrapper = ModelWrapper()
    """ The model wrapper. """
    app = QApplication([])
    """ The Qt application. """
    if len(sys.argv) > 1:
        datafile = os.path.join(os.getcwd(), sys.argv[1])
        model_wrapper.import_model(datafile)
    
    win = Window(model_wrapper)  # create the window.

    sys.exit(app.exec_())
