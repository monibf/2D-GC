import sys
from os import path
from shutil import copy

import numpy
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget, \
    QFileDialog, QSizePolicy, QDialog, QSpinBox, QComboBox, QDoubleSpinBox

import gc2d.main as main
from gc2d.model.preferences import ScaleEnum
from gc2d.model.time_unit import TimeUnit
from gc2d.view.palette.palette import palettes, load_custom_palettes


class EditAxes(QDialog):
    
    def __init__(self, parent, modelwrapper):
        """
        This window will open a palette chooser to let users select a palette from the (global) list of possible
        palettes.

        :param parent: The parent window, should be the current instance of MainWindow.
        :param modelwrapper: The wrapper of the model.
        """
        
        super().__init__(parent=parent)
        self.parent().addDialog(self)
        self.setWindowTitle("Choose Palette")

        self.modelwrapper = modelwrapper

        # vertical layout as central panel.
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

        options = QWidget()
        opts_layout = QVBoxLayout()
        options.setLayout(opts_layout)
        vlayout.addWidget(options)

        xbox = QWidget()
        xlayout = QHBoxLayout()
        xbox.setLayout(xlayout)
        vlayout.addWidget(xbox)

        xlayout.addWidget(QLabel("x axis:"))

        self.xPeriodField = QDoubleSpinBox()
        self.xPeriodField.setRange(0, float("inf"))
        self.xPeriodField.setValue(modelwrapper.get_preference(ScaleEnum.X_PERIOD))
        xlayout.addWidget(self.xPeriodField)

        self.xUnitField = QComboBox()
        for i, unit in enumerate(TimeUnit):
            self.xUnitField.addItem(unit.name.lower(), userData=unit)
            if modelwrapper.get_preference(ScaleEnum.X_UNIT) is unit:
                self.xUnitField.setCurrentIndex(i)
        xlayout.addWidget(self.xUnitField)

        ybox = QWidget()
        ylayout = QHBoxLayout()
        ybox.setLayout(ylayout)
        vlayout.addWidget(ybox)

        ylayout.addWidget(QLabel("y axis:"))
        self.yPeriodField = QDoubleSpinBox()
        self.yPeriodField.setRange(0, float("inf"))
        self.yPeriodField.setValue(modelwrapper.get_preference(ScaleEnum.Y_PERIOD))
        ylayout.addWidget(self.yPeriodField)

        self.yUnitField = QComboBox()
        for i, unit in enumerate(TimeUnit):
            self.yUnitField.addItem(unit.name.lower(), userData=unit)
            if modelwrapper.get_preference(ScaleEnum.Y_UNIT) is unit:
                self.yUnitField.setCurrentIndex(i)
        ylayout.addWidget(self.yUnitField)

        # add a button bar at the bottom.
        button_bar = QWidget()
        button_bar_layout = QHBoxLayout()
        button_bar.setLayout(button_bar_layout)
        vlayout.addWidget(button_bar)

        # add a cancel button.
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        button_bar_layout.addWidget(cancel_button)

        # add apply button.
        apply_button = QPushButton('Apply')
        apply_button.clicked.connect(self.apply)
        button_bar_layout.addWidget(apply_button)

        # add a ok button.
        ok_button = QPushButton('OK')
        ok_button.clicked.connect(self.ok)
        button_bar_layout.addWidget(ok_button)

    def ok(self):
        self.apply()
        self.close()

    def apply(self):
        self.modelwrapper.set_preference(ScaleEnum.X_PERIOD, self.xPeriodField.value())
        self.modelwrapper.set_preference(ScaleEnum.X_UNIT, self.xUnitField.currentData())
        self.modelwrapper.set_preference(ScaleEnum.Y_PERIOD, self.yPeriodField.value())
        self.modelwrapper.set_preference(ScaleEnum.Y_UNIT, self.yUnitField.currentData())

    # TODO is this function still necessary?
    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the top of the window."""
        event.accept()
        self.parent().dialogs.remove(self)
