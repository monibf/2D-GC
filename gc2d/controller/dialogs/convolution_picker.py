from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QDoubleSpinBox, \
    QPushButton

from gc2d.view.palette.palette import Palette

from gc2d.model.transformations import Transform, Gaussian, StaticCutoff

class ConvolutionPicker(QMainWindow):
    
    def __init__(self, on_select):
        """
        This window will open a convolution picker to let users select a convolution.
        :param on_select: A callback function that is called when a convolution is selected.
            This callback wil get one or two arguments, depending on whether the gausian convolution is picked.
            The arguments need to be improved once we have more convolutions to choose from.
        :param on_close: A callback function that is called when the window closes. This function gets no arguments.
        """
        
        super().__init__(parent=None)
        
        self.on_select = on_select
        
        self.setWindowTitle("Convolve")

        vbox = QWidget()
        self.setCentralWidget(vbox)

        vlayout = QVBoxLayout()
        vbox.setLayout(vlayout)

        type_lbl = QLabel('Convolution filter type:')
        vlayout.addWidget(type_lbl)

        radio_buttons = QWidget()
        vlayout.addWidget(radio_buttons)
        radio_button_layout = QVBoxLayout()
        radio_buttons.setLayout(radio_button_layout)
        
        # No transform
        self.none_radio_button = QRadioButton('No transform')
        self.none_radio_button.setChecked(True)
        self.none_radio_button.toggled.connect(self.switch_params)
        radio_button_layout.addWidget(self.none_radio_button)
        
        # Static cut-off
        self.cutoff_radio_button = QRadioButton('Static cut-off', radio_buttons)
        self.cutoff_radio_button.toggled.connect(self.switch_params)
        radio_button_layout.addWidget(self.cutoff_radio_button)

        self.cutoff_params = QWidget()
        cutoff_params_layout = QVBoxLayout()
        self.cutoff_params.setLayout(cutoff_params_layout)
        vlayout.addWidget(self.cutoff_params)
        self.cutoff_params.setVisible(False)

        cutoff_value_label = QLabel('cut-off value: ')
        self.cutoff_value = QDoubleSpinBox()
        self.cutoff_value.setMinimum(0)
        self.cutoff_value.setMaximum(float('inf'))
        cutoff_value_label.setBuddy(self.cutoff_value)
        gsb = QWidget()
        gsl = QHBoxLayout()
        gsb.setLayout(gsl)
        gsl.addWidget(cutoff_value_label)
        gsl.addWidget(self.cutoff_value)
        cutoff_params_layout.addWidget(gsb)

        # Gaussian Convolution
        self.gaussian_radio_button = QRadioButton('Gaussian Convolution', radio_buttons)
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
        select_button.clicked.connect(self.select)
        cancel_select_layout.addWidget(select_button)
	
	

    def switch_params(self):
        self.gaussian_params.setVisible(False)
        if self.gaussian_radio_button.isChecked():
            self.gaussian_params.setVisible(True)
        
        self.cutoff_params.setVisible(False)
        if self.cutoff_radio_button.isChecked():
            self.cutoff_params.setVisible(True)
        
    def select(self):
        if self.none_radio_button.isChecked():
            self.on_select(Transform())
        elif self.gaussian_radio_button.isChecked():
            self.on_select(Gaussian(self.gaussian_sigma.value()))
        elif self.cutoff_radio_button.isChecked():
            self.on_select(StaticCutoff(self.cutoff_value.value()))
        self.close()


    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the top of the window."""
        event.accept()
    

