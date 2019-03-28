from PyQt5.Qt import QTableWidget, QTableWidgetItem, QHeaderView
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
        self.setColumnCount(2)
        # self.setRowCount(7)
        model_wrapper.add_observer(self, self.notify)
        self.currentItemChanged.connect(self.select)
        self.cellChanged.connect(self.changeLabel)

        self.horizontalHeader().setStretchLastSection(True) 
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def notify(self, name, value):
        """
        Updates the image rendered to match current integration data.
        Clears list if no chromatogram is opened
        :return: None
        """
        if name == 'integrationUpdate':
            self.redrawList(value) 
        elif name == 'model':
            if value is None:
                self.clear()
        

    def redrawList(self, value):
        """
        Takes the Integration objects from param value and draws them in the integrationList
        :param value: list of Integration objects
        :return: None
        """
        print (self.rowCount(), len(value))
        self.blockSignals(True)
        if len(value) > self.rowCount():
            self.insertRow(len(value) - 1)
        for row, integration in enumerate(value):
            self.setItem(row, 0, QTableWidgetItem(integration.label))
            self.setItem(row, 1, QTableWidgetItem(str(integration.value)))
        self.blockSignals(False)

       
    def select(self):
        # still tryout
        for index in self.selectedIndexes():
            print(index.row(), index.column())
    
    def changeLabel(self):
        """
        Takes an edited label and saves this to the appropriate Integration object in the model_wrapper
        :return: None
        """
        if self.currentColumn() == 0: # currently only labels can be edited
            self.model_wrapper.update_integration(self.currentRow(), label=self.currentItem().text())