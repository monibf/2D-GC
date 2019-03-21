from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from controller.exit_button import ExitButton
from controller.open_button import OpenButton
import pyqtgraph as pg
from view.colormaps.red_green_blue import RedGreenBlue


class Window(QMainWindow):

    # noinspection PyArgumentList
    def __init__(self, model_wrapper):
        """
        The Window object represents the main window of the program. It is the root element of which all other elements
        are placed into.

        :param model_wrapper: The model wrapper.
        """
        super().__init__()

        self.model_wrapper = model_wrapper
        """The model wrapper."""

        # init the window settings.
        self.resize(250, 150)
        self.setWindowTitle('GCxGC')
        self.show()  # Show the window.

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_image()

    def create_menus(self):
        """
        Create the Tool bar menus; file, edit, help, etc.
        :return: None
        """

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')
        file_menu.addAction(OpenButton(self, self.model_wrapper))
        file_menu.addAction(ExitButton(self))

        editMenu = main_menu.addMenu('Edit')
        # TODO

        viewMenu = main_menu.addMenu('View')
        # TODO

        toolsMenu = main_menu.addMenu('Tools')
        # TODO

        helpMenu = main_menu.addMenu('Help')
        # TODO

    # noinspection PyArgumentList
    def create_image(self):

        cw = QWidget(self)
        cwl = QHBoxLayout()
        cw.setLayout(cwl)
        self.setCentralWidget(cw)

        pw = pg.PlotWidget()
        cwl.addWidget(pw)

        img = pg.ImageItem()
        pw.addItem(img)
        pw.setAspectLocked(True)

        img.setImage(self.model_wrapper.model.get_2d_chromatogram_data().clip(-30000, 581910), lut=RedGreenBlue())
