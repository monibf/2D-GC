from PyQt5.QtWidgets import QAction, QFileDialog


class ExportIntegrationAction(QAction):

    def __init__(self, parent, model_wrapper, shortcut=None):
        """
        :param parent: The parent widget
        :param model_wrapper: The Model Wrapper
        """
        super().__init__('Export to CSV', parent)
        self.window = parent
        self.model_wrapper = model_wrapper

        if shortcut is not None:
            self.setShortcut(shortcut)

        self.setStatusTip('Export to CSV')
        self.setEnabled(model_wrapper.model is not None)
        self.triggered.connect(self.export_integration_list)

        self.model_wrapper.add_observer(self, self.notified)

    def export_integration_list(self):
        """
        Export the integration list to CSV
        :return: bool if data was successfully exported
        """

        # Check if a plot is loaded
        if self.model_wrapper.model is not None:

            path = QFileDialog.getSaveFileName(self.window, 'Export to CSV')[0]
            if path is '':
                return

            # Export the integration list
            integration_array = self.model_wrapper.integrations.values()

            with open(path, 'w') as file:
                for integration in integration_array:
                    line = '{0}, {1}, {2}\r\n'.format(integration.label, str(integration.mean), str(integration.sum))
                    file.write(line)

            return True

        # Otherwise, no data was loaded.
        return False

    def notified(self, name, model):
        if name == 'model':
            self.setEnabled(model is not None)

