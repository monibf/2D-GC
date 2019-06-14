from PyQt5.QtWidgets import QAction

from gc2d.view.dialogs.export_dialog import ExportDialog


class ExportAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setStatusTip('Export')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.show_dialog)

        self.model_wrapper.add_observer(self, self.notified)

    def show_dialog(self):
        """
        Shows the convolution picking dialog.
        :return: None
        """
        self.parent().add_dialog(ExportDialog(self.window, self.model_wrapper))

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
