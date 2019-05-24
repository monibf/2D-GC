from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QDoubleSpinBox, \
    QPushButton

from gc2d.view.palette.palette import Palette

from gc2d.model.transformations import Transform, Gaussian, StaticCutoff, DynamicCutoff

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

        self.vlayout = vlayout = QVBoxLayout()
        vbox.setLayout(self.vlayout)

        type_lbl = QLabel('Convolution filter type:')
        vlayout.addWidget(type_lbl)

        self.radio_buttons = QWidget()
        vlayout.addWidget(self.radio_buttons)
        self.radio_button_layout = QVBoxLayout()
        self.radio_buttons.setLayout(self.radio_button_layout)
        
        self.buttons = []
        
        # No transform
        self.add_button(Transform, "No Transform", [], checked=True)
        
        # Static cut-off
        cutoff_value = QDoubleSpinBox()
        cutoff_value.setMinimum(0)
        cutoff_value.setMaximum(float('inf'))
        self.add_button(StaticCutoff, "Static cut-off", [("cut-off value: ", cutoff_value)])
        
        # Dynamic cut-off
        quantile = QDoubleSpinBox()
        quantile.setMinimum(0)
        quantile.setMaximum(100)
        self.add_button(DynamicCutoff, "Dynamic cut-off", [("base percentile: ", quantile)])

        # Gaussian Convolution
        gaussian_sigma = QDoubleSpinBox()
        gaussian_sigma.setMinimum(0)
        self.add_button(Gaussian, "Gaussian Convolution", [("Sigma: ", gaussian_sigma)])

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
    
    def add_button(self, transform_type, label, parameters, checked=False):
        
        radio_button = QRadioButton(label, self.radio_buttons)
        if checked:
            radio_button.setChecked(True)
        radio_button.toggled.connect(self.switch_params)
        self.radio_button_layout.addWidget(radio_button)

        param_area = QWidget()
        params_layout = QVBoxLayout()
        param_area.setLayout(params_layout)
        self.vlayout.addWidget(param_area)
        param_area.setVisible(False)

        params = []
        for description, selector in parameters:
            label = QLabel(description)
            label.setBuddy(selector)
            gsb = QWidget()
            gsl = QHBoxLayout()
            gsb.setLayout(gsl)
            gsl.addWidget(label)
            gsl.addWidget(selector)
            params_layout.addWidget(gsb)
            params.append(selector)
        
        self.buttons.append(_Button(transform_type, radio_button, param_area, params))
        

    def switch_params(self):
        for button in self.buttons:
            button.param_area.setVisible(False)
        for button in self.buttons:
            button.param_area.setVisible(button.radio_button.isChecked())
        
    def select(self):
        for button in self.buttons:
            if button.radio_button.isChecked():
                parameters = [param.value() for param in button.parameters]
                transform = button.transform_type(*parameters)
                self.on_select(transform)
                
        self.close()


    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the top of the window."""
        event.accept()
    


class _Button:
    
    def __init__(self, transform_type, radio_button, param_area, parameters):
        self.radio_button = radio_button
        self.transform_type = transform_type
        self.param_area = param_area
        self.parameters = parameters
