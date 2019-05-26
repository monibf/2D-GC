from PyQt5 import QtCore
from PyQt5.Qt import QHeaderView, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox
from enum import Enum
from decimal import Decimal
from gc2d.controller.integration.handler import Handler

class Col(Enum):
    show = 0
    label = 1
    mean = 2
    integration = 3
    clear = 4


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

        self.precision = 5 #amount of decimals displayed

        self.setColumnCount(len(Col))
        self.setHorizontalHeaderLabels((' ', 'Label', 'Mean Count', 'Sum', ' '))
        self.horizontalHeader().setDefaultSectionSize(130)
        self.horizontalHeader().setSectionResizeMode(Col.show.value, QHeaderView.ResizeToContents)
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
        elif name == 'model':
            if value is None:
                self.clear()

    def new_row(self, integration):
        """
        Initializes a new row with the appropriate fields
        :param integration: the new integration value
        """
        row = self.rowCount()
        self.insertRow(row)

        clear_button = QPushButton()
        clear_button.setText('Clear')
        clear_button.setMinimumWidth(2)
        clear_button.pressed.connect(lambda: self.clear_value(integration.id))
        self.setCellWidget(row, Col.clear.value, clear_button)

        show_toggle = QCheckBox()
        show_toggle.stateChanged.connect(lambda: self.select(integration.id))
        self.setCellWidget(row, Col.show.value, show_toggle)
        
        self.showing.append(integration.id)
        self.redraw_row(integration)

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
    

    def select(self, key):
        # in progress
        self.handler.toggle_show(key)
      
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
        row = self.showing.index(key)
        self.removeRow(row)
        self.handler.clear_value(key)   
        del self.showing[row]
        
