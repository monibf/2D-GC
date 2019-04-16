from PyQt5 import QtCore
from PyQt5.Qt import QHeaderView, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox
from gc2d.controller.integration.handler import Handler

class IntegrationList(QTableWidget):
    def __init__(self, model_wrapper, parent=None):
        """
        The IntegrationList class shows the integration and selection data from model_wrapper
        It is also responsible for handling some user interaction with integration data
        :param model_wrapper: the wrapper of the model.
        :param parent: the parent of this Widget.
        """
        super().__init__(parent)

        self.showing = []
        self.handler = Handler(model_wrapper)
        model_wrapper.add_observer(self, self.notify)
        
        self.cellChanged.connect(self.change_label)

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels((' ', 'Label', 'Mean Count', ' '))
        self.horizontalHeader().setDefaultSectionSize(180)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

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
        self.setCellWidget(row, 3, clear_button)

        show_toggle = QCheckBox()
        show_toggle.stateChanged.connect(lambda: self.select(integration.id))
        self.setCellWidget(row, 0, show_toggle)
        
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
        self.blockSignals(True)
        row = self.showing.index(integration.id)
        self.setItem(row, 1, QTableWidgetItem(integration.label))
        value_item = QTableWidgetItem(str(integration.value))
        value_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.setItem(row, 2, value_item)
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
        
