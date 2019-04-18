
from PyQt5.QtWidgets import QAction

from gc2d.controller.dialogs.palette_chooser import PaletteChooser

class OpenChoosePaletteAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A ChoosePaletteAction is a QAction that will open the choose palette dialog when opened.
        :param parent: the parent widget
        """
        super().__init__('Choose Palette', parent)
        self.model_wrapper = model_wrapper
        self.dialog = None
        self.setShortcut('Ctrl+Shift+C')
        self.setStatusTip('Opens the Choose Palette Dialog')
        self.triggered.connect(self.show_dialog)

    # noinspection PyArgumentList
    def show_dialog(self):
        """
        Show the Choose Palette dialog.
        :return: None
        """
        
        if self.dialog is None:
            self.dialog = PaletteChooser(self.on_select, self.on_close)
            self.parent().dialogs.append(self.dialog)
        
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()

    def on_select(self, palette):
        self.model_wrapper.set_palette(palette)

    def on_close(self):
        self.parent().dialogs.remove(self.dialog)
        self.dialog = None
