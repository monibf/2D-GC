import sys
from shutil import copy

import numpy
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget, \
    QFileDialog, QSizePolicy, QDialog, QSpinBox

import gc2d.main as main
from gc2d.view.palette.palette import palettes, load_custom_palettes


class PaletteChooser(QDialog):
    
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
        self.setFixedSize(300, 400)
        # add a list widget to view all the pretty palettes.
        self.list = QListWidget()
        self.list.setSelectionMode(1)
        vlayout.addWidget(self.list)

        options = QWidget()
        opts_layout = QVBoxLayout()
        options.setLayout(opts_layout)
        vlayout.addWidget(options)

        ubox = QWidget()
        ulayout = QHBoxLayout()
        ubox.setLayout(ulayout)
        vlayout.addWidget(ubox)

        ulayout.addWidget(QLabel("upper bound:"))
        self.upperBoundField = QSpinBox()
        self.upperBoundField.setRange(-2147483648, 2147483647)
        self.upperBoundField.setValue(modelwrapper.model.upper_bound)
        self.upperBoundField.setSingleStep((modelwrapper.model.highest-modelwrapper.model.lowest)/1000)
        ulayout.addWidget(self.upperBoundField)

        lbox = QWidget()
        llayout = QHBoxLayout()
        lbox.setLayout(llayout)
        vlayout.addWidget(lbox)

        llayout.addWidget(QLabel("lower bound:"))
        self.lowerBoundField = QSpinBox()
        self.lowerBoundField.setRange(-2147483648, 2147483647)
        self.lowerBoundField.setValue(modelwrapper.model.lower_bound)
        self.lowerBoundField.setSingleStep(1)
        llayout.addWidget(self.lowerBoundField)

        # add a button bar at the bottom.
        button_bar = QWidget()
        button_bar_layout = QHBoxLayout()
        button_bar.setLayout(button_bar_layout)
        vlayout.addWidget(button_bar)

        # add a cancel button.
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        button_bar_layout.addWidget(cancel_button)

        # add import palette button
        import_button = QPushButton('Import')
        import_button.clicked.connect(self.import_palette)
        button_bar_layout.addWidget(import_button)

        # add apply button.
        apply_button = QPushButton('Apply')
        apply_button.clicked.connect(self.apply)
        button_bar_layout.addWidget(apply_button)

        # add a ok button.
        ok_button = QPushButton('OK')
        ok_button.clicked.connect(self.ok)
        button_bar_layout.addWidget(ok_button)

        self.gen_palette_list()

    def gen_palette_list(self):
        self.list.clear()
        for i, palt in enumerate(palettes):
            item = QListWidgetItem(self.list)
            # item.setBackground(QtCore.Qt.red)

            widg = QWidget()
            # widg.setStyleSheet("background-color:blue")
            layo = QHBoxLayout()
            self.list.setItemWidget(item, widg)
            text = QLabel(palt.name)
            text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

            grad = QLabel()
            grad.setScaledContents(True)
            grad.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            grad.setPixmap(QPixmap(palt.generate_preview(width=100, height=1)))
            # grad.setStyleSheet("background-color:green")

            layo.addWidget(text)
            layo.addWidget(grad)

            widg.setLayout(layo)
            widg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

            item.setSizeHint(widg.sizeHint())
            if self.modelwrapper.get_palette() is palt:
                self.list.setCurrentRow(i)

    def import_palette(self):
        files, _ = QFileDialog.getOpenFileNames(None, "Import palette file", "",
                                                "Palette Files (*.palette);;All Files(*)")
        loaded = []
        for file in files:
            loaded.extend(load_custom_palettes(file))

        self.gen_palette_list()

        for file in loaded:
            copy(file, main.CUSTOM_PALETTE_PATH)
        self.close()
        PaletteChooser(self.parent(), self.modelwrapper)

    def ok(self):
        self.apply()
        self.close()

    def apply(self):
        index = self.list.currentRow()
        self.modelwrapper.set_palette(palettes[index])
        self.modelwrapper.set_lower_bound(self.lowerBoundField.value())
        self.modelwrapper.set_upper_bound(self.upperBoundField.value())

    # TODO is this function still necessary?
    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the top of the window."""
        event.accept()
        self.parent().dialogs.remove(self)
