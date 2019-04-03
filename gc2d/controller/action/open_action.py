from PyQt5.QtWidgets import QAction, QFileDialog


class OpenAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        An OpenAction is a QAction that when triggered, opens a QFileDialog to select chromatogram data to open. The
        file name is passed to the model_wrapper to load the data into the model.
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Open', parent)
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
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data')

        if file_name[0]:
            self.model_wrapper.load_model(file_name[0])
