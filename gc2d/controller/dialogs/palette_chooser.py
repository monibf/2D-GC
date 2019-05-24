from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QListWidget, QListWidgetItem, QMainWindow, \
    QPushButton, QVBoxLayout, QWidget, QFileDialog

from shutil import copy

import gc2d.main as main
from gc2d.view.palette.palette import Palette


class PaletteChooser(QMainWindow):
    
    def __init__(self, on_select):
        """
        This window will open a palettle chooser to let users select a palette from the (global) list of possible palettes.
        :param on_select: A callback function that is called when a palette is selected.
            This callback wil get one argument which is the palette that is selected.
        :param on_close: A callback function that is called when the window closes. This function gets no arguments.
        """
        
        super().__init__(parent=None)
        self.setWindowTitle("Choose Palette")

        self.on_select = on_select

        # vertical layout as central panel.
        vbox = QWidget()
        vlayout = QVBoxLayout()
        self.setCentralWidget(vbox)
        vbox.setLayout(vlayout)

        # add a list widget to view all the pretty palettes.
        self.list = QListWidget()
        self.list.setSelectionMode(1)
        vlayout.addWidget(self.list)

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

        # add a select button.
        select_button = QPushButton('Confirm')
        select_button.clicked.connect(self.select)
        button_bar_layout.addWidget(select_button)

        self.gen_paletteList()

    def gen_paletteList(self):
        self.list.clear()
        for palt in Palette.palettes:
            item = QListWidgetItem()
            widg = QWidget()
            text = QLabel(palt.name)
            grad = QLabel('placeholder')
            layo = QHBoxLayout()
            layo.addWidget(text)
            layo.addWidget(grad)
            layo.addStretch()

            layo.setSizeConstraint(QLayout.SetFixedSize)
            widg.setLayout(layo)
            item.setSizeHint(widg.sizeHint())

            self.list.addItem(item)
            self.list.setItemWidget(item, widg)

    def import_palette(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Import palette file", "",
                                                "Palette Files (*.palette);;All Files(*)")
        loaded = []
        for file in files:
            loaded.extend(Palette.load_custom_palettes(file))

        self.gen_paletteList()

        for file in loaded:
            copy(file, main.CUSTOM_PALETTE_PATH)

    def select(self):
        index = self.list.currentRow()
        self.on_select(Palette.palettes[index])
        self.close()

    # TODO is this function still necessary?
    def closeEvent(self, event):
        """ Overrides the closing event to execute the on_close callback after closing.
        This is better than overriding close() because this will also execute when the user presses the x button on the top of the window."""
        event.accept()
