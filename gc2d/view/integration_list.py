from PyQt5.Qt import QTableWidget, QTableWidgetItem, QHeaderView, QPushButton
from PyQt5 import QtCore
from gc2d.model.model_wrapper import ModelWrapper
from gc2d.model.integration import Integration

class IntegrationList(QTableWidget):
    def __init__(self, model_wrapper, parent=None):
        """
        The IntegrationList class shows the integration and selection data from model_wrapper
        It is also responsible for handling some user interaction with integration data
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)
        self.model_wrapper = model_wrapper
        
        model_wrapper.add_observer(self, self.notify)
        self.itemSelectionChanged.connect(self.select)
        self.cellChanged.connect(self.changeLabel)

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(('Label', 'Mean Count', ' '))
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
        self.blockSignals(True)
        if len(value) > self.rowCount():
            # add row
            row = len(value) - 1
            self.insertRow(row)
            clear_button = QPushButton()
            clear_button.setText('Clear')
            clear_button.pressed.connect(lambda: self.clearValue(row))
            self.setCellWidget(row, 2, clear_button)
        elif len(value) < self.rowCount():
            # remove row
            self.removeRow(len(value))

        for row, integration in enumerate(value):
            # update values
            self.setItem(row, 0, QTableWidgetItem(integration.label))
            value = QTableWidgetItem(str(integration.value))
            value.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(row, 1, value)
        self.blockSignals(False)
       
    def select(self):
        return
        # still tryout -> will need to show selections in the plot_2d and plot_3d

    def changeLabel(self):
        """
        Takes an edited label and saves this to the appropriate Integration object in the model_wrapper
        :return: None
        """
        if self.currentColumn() == 0: # currently only labels can be edited
            self.model_wrapper.update_integration(self.currentRow(), label=self.currentItem().text())
    
    def clearValue(self, row):
        """
        Removes an integration from the model wrapper
        :return: None
        """
        self.model_wrapper.clear_integration(row)