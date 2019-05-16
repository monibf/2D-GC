from PyQt5.QtWidgets import QAction
from gc2d.controller.dialogs.convolution_picker import ConvolutionPicker


class OpenConvolutionPickerAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An OpenConvolutionPickerAction is a QAction that opens a dialog to select convolutions to be performed on the data.
        It currently supports Gaussian filters.
        :param parent: The parent widget
        :param model_wrapper: The model wrapper
        """
        super().__init__('Convolve...', parent)
        self.model_wrapper = model_wrapper
        self.dialog = None
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Shows the convolution picking dialog.
        :return: None
        """

       
        if self.dialog is None:
            self.dialog = ConvolutionPicker(self.on_select, self.on_close)
            self.parent().dialogs.append(self.dialog)
        
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()

    def on_select(self, is_gaussian, gaussian_sigma=None):
        if is_gaussian:
            self.model_wrapper.filter_gaussian(gaussian_sigma)

    def on_close(self):
        self.parent().dialogs.remove(self.dialog)
        self.dialog = None
