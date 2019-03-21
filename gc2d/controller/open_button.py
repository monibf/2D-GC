from PyQt5.QtWidgets import QAction, QFileDialog


class OpenButton(QAction):

    def __init__(self, window, model_wrapper):
        super().__init__('Open', window)
        self.window = window
        self. model_wrapper = model_wrapper
        self.setShortcut('Ctrl+O')
        self.setStatusTip('Open chromatography data')
        self.triggered.connect(self.show_dialog)

    def show_dialog(self):
        file_name = QFileDialog.getOpenFileName(self.window, 'Open chromatography data', '/home')

        if file_name[0]:
            self.model_wrapper.load_model(file_name[0])
