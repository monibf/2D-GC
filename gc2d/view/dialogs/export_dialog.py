from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget

from gc2d.controller.action.export_plot_2d_action import ExportPlot2DAction
from gc2d.controller.action.export_plot_3d_action import ExportPlot3DAction


class ExportDialog(QDialog):

    def __init__(self, main_window, model_wrapper):
        """
        Let users select the plot to export.
        """

        super().__init__(parent=None)

        self.export_2d = ExportPlot2DAction(main_window, model_wrapper)
        self.export_3d = ExportPlot3DAction(main_window, model_wrapper)

        self.setWindowTitle("Export plot")

        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

        type_lbl = QLabel('Export Plot')
        self.vlayout.addWidget(type_lbl)

        self.radio_buttons = QWidget()
        self.vlayout.addWidget(self.radio_buttons)
        self.radio_button_layout = QVBoxLayout()
        self.radio_buttons.setLayout(self.radio_button_layout)

        self.buttons = []

        # No transform
        self.radio_2d = QRadioButton("2D plot", self.radio_buttons)
        self.radio_2d.setChecked(True)

        self.radio_3d = QRadioButton("3D plot", self.radio_buttons)

        self.radio_button_layout.addWidget(self.radio_2d)
        self.radio_button_layout.addWidget(self.radio_3d)

        select_button = QPushButton('Select')
        select_button.clicked.connect(self.export_selected_plot)

        self.vlayout.addWidget(select_button)

    def export_selected_plot(self):

        self.close()

        if self.radio_2d.isChecked():
            self.export_2d.export_plot()

        elif self.radio_3d.isChecked():
            self.export_3d.export_plot()

        else:
            print("Unknown plot type")
