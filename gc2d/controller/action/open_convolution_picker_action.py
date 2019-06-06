from PyQt5.QtWidgets import QAction
from gc2d.view.dialogs.convolution_picker import ConvolutionPicker


class OpenConvolutionPickerAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        An OpenConvolutionPickerAction is a QAction that opens a dialog to select convolutions to be performed on the data.
        It currently supports Gaussian filters.
        :param parent: The parent widget
        :param model_wrapper: The model wrapper
        """
        super().__init__('Set Transformation', parent)
        self.model_wrapper = model_wrapper
        self.dialog = None
        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setEnabled(self.model_wrapper.model is not None)
        self.model_wrapper.add_observer(self, self.notify)
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Shows the convolution picking dialog.
        :return: None
        """

        self.parent().addDialog(ConvolutionPicker(self.model_wrapper))

    def notify(self, name, value):
        if name == 'model':
            self.setEnabled(value is not None)
