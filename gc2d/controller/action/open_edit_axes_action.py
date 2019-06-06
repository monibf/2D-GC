
from PyQt5.QtWidgets import QAction

from gc2d.view.dialogs import EditAxes


class OpenEditAxesAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        :param parent: the parent widget
        """
        super().__init__('Edit Axes', parent)
        self.model_wrapper = model_wrapper
        #self.setShortcut('Ctrl+Shift+C')
        self.setStatusTip('Opens the Edit Axes Dialog')
        self.setEnabled(self.model_wrapper.model is not None)
        self.model_wrapper.add_observer(self, self.notify)
        self.triggered.connect(self.show_dialog)

    # noinspection PyArgumentList
    def show_dialog(self):
        """
        :return: None
        """
        i = -1
        while i == -1:
            i = EditAxes(self.parent(), self.model_wrapper)

    def notify(self, name, value):
        if name == 'model':
            self.setEnabled(value is not None)
