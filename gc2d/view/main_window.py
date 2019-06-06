import os.path

from PyQt5.QtWidgets import QMainWindow
from pyqtgraph.dockarea import Dock, DockArea

from gc2d.controller.action.draw_action import DrawAction
from gc2d.controller.action.exit_action import ExitAction
from gc2d.controller.action.export_action import ExportAction
from gc2d.controller.action.export_plot_2d_action import ExportPlot2DAction
from gc2d.controller.action.export_plot_3d_action import ExportPlot3DAction
from gc2d.controller.action.import_data_action import ImportDataAction
from gc2d.controller.action.open_choose_palette_action import OpenChoosePaletteAction
from gc2d.controller.action.open_convolution_picker_action import OpenConvolutionPickerAction
from gc2d.controller.action.open_edit_axes_action import OpenEditAxesAction
from gc2d.controller.action.open_file_action import OpenFileAction
from gc2d.controller.action.save_action import SaveAction
from gc2d.controller.action.save_as_action import SaveAsAction
from gc2d.controller.action.save_integrations_action import SaveIntegrationsAction
from gc2d.controller.action.save_prefs_action import SavePrefsAction
from gc2d.controller.action.toggle_convolution_action import ToggleConvolutionAction
from gc2d.model.preferences import PreferenceEnum
from gc2d.view.integration_list import IntegrationList
from gc2d.view.plot_1d_widget import Plot1DWidget
from gc2d.view.plot_2d_widget import Plot2DWidget
from gc2d.view.plot_3d_widget import Plot3DWidget

# FILE
SHORTCUT_OPEN = 'Ctrl+O'
SHORTCUT_IMPORT = 'Ctrl+I'
SHORTCUT_SAVE = 'Ctrl+S'
SHORTCUT_SAVE_AS = 'Ctrl+Shift+S'
SHORTCUT_SAVE_INTEGRATIONS = None
SHORTCUT_SAVE_PREFERENCES = None
SHORTCUT_EXPORT_3D = 'Ctrl+T'
SHORTCUT_EXPORT_2D = 'Ctrl+R'
SHORTCUT_EXIT = 'Ctrl+Q'

# EDIT
SHORTCUT_DRAW = 'Ctrl+D'
SHORTCUT_EDIT_AXES = None

# VIEW
SHORTCUT_CHOOSE_PALETTE = 'Ctrl+Shift+C'
SHORTCUT_TOGGLE_CONVOLUTION = None

# TOOLS
SHORTCUT_CHOOSE_CONVOLUTION = None


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
        """The list of open dialogs."""

        self.toolbar = self.addToolBar("toolbar")
        """The toolbar."""

        self.plot_1d = None
        """The Plot1DWidget."""
        self.plot_2d = None
        """The Plot2DWidget."""
        self.plot_3d = None
        """The Plot3DWidget."""

        # add this as an observer
        model_wrapper.add_observer(self, self.notify)

        # init the window settings.
        self.resize(500, 500)
        self.setWindowTitle('GCxGC')

        # create UI elements.
        self.create_menus()  # Create the menus in the menu bar.
        self.create_toolbar()  # Create the toolbar.
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
        file_menu.addAction(OpenFileAction(self, self.model_wrapper, SHORTCUT_OPEN))

        file_menu.addAction(ImportDataAction(self, self.model_wrapper, SHORTCUT_IMPORT))
        file_menu.addAction(SaveAction(self, self.model_wrapper, SHORTCUT_SAVE))
        file_menu.addAction(SaveAsAction(self, self.model_wrapper, SHORTCUT_SAVE_AS))
        file_menu.addAction(SaveIntegrationsAction(self, self.model_wrapper, SHORTCUT_SAVE_INTEGRATIONS))
        file_menu.addAction(SavePrefsAction(self, self.model_wrapper, SHORTCUT_SAVE_PREFERENCES))

        file_menu.addSeparator()
        file_menu.addAction(ExportPlot2DAction(self, self.model_wrapper, SHORTCUT_EXPORT_2D))
        file_menu.addAction(ExportPlot3DAction(self, self.model_wrapper, SHORTCUT_EXPORT_3D))

        file_menu.addAction(ExitAction(self, SHORTCUT_EXIT))

        edit_menu = main_menu.addMenu('Edit')
        edit_menu.addAction(DrawAction(self, self.model_wrapper, SHORTCUT_DRAW))
        edit_menu.addAction(OpenEditAxesAction(self, self.model_wrapper, SHORTCUT_EDIT_AXES))

        view_menu = main_menu.addMenu('View')
        view_menu.addAction(OpenChoosePaletteAction(self, self.model_wrapper, SHORTCUT_CHOOSE_PALETTE))
        view_menu.addAction(ToggleConvolutionAction(self, self.model_wrapper, SHORTCUT_TOGGLE_CONVOLUTION))

        tools_menu = main_menu.addMenu('Tools')
        tools_menu.addAction(OpenConvolutionPickerAction(self, self.model_wrapper, SHORTCUT_CHOOSE_CONVOLUTION))
        # TODO

        help_menu = main_menu.addMenu('Help')
        # TODO

    def create_toolbar(self):
        """
        Creates the toolbar.
        :return: None
        """
        self.toolbar.addAction(ToggleConvolutionAction(self, self.model_wrapper))
        self.toolbar.addAction(OpenConvolutionPickerAction(self, self.model_wrapper))
        self.toolbar.addAction(OpenChoosePaletteAction(self, self.model_wrapper))
        self.toolbar.addAction(DrawAction(self, self.model_wrapper))
        self.toolbar.addAction(ExportAction(self, self.model_wrapper))

    # noinspection PyArgumentList
    def create_graph_views(self):
        """
        Creates the window containing the graph views.
        :return: None
        """
        dock_area = DockArea()
        self.setCentralWidget(dock_area)

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

    def add_dialog(self, dialog):
        """
        Adds a dialog to the view. This is so they don't get destroyed by QT's dumb garbage collector.
        Rather than allowing multiple dialogs to be opened, if a dialog of a specific type is already open it
        will focus that dialog and forget about the new one.
        :param dialog: The dialog to add (or focus)
        :return: None
        """
        for d in self.dialogs:
            if isinstance(d, type(dialog)):
                d.show()
                d.raise_()
                d.activateWindow()
                d.showNormal()
                return

        dialog.show()  # Make the dialog visible.
        dialog.raise_()  # Raise it above all other windows.
        dialog.activateWindow()  # Give it focus.
        dialog.showNormal()  # Unminimise it.
        self.dialogs.append(dialog)

    def notify(self, name, value):
        """Called when the model updates. Used to set the window name."""
        if name == PreferenceEnum.SAVE_FILE.name and value is not None:
            self.setWindowTitle(os.path.basename(value).split(".")[0])
