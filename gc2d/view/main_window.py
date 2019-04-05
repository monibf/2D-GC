from PyQt5.QtWidgets import QLabel, QMainWindow
from pyqtgraph.dockarea import Dock, DockArea

from gc2d.controller.action.draw_action import DrawAction
from gc2d.controller.action.exit_action import ExitAction
from gc2d.controller.action.open_file_action import OpenFileAction
from gc2d.controller.action.open_choose_palette_action import OpenChoosePaletteAction
from gc2d.view.integration_list import IntegrationList
from gc2d.view.plot_2d_widget import Plot2DWidget
from gc2d.view.plot_3d_widget import Plot3DWidget


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

        self.dialogs = []

        # init the window settings.
        self.resize(500, 500)
        self.setWindowTitle('GCxGC')

        self.open_file_action = OpenFileAction(self, self.model_wrapper)
        self.exit_action = ExitAction(self)
        self.draw_action = DrawAction(self, self.model_wrapper)
        self.open_palette_chooser_action = OpenChoosePaletteAction(self, self.model_wrapper)

        self.plot_2d = None
        self.plot_3d = None

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_graph_views()  # Create 2D and 3D dock tabs.

        # TODO status bar.
        status_bar = self.statusBar()
        status_bar.addWidget(QLabel("Some status"))

        self.show()  # Show the window.

    def create_menus(self):
        """
        Create the Tool bar menus; file, edit, help, etc.
        :return: None
        """

        main_menu = self.menuBar()

        # action objects need to be members because otherwise they get garbage collected

        file_menu = main_menu.addMenu('File')

        file_menu.addAction(self.open_file_action)

        file_menu.addAction(self.exit_action)

        edit_menu = main_menu.addMenu('Edit')
        edit_menu.addAction(self.draw_action)

        view_menu = main_menu.addMenu('View')

        view_menu.addAction(self.open_palette_chooser_action)

        tools_menu = main_menu.addMenu('Tools')
        # TODO

        help_menu = main_menu.addMenu('Help')
        # TODO

    # noinspection PyArgumentList
    def create_graph_views(self):
        """
        Creates the window containing the graph views.
        :return: None. Later it should return a QWidget containing the views.
        """
        dock_area = DockArea()
        self.setCentralWidget(dock_area)  # This is temporary

        dock_3d = Dock('3D')
        dock_area.addDock(dock_3d)

        dock_2d = Dock('2D')
        dock_area.addDock(dock_2d, 'above', dock_3d)

        self.plot_3d = Plot3DWidget(self.model_wrapper, dock_3d)
        dock_3d.addWidget(self.plot_3d)

        self.plot_2d = Plot2DWidget(self.model_wrapper, dock_2d)
        dock_2d.addWidget(self.plot_2d)

        # TODO: move away from this function
        dock_list = Dock('integration')
        dock_area.addDock(dock_list)
        dock_list.addWidget(IntegrationList(self.model_wrapper, dock_list))
