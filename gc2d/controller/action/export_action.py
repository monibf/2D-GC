from PyQt5.QtWidgets import QAction

from gc2d.view.dialogs import ExportDialog


class ExportAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export', parent)
        self.window = parent
        self.model_wrapper = model_wrapper

        self.setShortcut('Ctrl+E')
        self.setStatusTip('Export 2D plot')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.show_dialog)

        self.model_wrapper.add_observer(self, self.notified)

    def show_dialog(self):
        """
        Shows the convolution picking dialog.
        :return: None
        """
        self.parent().addDialog(ExportDialog(self.window, self.model_wrapper))

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
