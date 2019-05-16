from PyQt5.QtWidgets import QAction, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QDoubleSpinBox, \
                  QPushButton


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

        self.dialog = QMainWindow(parent=None)
        self.dialog.setWindowTitle("Convolve")
        self.parent().dialogs.append(self.dialog)

        vbox = QWidget()
        self.dialog.setCentralWidget(vbox)

        vlayout = QVBoxLayout()
        vbox.setLayout(vlayout)

        type_lbl = QLabel('Convolution filter type:')
        vlayout.addWidget(type_lbl)

        radio_buttons = QWidget()
        vlayout.addWidget(radio_buttons)
        radio_button_layout = QHBoxLayout()
        radio_buttons.setLayout(radio_button_layout)


        self.gaussian_radio_button = QRadioButton('Gaussian', radio_buttons)
        self.gaussian_radio_button.toggled.connect(self.switch_params)
        radio_button_layout.addWidget(self.gaussian_radio_button)

        self.gaussian_params = QWidget()
        gaussian_params_layout = QVBoxLayout()
        self.gaussian_params.setLayout(gaussian_params_layout)
        vlayout.addWidget(self.gaussian_params)
        self.gaussian_params.setVisible(False)

        gaussian_sigma_label = QLabel('Sigma: ')
        self.gaussian_sigma = QDoubleSpinBox()
        self.gaussian_sigma.setMinimum(0)
        gaussian_sigma_label.setBuddy(self.gaussian_sigma)
        gsb = QWidget()
        gsl = QHBoxLayout()
        gsb.setLayout(gsl)
        gsl.addWidget(gaussian_sigma_label)
        gsl.addWidget(self.gaussian_sigma)
        gaussian_params_layout.addWidget(gsb)

        cancel_select = QWidget()
        vlayout.addWidget(cancel_select)
        cancel_select_layout = QHBoxLayout()
        cancel_select.setLayout(cancel_select_layout)

        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        cancel_select_layout.addWidget(cancel_button)

        select_button = QPushButton('Confirm')
        select_button.clicked.connect(self.confirm)
        cancel_select_layout.addWidget(select_button)
        self.dialog.show()

    def confirm(self):
        if self.gaussian_radio_button.isChecked():
            self.model_wrapper.filter_gaussian(self.gaussian_sigma.value())
        self.dialog.close()

    def close(self):
        self.parent().dialogs.remove(self.dialog)
        self.dialog.close()

    def switch_params(self):
        self.gaussian_params.setVisible(False)
        if self.gaussian_radio_button.isChecked():
            self.gaussian_params.setVisible(True)
