from PyQt5.QtWidgets import QAction, QFileDialog
import os.path
import numpy as np
import json
from gc2d.controller.integration.selector import Selector

class ImportDataAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An OpenFileAction is a QAction that when triggered, opens a QFileDialog to select chromatogram data to open. The
        file name is passed to the model_wrapper to load the data into the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Import data', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+I')
        self.setStatusTip('Import chromatography data')
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Show the Open file dialog.
        :return: None
        """
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data', filter='2D-GC data (*.txt *.csv)')
        if file_name[0]:
            self.model_wrapper.import_model(file_name[0])
