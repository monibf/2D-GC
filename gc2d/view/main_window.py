from PyQt5.QtWidgets import QLabel, QMainWindow
from pyqtgraph.dockarea import Dock, DockArea

from gc2d.controller.action.draw_action import DrawAction
from gc2d.controller.action.exit_action import ExitAction
from gc2d.controller.action.import_data_action import ImportDataAction
from gc2d.controller.action.open_edit_axes_action import OpenEditAxesAction
from gc2d.controller.action.open_file_action import OpenFileAction

from gc2d.controller.action.save_action import SaveAction
from gc2d.controller.action.save_integrations_action import SaveIntegrationsAction
from gc2d.controller.action.save_prefs_action import SavePrefsAction
from gc2d.controller.action.save_as_action import SaveAsAction

from gc2d.controller.action.export_action import ExportAction
from gc2d.controller.action.export_plot_2d_action import ExportPlot2DAction
from gc2d.controller.action.export_plot_3d_action import ExportPlot3DAction

from gc2d.controller.action.open_choose_palette_action import OpenChoosePaletteAction
from gc2d.controller.action.open_convolution_picker_action import OpenConvolutionPickerAction
from gc2d.controller.action.toggle_convolution_action import ToggleConvolutionAction
from gc2d.view.integration_list import IntegrationList
from gc2d.view.plot_1d_widget import Plot1DWidget
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

        self.plot_1d = None
        self.plot_2d = None
        self.plot_3d = None

        self.open_file_action = OpenFileAction(self, self.model_wrapper)

        self.save_action = SaveAction(self, self.model_wrapper)
        self.save_as_action = SaveAsAction(self, self.model_wrapper, self.save_action)
        self.save_integrations_action = SaveIntegrationsAction(self, self.model_wrapper)
        self.save_prefs_action = SavePrefsAction(self, self.model_wrapper)
        self.import_data_action = ImportDataAction(self, self.model_wrapper)

        self.export_action = ExportAction(self, self.model_wrapper)
        self.export_plot_2d_action = ExportPlot2DAction(self, self.model_wrapper)
        self.export_plot_3d_action = ExportPlot3DAction(self, self.model_wrapper)

        self.exit_action = ExitAction(self)
        self.draw_action = DrawAction(self, self.model_wrapper)
        self.open_edit_axes_action = OpenEditAxesAction(self, self.model_wrapper)
        self.open_palette_chooser_action = OpenChoosePaletteAction(self, self.model_wrapper)
        self.open_convolution_picker_action = OpenConvolutionPickerAction(self, self.model_wrapper)
        self.toggle_convolution_action = ToggleConvolutionAction(self, self.model_wrapper)

        status_bar = self.statusBar()

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_toolbar()
        self.create_graph_views(status_bar)  # Create 2D and 3D dock tabs.

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

        file_menu.addAction(self.import_data_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addAction(self.save_integrations_action)
        file_menu.addAction(self.save_prefs_action)

        file_menu.addSeparator()
        file_menu.addAction(self.export_plot_2d_action)
        file_menu.addAction(self.export_plot_3d_action)

        file_menu.addAction(self.exit_action)

        edit_menu = main_menu.addMenu('Edit')
        edit_menu.addAction(self.draw_action)
        edit_menu.addAction(self.open_edit_axes_action)

        view_menu = main_menu.addMenu('View')
        view_menu.addAction(self.open_palette_chooser_action)
        view_menu.addAction(self.toggle_convolution_action)

        tools_menu = main_menu.addMenu('Tools')
        tools_menu.addAction(self.open_convolution_picker_action)
        # TODO

        help_menu = main_menu.addMenu('Help')
        # TODO
    
    def create_toolbar(self):
        
        self.toolbar = self.addToolBar("toolbar")
        self.toolbar.addAction(self.toggle_convolution_action)
        self.toolbar.addAction(self.open_convolution_picker_action)
        self.toolbar.addAction(self.open_palette_chooser_action)
        self.toolbar.addAction(self.draw_action)
        self.toolbar.addAction(self.export_action)

    # noinspection PyArgumentList
    def create_graph_views(self, status_bar):
        """
        Creates the window containing the graph views.
        :return: None. Later it should return a QWidget containing the views.
        """
        dock_area = DockArea()
        self.setCentralWidget(dock_area)  # This is temporary

        dock_3d = Dock('3D')
        dock_area.addDock(dock_3d)

        dock_1d = Dock('1D')
        dock_area.addDock(dock_1d, 'above', dock_3d)

        dock_2d = Dock('2D')
        dock_area.addDock(dock_2d, 'above', dock_3d)

        self.plot_3d = Plot3DWidget(self.model_wrapper, dock_3d)
        dock_3d.addWidget(self.plot_3d)

        self.plot_2d = Plot2DWidget(self.model_wrapper, status_bar, dock_2d)
        dock_2d.addWidget(self.plot_2d)

        self.plot_1d = Plot1DWidget(self.model_wrapper, status_bar, dock_1d)
        dock_1d.addWidget(self.plot_1d)

        # TODO: move away from this function
        dock_list = Dock('integration')
        dock_area.addDock(dock_list)
        dock_list.addWidget(IntegrationList(self.model_wrapper, dock_list))

    def addDialog(self, dialog):
        for d in self.dialogs:
            if isinstance(d, type(dialog)):
                d.show()
                d.raise_()
                d.activateWindow()
                d.showNormal()
                return

        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
        dialog.showNormal()
        self.dialogs.append(dialog)
