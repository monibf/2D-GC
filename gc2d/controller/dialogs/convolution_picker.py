from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QDoubleSpinBox, \
    QPushButton, QComboBox, QSpinBox, QTextEdit

from gc2d.view.palette.palette import Palette

from gc2d.model.transformations import Transform, Gaussian, StaticCutoff, DynamicCutoff, Min1D
from gc2d.model.transformations.dynamiccutoff import CutoffMode

class ConvolutionPicker(QDialog):
    
    def __init__(self, model_wrapper):
        """
        This window will open a convolution picker to let users select a convolution.
        :param on_select: A callback function that is called when a convolution is selected.
            This callback wil get one or two arguments, depending on whether the gausian convolution is picked.
            The arguments need to be improved once we have more convolutions to choose from.
        :param on_close: A callback function that is called when the window closes. This function gets no arguments.
        """
        
        super().__init__(parent=None)
        
        self.model_wrapper = model_wrapper
        
        self.setWindowTitle("Transform data")

        self.vlayout = vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

        type_lbl = QLabel('Transformation type:')
        vlayout.addWidget(type_lbl)

        self.radio_buttons = QWidget()
        vlayout.addWidget(self.radio_buttons)
        self.radio_button_layout = QVBoxLayout()
        self.radio_buttons.setLayout(self.radio_button_layout)
        
        self.buttons = []
        
        # No transform
        self.add_button(Transform, "No Transform", "No transformation is linked under 'show transformed data' with this option.", [] ,checked=True)
        
        # Static cut-off
        self.add_button(StaticCutoff, "Static cut-off", "From each point in the graph, the given value is subtracted. The written value is one tenth of the upper bound of the color palette.", [_ParamDouble("cut-off value: ", value=self.model_wrapper.model.upper_bound/10)])
        
        # Dynamic cut-off
        self.add_button(
            DynamicCutoff,
            "Dynamic cut-off", 
            '''The dynamic cut-off transformation subtracts values from the data, depending on the slice over the y axis.
            The aim is to counteract base-line shift by only taking the lowest points along each slice, and subtract their value from the whole slice.
            \n The accounted percentage is how much of the lowest datapoints are taken into account when defining the cutoff point. There are two modes:
            The 'Mean' mode subtracts the mean of the lowest peaks of all points, the 'Max' mode subtracts the maximum value in the lowest points. ''',
            [
                _ParamDouble("Accounted percentage of the data: ", 0, 100),
                _ParamOption("Mode", [(CutoffMode.MEAN, "Mean"), (CutoffMode.QUANTILE, "Max")])
            ]
        )

        # Gaussian Convolution
        self.add_button(Gaussian, "Gaussian Convolution", "Convolves the data with a gaussian kernel" , [_ParamDouble("Sigma: ")])

        self.add_button(Min1D, "Min 1D Convolution", 
                               """
                               Slides a minimum filter of the specified size over the 1D chromatogram (summed 2D over the first dimension). 
                               This means that for each point in the 1D graph the specified number of adjoining/connected datapoints are assayed, 
                               and the minimum value between those points is subtracted from each point in the slice. Because the baseline is 
                               practically the same within each slice, the second dimension is not taken into account.
                               """,
                               [_ParamInt("Number of accounted slices: ")])


        cancel_select = QWidget()
        vlayout.addWidget(cancel_select)
        cancel_select_layout = QHBoxLayout()
        cancel_select.setLayout(cancel_select_layout)

        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        cancel_select_layout.addWidget(cancel_button)
        
        select_button = QPushButton('Apply')
        select_button.clicked.connect(self.select)
        cancel_select_layout.addWidget(select_button)

        select_button = QPushButton('Confirm')
        select_button.clicked.connect(self.select_and_close)
        cancel_select_layout.addWidget(select_button)
    
    def add_button(self, transform_type, label, info, parameters, checked=False):
        
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

        info_label = QTextEdit(info) 
        info_label.setReadOnly(True)
        params_layout.addWidget(info_label)

        for param in parameters:
            label = QLabel(param.label)
            label.setBuddy(param.selector)
            gsb = QWidget()
            gsl = QHBoxLayout()
            gsb.setLayout(gsl)
            gsl.addWidget(label)
            gsl.addWidget(param.selector)
            params_layout.addWidget(gsb)
        
        self.buttons.append(_Button(transform_type, radio_button, param_area, parameters))
        

    def switch_params(self):
        for button in self.buttons:
            button.param_area.setVisible(False)
        for button in self.buttons:
            button.param_area.setVisible(button.radio_button.isChecked())
        
        
    def select(self):
        for button in self.buttons:
            if button.radio_button.isChecked():
                parameters = [param.get_value() for param in button.parameters]
                transform = button.transform_type(*parameters)
                self.model_wrapper.set_transform(transform)
    
    def select_and_close(self):
        self.select()
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

class _ParamDouble:
    
    def __init__(self, label, minimum=0, maximum=float('inf'), value=0):
        self.label = label
        self.selector = QDoubleSpinBox()
        self.selector.setMinimum(minimum)
        self.selector.setMaximum(maximum)
        self.selector.setValue(value)
    
    def get_value(self):
        return self.selector.value()

class _ParamInt:
    
    def __init__(self, label, minimum=0, maximum=(2**31-1)):
        self.label = label
        self.selector = QSpinBox()
        self.selector.setMinimum(minimum)
        self.selector.setMaximum(maximum)
    
    def get_value(self):
        return self.selector.value()

class _ParamOption:
    
    def __init__(self, label, options):
        self.label = label
        self.selector = QComboBox()
        self.text_to_value = {}
        for option in options:
            if isinstance(option, str):
                option = (option, option)
            value, text = option
            self.selector.addItem(text)
            self.text_to_value[text] = value
    
    def get_value(self):
        return self.text_to_value[self.selector.currentText()]


