from PyQt5 import QtCore
from PyQt5.Qt import QHeaderView, QPushButton, QTableWidget, QTableWidgetItem
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
        
        self.itemSelectionChanged.connect(self.select)
        self.cellChanged.connect(self.change_label)

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
            self.redraw_row(value)
        elif name == 'newIntegration':
            self.new_row(value)
        elif name == 'model':
            if value is None:
                self.clear()

    def new_row(self, integration):
        row = self.rowCount()
        self.insertRow(row)
        clear_button = QPushButton()
        clear_button.setText('Clear')
        clear_button.pressed.connect(lambda: self.clear_value(integration.id))
        self.setCellWidget(row, 2, clear_button)
        self.showing.append(integration.id)
        self.redraw_row(integration)

    def redraw_row(self, integration):
        """
        Takes the Integration objects from param value and draws them in the integrationList
        :param value: list of Integration objects
        :return: None
        """
        if integration.id not in self.showing:
            return
        self.blockSignals(True)
        row = self.showing.index(integration.id)
        self.setItem(row, 0, QTableWidgetItem(integration.label))
        value_item = QTableWidgetItem(str(integration.value))
        value_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.setItem(row, 1, value_item)
        self.blockSignals(False)
    

    def select(self):
        return
        # still tryout -> will need to show selections in the plot_2d and plot_3d

    def change_label(self):
        """
        Takes an edited label and saves this to the appropriate Integration object in the model_wrapper
        :return: None
        """
        self.handler.change_label(self.showing[self.currentRow()], self.currentItem().text())
       
    def clear_value(self, key):
        row = self.showing.index(key)
        self.removeRow(row)
        self.handler.clear_value(key)   
        del self.showing[row]
        
