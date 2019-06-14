from PyQt5.QtWidgets import QAction, QFileDialog


class ExportPlot1DAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export 1D plot', parent)
        self.window = parent
        self.model_wrapper = model_wrapper

        if shortcut is not None:
            self.setShortcut(shortcut)
        self.setStatusTip('Export 1D plot')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.export_plot)

        self.model_wrapper.add_observer(self, self.notified)

    def export_plot(self):
        """
        Export the 1D plot
        :return: bool if file was successfully exported
        """

        # Check if a model is loaded
        if self.model_wrapper.model is not None:
            plot = self.window.plot_1d
            path = QFileDialog.getSaveFileName(self.window, 'Export 1D plot',
                                               filter='png files (*.png)')[0]
            if path is '':
                return False

            # Check if the png file extension was added
            elif not path.lower().endswith(".png"):
                path = path + ".png"

            # Save the plot
            plot.grab().save(path)
            return True

        # Otherwise, no data was loaded.
        return False

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
