from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from controller.exit_button import ExitButton
from controller.open_button import OpenButton
from view.plot_2d_widget import Plot2DWidget


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
        self.create_graph_views()

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
    def create_graph_views(self):
        """
        Creates the window containing the graph views.
        :return: None. Later it should return a QWidget containing the views.
        """
        cw = QWidget(self)
        cwl = QHBoxLayout()
        cw.setLayout(cwl)

        p2d = Plot2DWidget(self.model_wrapper, cw)
        cwl.addWidget(p2d)
        self.setCentralWidget(cw)  # This is temporary
