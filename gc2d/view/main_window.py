from PyQt5.QtWidgets import QMainWindow, QLabel

from pyqtgraph import QtCore
from pyqtgraph.dockarea import Dock, DockArea

from controller.button.choose_palette_button import ChoosePaletteButton
from controller.button.exit_button import ExitButton
from controller.button.open_button import OpenButton
from controller.button.draw_button import DrawButton
from gc2d.view.plot_2d_widget import Plot2DWidget
from gc2d.view.plot_3d_widget import Plot3DWidget


class Window:

    # noinspection PyArgumentList
    def __init__(self, model_wrapper):
        """
        The Window object represents the main window of the program. It is the root element of which all other elements
        are placed into.

        :param model_wrapper: The model wrapper.
        """
        self.win = QMainWindow()

        self.model_wrapper = model_wrapper
        self.dialogs = []
        """The model wrapper."""

        # init the window settings.
        self.win.resize(250, 150)
        self.win.setWindowTitle('GCxGC')

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_graph_views()  # Create 2D and 3D dock tabs.

        # TODO status bar.
        status_bar = self.win.statusBar()
        status_bar.addWidget(QLabel("Some status"))

        self.win.show()  # Show the window.

    def create_menus(self):
        """
        Create the Tool bar menus; file, edit, help, etc.
        :return: None
        """

        main_menu = self.win.menuBar()

        # button objects need to be members because otherwise they get garbage collected
        
        file_menu = main_menu.addMenu('File')
        self.open_button = OpenButton(self.win, self.model_wrapper)
        file_menu.addAction(self.open_button.button)
        self.exit_button = ExitButton(self.win)
        file_menu.addAction(self.exit_button.button)

        edit_menu = main_menu.addMenu('Edit')
        self.draw_button = DrawButton(self.win, self.model_wrapper)
        edit_menu.addAction(self.draw_button.button)
        # TODO

        view_menu = main_menu.addMenu('View')
        self.palette_chooser_button = ChoosePaletteButton(self.win, self.model_wrapper) 
        view_menu.addAction(self.palette_chooser_button.button)

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
        self.win.setCentralWidget(dock_area)  # This is temporary

        dock_3d = Dock('3D')
        dock_area.addDock(dock_3d)

        dock_2d = Dock('2D')
        dock_area.addDock(dock_2d, 'above', dock_3d)

        self.plot_3d = Plot3DWidget(self.model_wrapper, dock_3d)
        dock_3d.addWidget(self.plot_3d.widget)

        self.plot_2d = Plot2DWidget(self.model_wrapper, dock_2d)
        dock_2d.addWidget(self.plot_2d.widget)
    
    def keyPressEvent(self, event): 
        if event.key() == QtCore.Qt.Key_Escape:
            self.win.close()
