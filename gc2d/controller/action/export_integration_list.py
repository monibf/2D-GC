from PyQt5.QtWidgets import QAction, QApplication


class ExportIntegrationAction(QAction):

    def __init__(self, parent, model_wrapper):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Copy Integration to Clipboard', parent)
        self.window = parent
        self.model_wrapper = model_wrapper
        self.status_bar = parent.status_bar

        self.clipboard = QApplication.clipboard()
        self.clipboard.clear(mode=self.clipboard.Clipboard)
        self.clipboard.setText('Initialized')

        self.setShortcut('Ctrl+Y')
        self.setStatusTip('Copy Integration to Clipboard')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.export_integration_list)

        self.model_wrapper.add_observer(self, self.notified)

    def export_integration_list(self):
        """
        Export the 2D plot
        :return: bool if file was successfully exported
        """

        # Check if a plot is loaded
        if self.window.plot_2d is not None:

            # Copy the integration list
            csv = self.create_csv_array()
            self.clipboard.setText(csv)
            self.status_bar.showMessage("Copied integration list to clipboard")
            return True

        # Otherwise, no data was loaded.
        print("No data loaded")
        return False

    def create_csv_array(self):
        integration_array = self.model_wrapper.integrations.values()

        csv = ""
        for integration in integration_array:
            csv += str(integration.id + 1) + ", " + integration.label + ", " + \
                   str(integration.mean) + ", " + str(integration.sum) + "\r\n"

        return str(csv)

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)

