from PyQt5.QtWidgets import QAction, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel, QHBoxLayout, \
    QLayout, QListWidgetItem

from gc2d.view.palette import palette


class OpenChoosePaletteAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        A ChoosePaletteAction is a QAction that will open the choose palette dialog when opened.
        :param parent: the parent widget
        """
        super().__init__('Choose Palette', parent)
        self.model_wrapper = model_wrapper
        self.dialog = None
        self.list = None
        self.setShortcut('Ctrl+Shift+C')
        self.setStatusTip('Opens the Choose Palette Dialog')
        self.triggered.connect(self.show_dialog)

    # noinspection PyArgumentList
    def show_dialog(self):
        """
        Show the Choose Palette dialog.
        :return: None
        """

        self.dialog = QMainWindow(parent=None)
        self.dialog.setWindowTitle("Choose Palette")
        self.parent().dialogs.append(self.dialog)

        vbox = QWidget()
        self.dialog.setCentralWidget(vbox)

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

        for palt in palette.palettes:
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
        self.dialog.show()

    def select(self):
        index = self.list.currentRow()
        self.model_wrapper.set_palette(palette.palettes[index])
        self.dialog.close()

    def close(self):
        self.parent().dialogs.remove(self.dialog)
        self.dialog.close()

