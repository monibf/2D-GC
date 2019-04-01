from PyQt5.QtWidgets import QAction, QFileDialog


class OpenButton:

    def __init__(self, parent, model_wrapper):
        """
        An OpenButton has a QAction that when triggered, opens a QFileDialog to select chromatogram data to open. The
        file name is passed to the model_wrapper to load the data into the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        self.button = QAction('Open', parent)
        self.window = parent
        self. model_wrapper = model_wrapper
        self.button.setShortcut('Ctrl+O')
        self.button.setStatusTip('Open chromatography data')
        self.button.triggered.connect(self.show_dialog)

    def show_dialog(self):
        """
        Show the Open file dialog.
        :return: None
        """
        # noinspection PyArgumentList
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data')

        if file_name[0]:
            self.model_wrapper.load_model(file_name[0])
