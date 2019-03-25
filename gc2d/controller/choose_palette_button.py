from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QAction, QMainWindow, QVBoxLayout, QWidget, QPushButton


class QButton(object):
    pass


class IntegrateButton(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An IntegrateButton is a QAction that will open the integration dialog when opened.
        :param parent: the parent widget
        """
        super().__init__('Integrate', parent)
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+I')
        self.setStatusTip('Opens the Integration Dialog')
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Show the integration dialog.
        :return: None
        """
        dialog = QMainWindow(parent=None)
        dialog.setWindowTitle("Integrate")
        self.parent().dialogs.append(dialog)

        vbox = QWidget()
        dialog.setCentralWidget(vbox)

        vlayout = QVBoxLayout()
        vbox.setLayout(vlayout)

        select_region = QPushButton("Select region")
        select_region.clicked.connect(self.select_region)
        vlayout.addWidget(select_region)

        intergrate = QPushButton("Intergrate")
        vlayout.addWidget(intergrate)

        dialog.show()
        print('dialog opened?')

    def select_region(self):
        self.model_wrapper.set_selecting(True)
