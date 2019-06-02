from PyQt5 import QtCore
from PyQt5.Qt import QHeaderView, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox
from enum import Enum
from decimal import Decimal
from gc2d.controller.integration.handler import Handler

class Col(Enum):
    label = 0
    mean = 1
    integration = 2
    clear = 3


class IntegrationList(QTableWidget):
    def __init__(self, model_wrapper, parent=None):
        """
        The IntegrationList class shows the integration and selection data from model_wrapper
        It is also responsible for handling some user interaction with integration data
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)

        # self.showing contains the id of each shown integration
        # the index in showing corresponds with the row in the table
        self.showing = [] 

        # self.handler is a controller for all actions from this view with model_wrapper
        self.handler = Handler(model_wrapper)
        model_wrapper.add_observer(self, self.notify)
        
        self.cellChanged.connect(self.change_label)

        self.previous_selection = []
        self.itemSelectionChanged.connect(self.select)

        self.precision = 5 #amount of decimals displayed

        self.setColumnCount(len(Col))
        self.setHorizontalHeaderLabels(('Label', 'Mean Count', 'Sum', ' '))
        self.horizontalHeader().setDefaultSectionSize(130)
        self.horizontalHeader().setSectionResizeMode(Col.label.value, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(Col.mean.value, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(Col.integration.value, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(Col.clear.value, QHeaderView.Stretch)

    def notify(self, name, value):
        """
        Updates the image rendered to match current integration data.
        Clears list if no chromatogram is opened
        :return: None
        """
        if name == 'integrationUpdate':
            self.redraw_row(value)
        elif name == 'newIntegration':
            self.new_row(value)
        elif name == 'removeIntegration' and value.id in self.showing:
            self.clear_row(self.showing.index(value.id))
        elif name == 'showIntegration':
            if self.showing.index(value.id) not in self.previous_selection and value.show is True:
                self.set_selected_row(self.showing.index(value.id))
        elif name == 'model':
            if value is None:
                self.setRowCount(0) 

    def new_row(self, integration):
        """
        Initializes a new row with the appropriate fields
        :param integration: the new integration value
        """
        row = self.rowCount()
        self.previous_selection = [row]
        self.insertRow(row)

        clear_button = QPushButton()
        clear_button.setText('Clear')
        clear_button.setMinimumWidth(2)
        clear_button.pressed.connect(lambda: self.clear_value(integration.id))
        self.setCellWidget(row, Col.clear.value, clear_button)
        
        self.showing.append(integration.id)
        self.redraw_row(integration)
        self.set_selected_row(self.showing.index(row))

    def redraw_row(self, integration):
        """
        Takes the integration, and redraws the variable fields in the row
        :param value: list of Integration objects
        :return: None
        """
        if integration.id not in self.showing:
            return
        self.blockSignals(True) # signals are blocked during redraw so cellChanged -> change_label is not called
        row = self.showing.index(integration.id)
        self.setItem(row, Col.label.value, QTableWidgetItem(integration.label))


        mean_item = QTableWidgetItem('{num:.{precision}E}'.format(num=Decimal(integration.mean), precision=self.precision))
        mean_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.setItem(row, Col.mean.value, mean_item)

        sum_item = QTableWidgetItem('{num:.{precision}E}'.format(num=Decimal(integration.sum), precision=self.precision))
        sum_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.setItem(row, Col.integration.value, sum_item)
        self.blockSignals(False)
    
    def select(self):
        current_selection =[]
        for selected in self.selectedIndexes():
            row = selected.row()
            if row not in current_selection:
                self.handler.show(self.showing[row])
                current_selection.append(row)
                if row in self.previous_selection:
                    self.previous_selection.remove(row)
        to_hide = self.previous_selection
        self.previous_selection = current_selection  
        for previous in to_hide:
            self.handler.hide(self.showing[previous])
        
        
    def change_label(self):
        """
        Takes an edited label and hands this to the handler, with the key of the appropriate integration and the edited text
        :return: None
        """
        self.handler.change_label(self.showing[self.currentRow()], self.currentItem().text())
       
    def clear_value(self, key):
        """
        Removes row and signals to controller to remove the integration value from the model
        :param key: identifier of the row to be removed
        """
        self.clear_row(self.showing.index(key))
        self.handler.clear_value(key)

    def set_selected_row(self, row):
        self.blockSignals(True)
        self.clearSelection()
        self.setCurrentCell(row, Col.label.value)
        self.select()
        self.previous_selection = [row]
        self.blockSignals(False)

    def clear_row(self, row):
        """
        Removes row the corresponding integration from local data
        :param row: which row to remove
        """
        self.removeRow(row)
        del self.showing[row]
        for ix, selected in enumerate(self.previous_selection):
            if selected > row:
                self.previous_selection[ix] -= 1
        
           
        
        
