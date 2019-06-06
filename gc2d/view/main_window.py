from PyQt5.QtWidgets import QLabel, QMainWindow
from pyqtgraph.dockarea import Dock, DockArea
import os.path

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
from gc2d.model.preferences import Preferences, PreferenceEnum
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
        model_wrapper.add_observer(self, self.notify)

        self.dialogs = []

        # init the window settings.
        self.resize(500, 500)
        self.setWindowTitle('GCxGC')

        self.toolbar = self.addToolBar("toolbar")

        self.plot_1d = None
        self.plot_2d = None
        self.plot_3d = None

        self.save_action = SaveAction(self, self.model_wrapper)
        self.save_as_action = SaveAsAction(self, self.model_wrapper, self.save_action)

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_toolbar()
        self.create_graph_views()  # Create 2D and 3D dock tabs.

        self.show()  # Show the window.

    def create_menus(self):
        """
        Create the Tool bar menus; file, edit, help, etc.
        :return: None
        """

        main_menu = self.menuBar()

        # action objects need to be members because otherwise they get garbage collected
        file_menu = main_menu.addMenu('File')
        file_menu.addAction(OpenFileAction(self, self.model_wrapper))

        file_menu.addAction(ImportDataAction(self, self.model_wrapper))
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addAction(SaveIntegrationsAction(self, self.model_wrapper))
        file_menu.addAction(SavePrefsAction(self, self.model_wrapper))

        file_menu.addSeparator()
        file_menu.addAction(ExportPlot2DAction(self, self.model_wrapper))
        file_menu.addAction(ExportPlot3DAction(self, self.model_wrapper))

        file_menu.addAction(ExitAction(self))

        edit_menu = main_menu.addMenu('Edit')
        edit_menu.addAction(DrawAction(self, self.model_wrapper))
        edit_menu.addAction(OpenEditAxesAction(self, self.model_wrapper))

        view_menu = main_menu.addMenu('View')
        view_menu.addAction(OpenChoosePaletteAction(self, self.model_wrapper))
        view_menu.addAction(ToggleConvolutionAction(self, self.model_wrapper))

        tools_menu = main_menu.addMenu('Tools')
        tools_menu.addAction(OpenConvolutionPickerAction(self, self.model_wrapper))
        # TODO

        help_menu = main_menu.addMenu('Help')
        # TODO
    
    def create_toolbar(self):
        self.toolbar.addAction(ToggleConvolutionAction(self, self.model_wrapper))
        self.toolbar.addAction(OpenConvolutionPickerAction(self, self.model_wrapper))
        self.toolbar.addAction(OpenChoosePaletteAction(self, self.model_wrapper))
        self.toolbar.addAction(DrawAction(self, self.model_wrapper))
        self.toolbar.addAction(ExportAction(self, self.model_wrapper))

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

        dock_1d = Dock('1D')
        dock_area.addDock(dock_1d, 'above', dock_3d)

        dock_2d = Dock('2D')
        dock_area.addDock(dock_2d, 'above', dock_3d)

        self.plot_3d = Plot3DWidget(self.model_wrapper, dock_3d)
        dock_3d.addWidget(self.plot_3d)

        self.plot_2d = Plot2DWidget(self.model_wrapper, self.statusBar(), dock_2d)
        dock_2d.addWidget(self.plot_2d)

        self.plot_1d = Plot1DWidget(self.model_wrapper, self.statusBar(), dock_1d)
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

    def notify(self, name, value):
        if name == PreferenceEnum.SAVE_FILE.name and value is not None:
            self.setWindowTitle(os.path.basename(value).split(".")[0])
