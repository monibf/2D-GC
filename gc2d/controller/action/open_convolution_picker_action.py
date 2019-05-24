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
        super().__init__('Set Convolution', parent)
        self.model_wrapper = model_wrapper
        self.dialog = None
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Shows the convolution picking dialog.
        :return: None
        """

       
        self.parent().addDialog(ConvolutionPicker(self.on_select))

    def on_select(self, transform):
        self.model_wrapper.set_transform(transform)

