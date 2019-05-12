from PyQt5.QtWidgets import QAction, QFileDialog
import os.path
import pickle

class OpenFileAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An OpenFileAction is a QAction that when triggered, opens a QFileDialog to select chromatogram data to open. The
        file name is passed to the model_wrapper to load the data into the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Open New', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.setShortcut('Ctrl+O')
        self.setStatusTip('Open chromatography data')
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Show the Open file dialog.
        :return: None
        """
        # noinspection PyArgumentList
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data', filter='2D-GC data (*.txt *.csv);; GCxGC files (*.gcgc)')
        if not file_name[0]:
            return
        extension = os.path.splitext(file_name[0])[1]
        if extension == ".txt" or extension == ".csv": 
            self.model_wrapper.load_model(file_name[0])
        if extension == ".gcgc":
            file = open(file_name[0], 'rb')
            model, integrations = pickle.load(file)
            self.model_wrapper.model = model
            for key in integrations:
                print(integrations[key][0], integrations[key][1])