
from PyQt5.QtWidgets import QAction

from gc2d.controller.dialogs.all_preferences import AllPreferences
from gc2d.controller.dialogs.palette_chooser import PaletteChooser


class OpenAllPreferencesAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A ChoosePaletteAction is a QAction that will open the choose palette dialog when opened.
        :param parent: the parent widget
        """
        super().__init__('Open Preferences', parent)
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+Shift+P')
        self.setStatusTip('Opens the preferences window')
        self.triggered.connect(self.show_dialog)

    # noinspection PyArgumentList
    def show_dialog(self):
        """
        Show the Choose Palette dialog.
        :return: None
        """
        i = -1
        while i == -1:
            i = AllPreferences(self.parent(), self.model_wrapper)
