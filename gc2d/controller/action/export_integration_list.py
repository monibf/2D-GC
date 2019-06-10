from PyQt5.QtWidgets import QAction, QApplication


class ExportIntegrationAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export Integrations to CSV File', parent)
        self.window = parent
        self.model_wrapper = model_wrapper

        if shortcut is not None:
            self.setShortcut(shortcut)

        self.setStatusTip('Export Integrations to CSV File')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.export_integration_list)

        self.model_wrapper.add_observer(self, self.notified)

    def export_integration_list(self):
        """
        Export the integration list to a CSV file
        :return: bool if data was successfully exported
        """

        # Check if a plot is loaded
        if self.model_wrapper.model is not None:

            # Export the integration list
            integration_array = self.model_wrapper.integrations.values()

            csv = ""
            for integration in integration_array:
                csv += integration.label + ", " + \
                       str(integration.mean) + ", " + str(integration.sum) + "\r\n"

            return True

        # Otherwise, no data was loaded.
        return False

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)

