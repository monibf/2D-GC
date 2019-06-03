from PyQt5.QtWidgets import QAction


class ExportPlot3DAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export 3D plot', parent)
        self.window = parent
        self.model_wrapper = model_wrapper

        self.setShortcut('Ctrl+R')
        self.setStatusTip('Export 3D plot')
        self.setDisabled(True)
        self.triggered.connect(self.export_plot)

        self.model_wrapper.add_observer(self, self.notified)

    def export_plot(self):
        """
        Export the 2D plot to a png file
        :return: None
        """

        # Check if a plot is loaded
        if self.window.plot_3d is not None:
            # x = self.plot.grabWindow()
            print('Exported 3D plot')
            return True

        # Otherwise, no data was loaded.
        print("No data loaded")
        return False

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)
