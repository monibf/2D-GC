from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget

from gc2d.controller.action.export_plot_1d_action import ExportPlot1DAction
from gc2d.controller.action.export_plot_2d_action import ExportPlot2DAction
from gc2d.controller.action.export_plot_3d_action import ExportPlot3DAction
from gc2d.controller.action.export_integration_list import ExportIntegrationAction


class ExportDialog(QDialog):

    def __init__(self, main_window, model_wrapper):
        """
        Let users select which data to export.
        """

        super().__init__(parent=None)

        self.export_1d = ExportPlot1DAction(main_window, model_wrapper)
        self.export_2d = ExportPlot2DAction(main_window, model_wrapper)
        self.export_3d = ExportPlot3DAction(main_window, model_wrapper)
        self.export_integrations = ExportIntegrationAction(main_window, model_wrapper)

        self.setWindowTitle("Export")

        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

        type_lbl = QLabel('Export')
        self.vlayout.addWidget(type_lbl)

        self.radio_buttons = QWidget()
        self.vlayout.addWidget(self.radio_buttons)
        self.radio_button_layout = QVBoxLayout()
        self.radio_buttons.setLayout(self.radio_button_layout)

        self.buttons = []

        self.radio_1d = QRadioButton("1D plot", self.radio_buttons)
        self.radio_2d = QRadioButton("2D plot", self.radio_buttons)
        self.radio_3d = QRadioButton("3D plot", self.radio_buttons)
        self.radio_export_integrations = QRadioButton("Integrations", self.radio_buttons)

        self.radio_1d.setChecked(True)

        self.radio_button_layout.addWidget(self.radio_1d)
        self.radio_button_layout.addWidget(self.radio_2d)
        self.radio_button_layout.addWidget(self.radio_3d)
        self.radio_button_layout.addWidget(self.radio_export_integrations)

        select_button = QPushButton('Select')
        select_button.clicked.connect(self.export_selected_plot)

        self.vlayout.addWidget(select_button)

    def export_selected_plot(self):

        self.close()

        if self.radio_1d.isChecked():
            self.export_1d.export_plot()

        elif self.radio_2d.isChecked():
            self.export_2d.export_plot()

        elif self.radio_3d.isChecked():
            self.export_3d.export_plot()

        elif self.radio_export_integrations.isChecked():
            self.export_integrations.export_integration_list()

        else:
            print("Unknown plot type")
