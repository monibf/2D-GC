from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QListWidget, QListWidgetItem, QMainWindow, \
    QPushButton, QVBoxLayout, QWidget

from gc2d.view.palette.palette import Palette

class PaletteChooser(QMainWindow):
    
    def __init__(self, on_select, on_close):
        """
        This window will open a palettle chooser to let users select a palette from the (global) list of possible palettes.
        :param on_select: A callback function that is called when a palette is selected.
            This callback wil get one argument which is the palette that is selected.
        :param on_close: A callback function that is called when the window closes. This function gets no arguments.
        """
        
        super().__init__(parent=None)
        self.setWindowTitle("Choose Palette")
        
        self.on_select = on_select
        self.on_close = on_close

        vbox = QWidget()
        self.setCentralWidget(vbox)

        vlayout = QVBoxLayout()
        vbox.setLayout(vlayout)

        self.list = QListWidget()
        self.list.setSelectionMode(1)
        vlayout.addWidget(self.list)
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
        self.show()
        
    def select(self):
        index = self.list.currentRow()
        self.on_select(Palette.palettes[index])
        self.close()


    def closeEvent(self, event):
        self.on_close()
        event.accept()
    

