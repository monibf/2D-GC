from PyQt5.QtWidgets import QAction

from gc2d.view.dialogs.palette_chooser import PaletteChooser


class OpenChoosePaletteAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        A ChoosePaletteAction is a QAction that will open the choose palette dialog when opened.
        :param parent: the parent widget
        """
        super().__init__('Choose Palette', parent)
        self.model_wrapper = model_wrapper

        self.setStatusTip('Opens the Choose Palette Dialog')
        self.setEnabled(self.model_wrapper.model is not None)

        if shortcut is not None:
            self.setShortcut(shortcut)

        self.triggered.connect(self.show_dialog)

        self.model_wrapper.add_observer(self, self.notify)

    # noinspection PyArgumentList
    def show_dialog(self):
        """
        Show the Choose Palette dialog.
        :return: None
        """
        self.parent().add_dialog(PaletteChooser(self.parent(), self.model_wrapper))

    def notify(self, name, value):
        if name == 'model':
            self.setEnabled(value is not None)
