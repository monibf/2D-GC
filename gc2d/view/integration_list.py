from PyQt5.Qt import QTableWidget, QTableWidgetItem
from gc2d.model.model_wrapper import ModelWrapper
from gc2d.model.integration import Integration

class IntegrationList(QTableWidget):
    def __init__(self, model_wrapper, parent=None):
        """
        The Plot2DWidget is responsible for rendering the 2D chromatogram data.
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.model_wrapper = model_wrapper
        # self.notify('integrationUpdate', self)
        self.setColumnCount(2)
        model_wrapper.add_observer(self, self.notify)


    def notify(self, name, value):
        """
        Updates the image rendered to match current integration data.
        :return: None
        """

        if name == 'model':
            if value is None:
                self.clear()
        if name == 'integrationUpdate':
            self.updateList(value) # expects row/integration number
       

    def updateList(self, row):
        integration = self.model_wrapper.integrations[row]
        if row > self.rowCount() - 1:
            self.insertRow()
        # self.setItem(row, 0, QTableWidgetItem(integration.label)
        # self.setItem(row, 1, QTableWidgetItem(integration.value)

       

